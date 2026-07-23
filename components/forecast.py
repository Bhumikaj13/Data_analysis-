import streamlit as st
import pandas as pd
import plotly.express as px


def show_forecast(df):

    st.subheader("📈 Sales Forecast")

    if "Order Date" not in df.columns:
        st.warning("Order Date column not found.")
        return

    if "Sales" not in df.columns:
        st.warning("Sales column not found.")
        return

    data = df.copy()

    data["Order Date"] = pd.to_datetime(
        data["Order Date"],
        errors="coerce"
    )

    data = data.dropna(subset=["Order Date"])

    sales = (
        data.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    sales = sales.sort_values("Order Date")

    # 7-Day Moving Average
    sales["Forecast"] = (
        sales["Sales"]
        .rolling(window=7)
        .mean()
    )

    fig = px.line(
        sales,
        x="Order Date",
        y=["Sales", "Forecast"],
        title="Sales Forecast (7-Day Moving Average)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    latest_forecast = sales["Forecast"].dropna().iloc[-1]

    st.info(
        f"📊 Estimated sales for the upcoming period: ${latest_forecast:,.2f}"
    )
    