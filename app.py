import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import matplotlib.pyplot as plt

# Title
st.title("Electricity Price Forecasting (SARIMA Model)")

# Load the model
model_file = st.file_uploader("Upload your SARIMA model (.pkl)", type="pkl")
if model_file is not None:
    model = pickle.load(model_file)
    st.success("Model loaded successfully!")

    # User input for number of months
    months = st.slider("Select number of months to forecast (1-24)", min_value=1, max_value=24, value=12)

    # Prediction button
    if st.button("Predict Future Consumption"):
        forecast = model.get_forecast(steps=months)
        forecast_df = forecast.conf_int()
        forecast_df["forecast"] = forecast.predicted_mean

        # Create index for future months
        last_date = model.data.dates[-1]
        forecast_df.index = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=months, freq='MS')

        # Plotting
        st.subheader("Forecasted Values")
        fig, ax = plt.subplots(figsize=(12, 5))
        forecast_df["forecast"].plot(ax=ax, label="Forecast", color="blue")
        ax.fill_between(forecast_df.index, 
                        forecast_df["lower Total_Power_Purchase"], 
                        forecast_df["upper Total_Power_Purchase"], 
                        color='lightblue', alpha=0.5)
        plt.title("Forecast for Future Months")
        plt.xlabel("Month")
        plt.ylabel("Power Purchase")
        plt.legend()
        st.pyplot(fig)

        # Show forecast table
        st.dataframe(forecast_df[["forecast"]].rename(columns={"forecast": "Forecasted Power Purchase"}))
