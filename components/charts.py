import streamlit as st
import pandas as pd
import plotly.express as px


def show_charts(df):

    st.subheader("📈 Sales Analytics")

    # ==============================
    # Monthly Sales Trend
    # ==============================
    if "Order Date" in df.columns and "Sales" in df.columns:

        temp = df.copy()

        temp["Order Date"] = pd.to_datetime(
            temp["Order Date"],
            errors="coerce"
        )

        monthly_sales = (
            temp.groupby(temp["Order Date"].dt.to_period("M"))["Sales"]
            .sum()
            .reset_index()
        )

        monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

        fig = px.line(
            monthly_sales,
            x="Order Date",
            y="Sales",
            title="Monthly Sales Trend",
            markers=True
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Monthly Profit Trend
    # ==============================
    if "Order Date" in df.columns and "Profit" in df.columns:

        temp = df.copy()

        temp["Order Date"] = pd.to_datetime(
            temp["Order Date"],
            errors="coerce"
        )

        monthly_profit = (
            temp.groupby(temp["Order Date"].dt.to_period("M"))["Profit"]
            .sum()
            .reset_index()
        )

        monthly_profit["Order Date"] = monthly_profit["Order Date"].astype(str)

        fig = px.line(
            monthly_profit,
            x="Order Date",
            y="Profit",
            title="Monthly Profit Trend",
            markers=True
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Two Charts Side by Side
    # ==============================
    col1, col2 = st.columns(2)

    # Category Pie Chart
    with col1:

        if "Category" in df.columns:

            category_sales = (
                df.groupby("Category")["Sales"]
                .sum()
                .reset_index()
            )

            fig = px.pie(
                category_sales,
                names="Category",
                values="Sales",
                hole=0.45,
                title="Sales by Category"
            )

            st.plotly_chart(fig, use_container_width=True)

    # Region Bar Chart
    with col2:

        if "Region" in df.columns:

            region_sales = (
                df.groupby("Region")["Sales"]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                region_sales,
                x="Region",
                y="Sales",
                color="Region",
                title="Region Wise Sales"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # State Sales
    # ==============================

    if "State" in df.columns:

        st.subheader("📍 Top States by Sales")

        state_sales = (
            df.groupby("State")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            state_sales,
            x="Sales",
            y="State",
            orientation="h",
            title="Top 10 States"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Top Products
    # ==============================

    if "Product Name" in df.columns:

        st.subheader("🏆 Top Selling Products")

        top_products = (
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top_products,
            x="Sales",
            y="Product Name",
            orientation="h",
            title="Top 10 Products"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Top Customers
    # ==============================

    if "Customer Name" in df.columns:

        st.subheader("👥 Top Customers")

        top_customers = (
            df.groupby("Customer Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top_customers,
            x="Sales",
            y="Customer Name",
            orientation="h",
            title="Top Customers"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Segment Analysis
    # ==============================

    if "Segment" in df.columns:

        st.subheader("📦 Segment Analysis")

        segment_sales = (
            df.groupby("Segment")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            segment_sales,
            x="Segment",
            y="Sales",
            color="Segment",
            title="Sales by Segment"
        )

        st.plotly_chart(fig, use_container_width=True)