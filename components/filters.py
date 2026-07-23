import streamlit as st


def apply_filters(df):
    """
    Apply sidebar filters and return filtered dataframe.
    """

    st.sidebar.title("📌 Dashboard Filters")

    # -------------------------
    # Region Filter
    # -------------------------
    if "Region" in df.columns:
        regions = sorted(df["Region"].dropna().unique())

        selected_regions = st.sidebar.multiselect(
            "🌍 Select Region",
            options=regions,
            default=regions,
        )

        df = df[df["Region"].isin(selected_regions)]

    # -------------------------
    # Category Filter
    # -------------------------
    if "Category" in df.columns:
        categories = sorted(df["Category"].dropna().unique())

        selected_categories = st.sidebar.multiselect(
            "📦 Select Category",
            options=categories,
            default=categories,
        )

        df = df[df["Category"].isin(selected_categories)]

    # -------------------------
    # Segment Filter
    # -------------------------
    if "Segment" in df.columns:
        segments = sorted(df["Segment"].dropna().unique())

        selected_segments = st.sidebar.multiselect(
            "👥 Select Segment",
            options=segments,
            default=segments,
        )

        df = df[df["Segment"].isin(selected_segments)]

    # -------------------------
    # State Filter
    # -------------------------
    if "State" in df.columns:
        states = sorted(df["State"].dropna().unique())

        selected_states = st.sidebar.multiselect(
            "📍 Select State",
            options=states,
            default=states,
        )

        df = df[df["State"].isin(selected_states)]

    # -------------------------
    # Ship Mode Filter
    # -------------------------
    if "Ship Mode" in df.columns:
        ship_modes = sorted(df["Ship Mode"].dropna().unique())

        selected_ship_modes = st.sidebar.multiselect(
            "🚚 Ship Mode",
            options=ship_modes,
            default=ship_modes,
        )

        df = df[df["Ship Mode"].isin(selected_ship_modes)]

    return df