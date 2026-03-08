# 🩸 Blood Disease Prediction Web Application

A Machine Learning powered web application that predicts possible blood diseases using Complete Blood Count (CBC) parameters.  
The system provides predictions, visualizes blood values, stores history, and generates downloadable medical reports.

---

## 🚀 Features

- 🔐 User Authentication (Login / Register / Logout)
- 🧠 Machine Learning Blood Disease Prediction
- 📊 Blood Parameter Visualization using Chart.js
- 📁 Prediction History Storage (SQLite Database)
- 🗑 Delete Individual Prediction History
- 🎨 Clean Bootstrap UI

---

## 🧪 Input Parameters

The model predicts diseases using these blood parameters:

- Hemoglobin
- RBC (Red Blood Cell Count)
- Platelets
- MCV (Mean Corpuscular Volume)
- MCH (Mean Corpuscular Hemoglobin)
- MCHC (Mean Corpuscular Hemoglobin Concentration)
- PDW (Platelet Distribution Width)

---

## 🧠 Machine Learning Model

The prediction model was trained using:

- **Algorithm:** Random Forest Classifier
- **Libraries:** Scikit-learn, Pandas, NumPy
- **Dataset:** Blood test dataset (CBC parameters)
