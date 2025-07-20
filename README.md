# 🍽️ FitFuel Calorie Detector

A full-stack web app that detects calories from food images, calculates your BMI, and helps you track your daily intake — all in one smart dashboard.

---

## 🚀 Features

- 📷 Upload food images to detect calorie value using AI
- 🧮 Auto BMI calculation + category classification
- 🎯 Personalized daily calorie goals
- 📊 Visual calorie progress bar by meal (breakfast, lunch, dinner, snacks)
- 🧠 Smart meal tracking using PHP + MySQL

---

## 🛠️ Tech Stack

| Layer      | Tech                        |
|------------|-----------------------------|
| Frontend   | HTML, CSS, JavaScript       |
| Backend    | PHP (Standalone, No XAMPP)  |
| Database   | MySQL                       |
| AI Logic   | Python (OpenCV or Gemini API) |
| Hosting    | Runs locally via `php -S`   |

---

## 📦 Local Setup

1. **Clone the Repo**
   ```bash
   git clone https://github.com/EnochJackson/fitfuel-calorie-detector.git
   cd fitfuel-calorie-detector

2. **Start PHP server**
   - php -S localhost:8000
   - run server.py in your personal environment or cmd

3. **Import MySQL DB**
   - Open your MySQL client
   - Import db/finalqueries.sql

4. **Visit App**
   - http://localhost:8000

---

## 🤖 AI Flow (Food Detection)

   - User uploads image
   - Python script (OpenCV or Gemini API) extracts food name
   - Calorie data fetched via nutrition API
   - Calorie is stored in DB and shown on the progress bar

---

## 📚 Author
   - 👨‍💻 Enoch Jackson C
   - 📫 enochjackson441@gmail.com


