# 💎 Diamond Price Prediction using KNN

## 📌 Project Overview
A machine learning project that predicts diamond prices using K-Nearest Neighbors (KNN) Regression and deploys the model as an interactive Streamlit web application.

## 🎯 Objectives
- Preprocess and encode dataset features.
- Apply feature scaling.
- Train a KNN regression model.
- Evaluate performance using MAE, RMSE, and R² Score.
- Deploy the model using Streamlit.

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Pickle
- Streamlit

## ⚙️ Machine Learning Workflow
1. Load and explore the dataset.
2. Handle missing values and duplicate rows.
3. Encode categorical features and scale numerical features.
4. Split data into training and testing sets (75:25).
5. Train the KNN regression model.
6. Evaluate model performance.
7. Save the trained pipeline using Pickle.
8. Deploy the application using Streamlit Cloud.

## 📊 Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🚀 Run Locally
Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🌐 Live Demo
[Diamond Price Prediction App](https://diamond-price-prediction-e4hxfnejjcqx9czy8rcyj7.streamlit.app/)

## 📂 Project Structure

```text
diamond-price-prediction/
├── app.py
├── diamond_price_model.pkl
├── requirements.txt
└── README.md
```

## 👨‍💻 Skills Demonstrated
Python, Machine Learning, Data Preprocessing, Feature Encoding, Feature Scaling, Model Evaluation, and Streamlit Deployment.
