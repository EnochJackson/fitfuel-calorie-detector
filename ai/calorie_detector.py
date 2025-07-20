import requests
from image_upload import upload_image  # Import function

# 🛑 Replace this with your actual USDA API Key
API_KEY = "L5bgM3xdkAjgyob8hZJFDV20bmSU5c4tdOdxO0VM"

# Function to get calories from USDA API
def get_food_calories(food_name):
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={food_name}&api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("foods"):
            food = data["foods"][0]
            calories = next((nutrient["value"] for nutrient in food["foodNutrients"] if nutrient["nutrientName"] == "Energy"), None)
            return calories if calories else "Calorie data not found"
        else:
            return "Food not found"
    else:
        return "API Error"

# 🌟 Main Program
image_path = upload_image()  # Step 1: Upload Image
if image_path:
    food_name = input("Enter the detected food name: ")  # Step 2: Enter Food Name
    calories = get_food_calories(food_name)  # Step 3: Get Calories
    print(f"Calories in {food_name}: {calories} kcal")  # Step 4: Display Output
