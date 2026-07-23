import streamlit as st


def format_currency(value):
    """
    Convert number into readable currency.
    Example:
    1520 -> $1.52K
    3500000 -> $3.50M
    """

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"

    if value >= 1000:
        return f"${value/1000:.2f}K"

    return f"${value:.2f}"


def show_kpis(df):

    sales = 0
    profit = 0
    orders = 0
    customers = 0

    if "Sales" in df.columns:
        sales = df["Sales"].sum()

    if "Profit" in df.columns:
        profit = df["Profit"].sum()

    if "Order ID" in df.columns:
        orders = df["Order ID"].nunique()

    if "Customer Name" in df.columns:
        customers = df["Customer Name"].nunique()

    avg_order = 0

    if orders != 0:
        avg_order = sales / orders

    st.subheader("📊 Business Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="💰 Total Sales",
            value=format_currency(sales)
        )

    with col2:
        st.metric(
            label="📈 Total Profit",
            value=format_currency(profit)
        )

    with col3:
        st.metric(
            label="📦 Orders",
            value=f"{orders:,}"
        )

    with col4:
        st.metric(
            label="👥 Customers",
            value=f"{customers:,}"
        )

    with col5:
        st.metric(
            label="🧾 Avg Order",
            value=format_currency(avg_order)
        )

    st.divider()