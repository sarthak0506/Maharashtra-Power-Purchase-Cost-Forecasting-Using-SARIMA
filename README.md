# 🔌 Power Purchase Cost Forecasting for Maharashtra

This project involves forecasting the monthly **power purchase cost** for the state of **Maharashtra**, India, using time series modeling techniques. The goal is to assist in better energy budgeting and cost planning using historical data trends.

## 📈 Project Overview

- **Objective:** Predict future power purchase costs based on past consumption data.
- **Data Source:** POSOCO (Power System Operation Corporation) — Maharashtra regional electricity data.
- **Model Used:** SARIMA (Seasonal AutoRegressive Integrated Moving Average)
- **Dashboard:** Built using Streamlit for interactive visualization of forecasts.

---

## 🔧 Technologies Used

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **statsmodels (SARIMA)**
- **Streamlit** (for web app/dashboard)

---

## 🚀 Features

- Time series forecasting using SARIMA model
- Data preprocessing and seasonal analysis
- Evaluation using RMSE and visual validation
- Interactive Streamlit dashboard to view future predictions and historical trends

---

## 📂 Project Structure
├── data/
│ └── maharashtra_power_cost.csv
├── src/
│ ├── preprocessing.py
│ ├── modeling.py
│ └── forecast.py
├── dashboard/
│ └── app.py
├── README.md
└── requirements.txt

---

## 📊 Sample Visualizations

- Line plots of historical vs. predicted costs
- Seasonal decomposition of the time series
- Forecast charts with confidence intervals

---

## ▶️ How to Run

1. **Clone the repo**
```bash
git clone https://github.com/your-username/maharashtra-power-cost-forecast.git
cd maharashtra-power-cost-forecast

Create a virtual environment and install dependencies

Run the Streamlit app
streamlit run dashboard/app.py
