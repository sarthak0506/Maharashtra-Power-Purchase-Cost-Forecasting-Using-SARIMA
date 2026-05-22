# ⚡ Maharashtra Power Purchase Cost Forecasting Using SARIMA

## 📌 Project Overview

This project focuses on forecasting the **Power Purchase Cost (PPC)** of Maharashtra using historical electricity cost data and Time Series Analysis. Accurate forecasting of power purchase costs helps energy providers and policymakers make informed decisions regarding budgeting, resource allocation, and future energy planning.

The forecasting model is developed using the **SARIMA (Seasonal AutoRegressive Integrated Moving Average)** algorithm, which effectively captures both trend and seasonal patterns present in electricity cost data.

---

## 🎯 Objectives

- Analyze historical power purchase cost data.
- Identify seasonal and trend patterns.
- Build a forecasting model using SARIMA.
- Predict future power purchase costs.
- Visualize historical and forecasted values through an interactive dashboard.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Streamlit

---

## 📊 Methodology

### 1. Data Collection
- Historical power purchase cost data collected from Maharashtra electricity records.

### 2. Data Preprocessing
- Handling missing values
- Date-time conversion
- Data cleaning and transformation

### 3. Exploratory Data Analysis (EDA)
- Trend Analysis
- Seasonal Pattern Analysis
- Time Series Visualization

### 4. Model Development
- SARIMA Model Selection
- Parameter Tuning
- Model Training

### 5. Forecasting
- Future Power Purchase Cost Prediction
- Confidence Interval Generation

### 6. Evaluation
- RMSE (Root Mean Squared Error)
- Forecast Visualization

---

## ✨ Key Features

- Historical Power Purchase Cost Analysis
- Seasonal Trend Detection
- SARIMA-Based Forecasting
- Interactive Streamlit Dashboard
- Future Cost Prediction Visualization
- Model Performance Evaluation

---

## 📂 Project Structure

```text
Power-Purchase-Cost-Forecasting/
│
├── data/
│   └── power_purchase_cost.csv
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── preprocessing.py
│   ├── modeling.py
│   └── forecasting.py
│
├── images/
│   ├── architecture.png
│   ├── dashboard.png
│   └── forecast.png
│
├── requirements.txt
├── README.md
└── model.pkl
```

---

## 📈 Results

The SARIMA model successfully captured the seasonal and trend components of the power purchase cost data and generated reliable forecasts for future periods. The model demonstrated strong predictive performance and can assist in energy cost planning and decision-making.

---

## 🔮 Future Enhancements
- Integration with real-time electricity market data
- Advanced forecasting using LSTM and Prophet models
- Multi-state power cost comparison
- Deployment on cloud platforms
- Automated report generation

---

⭐ If you found this project useful, consider giving it a star on GitHub.
