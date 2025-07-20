from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import tensorflow as tf
import os
import requests
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwaszx086*",  # Update with your actual DB password
    database="calories"
)
cursor = conn.cursor()

# Load the MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# USDA API Key
API_KEY = "L5bgM3xdkAjgyob8hZJFDV20bmSU5c4tdOdxO0VM"

def get_food_calories(food_name):
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={food_name}&api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("foods"):
            food = data["foods"][0]
            calories = next((nutrient["value"] for nutrient in food["foodNutrients"] if nutrient["nutrientName"] == "Energy"), None)
            return calories if calories else 0
    return 0

def predict_food(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "Error loading image!"}
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    
    predictions = model.predict(image)
    best_prediction = max(tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0], key=lambda x: x[2])
    
    food_label = best_prediction[1]
    calories = get_food_calories(food_label)
    
    return {"food": food_label, "calories": calories}

def update_user_calories(user_id, meal_type, calories):
    cursor.execute(f"""
        UPDATE users
        SET {meal_type} = {meal_type} + %s
        WHERE id = %s
    """, (calories, user_id))
    conn.commit()

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files or 'user_id' not in request.form or 'meal_type' not in request.form:
        return jsonify({"error": "Missing required fields!"}), 400
    
    file = request.files['image']
    user_id = request.form['user_id']
    meal_type = request.form['meal_type']
    
    if meal_type not in ["breakfast", "lunch", "dinner", "snacks"]:
        return jsonify({"error": "Invalid meal type!"}), 400
    
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    result = predict_food(file_path)
    if "error" not in result:
        update_user_calories(user_id, meal_type, result["calories"])
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)