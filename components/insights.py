import streamlit as st


def show_insights(df):

    st.subheader("🤖 AI Business Insights")

    insights = []

    # -----------------------------
    # Highest Sales Region
    # -----------------------------
    if "Region" in df.columns and "Sales" in df.columns:

        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        top_region = region_sales.idxmax()

        insights.append(
            f"🌍 **{top_region}** generated the highest sales."
        )

    # -----------------------------
    # Most Profitable Category
    # -----------------------------
    if "Category" in df.columns and "Profit" in df.columns:

        category_profit = (
            df.groupby("Category")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

        top_category = category_profit.idxmax()

        insights.append(
            f"📈 **{top_category}** is the most profitable category."
        )

    # -----------------------------
    # Highest Sales Product
    # -----------------------------
    if "Product Name" in df.columns:

        product_sales = (
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        top_product = product_sales.idxmax()

        insights.append(
            f"🏆 **{top_product}** is the best selling product."
        )

    # -----------------------------
    # Highest Spending Customer
    # -----------------------------
    if "Customer Name" in df.columns:

        customer_sales = (
            df.groupby("Customer Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        top_customer = customer_sales.idxmax()

        insights.append(
            f"👤 **{top_customer}** is the highest spending customer."
        )

    # -----------------------------
    # Profit Margin
    # -----------------------------
    if "Sales" in df.columns and "Profit" in df.columns:

        total_sales = df["Sales"].sum()
        total_profit = df["Profit"].sum()

        if total_sales > 0:

            margin = (total_profit / total_sales) * 100

            insights.append(
                f"💹 Overall profit margin is **{margin:.2f}%**."
            )

    # -----------------------------
    # Loss Making Orders
    # -----------------------------
    if "Profit" in df.columns:

        loss_orders = df[df["Profit"] < 0]

        insights.append(
            f"⚠️ There are **{len(loss_orders)}** loss-making orders."
        )

    # -----------------------------
    # Display Insights
    # -----------------------------
    for insight in insights:
        st.success(insight)
        