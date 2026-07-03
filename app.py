import streamlit as st

from financial_model import calculate_all
from charts import (
    portfolio_growth_chart,
    investment_vs_returns_chart,
    wealth_breakdown_chart
)
from utils import (
    format_large_number,
    download_dataframe
)

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="How Rich Would I Be?",
    page_icon="💰",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------

st.title("💰 How Rich Would I Be?")
st.caption(
    "An interactive wealth simulator powered by compound interest."
)

st.divider()

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.header("Investment Details")

current_age = st.sidebar.slider(
    "Current Age",
    18,
    60,
    21
)

retirement_age = st.sidebar.slider(
    "Retirement Age",
    current_age + 1,
    70,
    60
)

monthly_sip = st.sidebar.number_input(
    "Monthly SIP (₹)",
    min_value=500,
    max_value=500000,
    value=5000,
    step=500
)

annual_return = st.sidebar.slider(
    "Expected Annual Return (%)",
    1.0,
    25.0,
    12.0,
    0.5
)

inflation = st.sidebar.slider(
    "Inflation (%)",
    0.0,
    10.0,
    6.0,
    0.5
)

calculate = st.sidebar.button(
    "🚀 Calculate Wealth",
    use_container_width=True
)

# ----------------------------
# Main
# ----------------------------

if calculate:

    result = calculate_all(
        current_age,
        retirement_age,
        monthly_sip,
        annual_return,
        inflation
    )

    df = result["yearly_data"]

    # ----------------------------
    # KPI Cards
    # ----------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Future Wealth",
        format_large_number(result["future_value"])
    )

    c2.metric(
        "💵 Total Investment",
        format_large_number(result["total_investment"])
    )

    c3.metric(
        "📈 Wealth Created",
        format_large_number(result["wealth_created"])
    )

    c4.metric(
        "🌍 Real Wealth",
        format_large_number(result["real_value"])
    )

    st.divider()

    # ----------------------------
    # Charts
    # ----------------------------

    st.subheader("Portfolio Growth")

    st.plotly_chart(
        portfolio_growth_chart(df),
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            investment_vs_returns_chart(df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            wealth_breakdown_chart(
                result["total_investment"],
                result["wealth_created"]
            ),
            use_container_width=True
        )

    st.divider()

    # ----------------------------
    # Data Table
    # ----------------------------

    st.subheader("Year-wise Projection")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = download_dataframe(df)

    st.download_button(
        "⬇ Download CSV",
        csv,
        "wealth_projection.csv",
        "text/csv"
    )

else:

    st.info(
        "👈 Enter your investment details from the sidebar and click **Calculate Wealth**."
    )
