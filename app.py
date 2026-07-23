import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from components.filters import apply_filters
from components.kpis import show_kpis
from components.charts import show_charts
from components.insights import show_insights
from components.forecast import show_forecast


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# LOAD CSS
# =====================================

css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================
# LOAD DATA
# =====================================

@st.cache_data
def load_data():

    try:
        df = pd.read_csv(
            "data/superstore.csv",
            encoding="latin1"
        )

    except:

        df = pd.read_csv(
            "data/superstore.csv",
            encoding="cp1252"
        )

    if "Order Date" in df.columns:

        df["Order Date"] = pd.to_datetime(
            df["Order Date"],
            errors="coerce"
        )

    return df


df = load_data()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=120
)

st.sidebar.title("Sales Dashboard")

st.sidebar.write(
    "Interactive Data Analytics Dashboard"
)

st.sidebar.markdown("---")

df = apply_filters(df)

st.sidebar.markdown("---")

st.sidebar.success(
    f"Filtered Records : {len(df):,}"
)

# =====================================
# HERO SECTION
# =====================================

st.title("📊 Sales Analytics Dashboard")

st.markdown(
"""
Analyze business performance using interactive charts,
KPIs, business insights and forecasting.

Built using **Python**, **Pandas**, **Plotly** and **Streamlit**.
"""
)

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================

show_kpis(df)

st.markdown("---")

# =====================================
# DATASET PREVIEW
# =====================================

with st.expander("📄 Preview Dataset"):

    st.dataframe(
        df,
        use_container_width=True,
        height=350
    )

st.markdown("---")

# =====================================
# BASIC INFORMATION
# =====================================

col1, col2, col3 = st.columns(3)

with col1:

    st.info(f"Rows : {df.shape[0]:,}")

with col2:

    st.info(f"Columns : {df.shape[1]}")

with col3:

    memory = round(
        df.memory_usage().sum()/1024,
        2
    )

    st.info(f"Memory : {memory} KB")

st.markdown("---")

# =====================================
# CHART SECTION
# =====================================

show_charts(df)

st.markdown("---")
# =====================================
# AI BUSINESS INSIGHTS
# =====================================

show_insights(df)

st.markdown("---")

# =====================================
# SALES FORECAST
# =====================================

show_forecast(df)

st.markdown("---")

# =====================================
# SALES SUMMARY
# =====================================

st.subheader("📊 Sales Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    if "Category" in df.columns and "Sales" in df.columns:

        category_summary = (
            df.groupby("Category")["Sales"]
            .agg(["sum", "mean", "max"])
            .round(2)
        )

        st.write("### Category Summary")

        st.dataframe(
            category_summary,
            use_container_width=True
        )

with summary_col2:

    if "Region" in df.columns and "Profit" in df.columns:

        region_summary = (
            df.groupby("Region")["Profit"]
            .agg(["sum", "mean", "max"])
            .round(2)
        )

        st.write("### Region Summary")

        st.dataframe(
            region_summary,
            use_container_width=True
        )

st.markdown("---")

# =====================================
# DATA DOWNLOAD
# =====================================

st.subheader("📥 Export Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv",
)

st.markdown("---")

# =====================================
# RAW DATA
# =====================================

st.subheader("📋 Complete Dataset")

st.dataframe(
    df,
    use_container_width=True,
    height=500
)

st.markdown("---")

# =====================================
# DATA STATISTICS
# =====================================

st.subheader("📈 Dataset Statistics")

numeric_columns = df.select_dtypes(include="number")

if not numeric_columns.empty:

    st.dataframe(
        numeric_columns.describe(),
        use_container_width=True
    )

st.markdown("---")

# =====================================
# MISSING VALUES
# =====================================

st.subheader("🧹 Missing Values")

missing = df.isnull().sum()

missing = missing[missing > 0]

if len(missing) == 0:

    st.success("✅ No Missing Values Found")

else:

    st.dataframe(
        missing,
        use_container_width=True
    )

st.markdown("---")

# =====================================
# PROJECT INFORMATION
# =====================================

st.subheader("ℹ About This Project")



st.markdown("---")

# =====================================
# FOOTER
# =====================================

st.markdown(
"""
<div style='text-align:center;
padding:25px;
font-size:16px;
color:gray;'>

Made with ❤️ using
<b>Python + Streamlit + Plotly</b>

<br><br>

© 2026 Sales Analytics Dashboard

</div>
""",
unsafe_allow_html=True
)