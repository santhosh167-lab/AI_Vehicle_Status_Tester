# 🚗 AI-Powered Vehicle Status Validator

This is a mini AI-based testing project designed to validate vehicle status data using both:

- ✅ Rule-based logic (e.g., checking battery/fuel levels)
- 🤖 Sentiment analysis on warning messages (using HuggingFace Transformers)

The project is useful for simulating intelligent validation in automotive domains such as **infotainment systems**, **connected vehicles**, and **telemetry-based alerts**.

---

## 📁 Project Structure

ai_vehicle_status_tester/
├── main.py # Main script to run all test cases
├── models.py # Defines vehicle data schema using Pydantic
├── ai_checker.py # Performs sentiment analysis using transformers
├── sample_response.json # Mock vehicle status data for testing 
└── requirements.txt # Python dependencies

---

## 🚀 Features

- Loads vehicle data from JSON (can simulate API responses)
- Validates structure using `Pydantic`
- Flags:
  - Low battery (`< 25%`)
  - Low fuel (`< 15%`)
- Uses NLP model to detect the **sentiment** of warning messages
- Clean output for each test case

---

## 📦 Dependencies

```txt
pydantic
transformers
torch

Sample Output

🔍 Test Case #3
✅ Schema valid.
Engine: on
Battery: 10%
Fuel: 5%
Warning: Critical warning! Battery and fuel levels dangerously low
⚠️  Low battery detected: 10%
⛽ Low fuel detected: 5%
🧠 Sentiment: NEGATIVE (0.99)

