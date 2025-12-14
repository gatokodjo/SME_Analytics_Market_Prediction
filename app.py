import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(page_title="SME Analytics & Market Prediction", layout="wide")

# -------------------------------------------------
# MARKET PRICE PREDICTION
# -------------------------------------------------
future_months = ["M+1", "M+2", "M+3", "M+4", "M+5"]
future_prices = [145.2, 147.8, 150.5, 152.1, 154.0]

forecast_df = pd.DataFrame({
    "Month": future_months,
    "Predicted Price": future_prices
})

price_change_pct = round(
    ((future_prices[-1] - future_prices[0]) / future_prices[0]) * 100, 2
)

# -------------------------------------------------
# SME DISBURSEMENT DATA
# -------------------------------------------------
branches = [
    "Matthewton", "Meyerchester", "Alexanderhaven", "South",
    "Hughesmouth", "Lake", "North", "Jessicaville", "Other (2)"
]
branch_disbursement = [456.5, 446.3, 445.4, 415.4, 404.9, 284.3, 252.9, 232.0, 202.9]

employment_status = ["Employed", "Self-Employed", "Student", "Unemployed"]
marital_status = ["Divorced", "Married", "Single", "Widowed"]

np.random.seed(42)
disbursed_by_status = pd.DataFrame(
    np.random.randint(150_000_000, 250_000_000, size=(4, 4)),
    index=employment_status,
    columns=marital_status
)

months = pd.date_range("2025-01-01", "2025-11-01", freq="MS").strftime("%B %Y")
monthly_disbursement = [
    90_000_000, 65_000_000, 55_000_000, 45_000_000, 52_000_000,
    60_000_000, 67_000_000, 72_000_000, 45_000_000, 35_000_000, 10_000_000
]

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("Analytics")

# =================================================
# KPI ROW (ONE LINE)
# =================================================
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Disbursement (Year)", "KES 180k", "14.79% ↑")
kpi2.metric("Total Disbursement (Quarter)", "Ksh 134,906", "-26.21% ↓")
kpi3.metric("Total Disbursement (Month)", "Ksh 159,244", "23.36% ↑")
kpi4.metric("Expected Price Change (5 Months)", f"{price_change_pct}%", "Upward trend")

# =================================================
# MIDDLE ROW (2 CHARTS)
# =================================================
left, right = st.columns(2)

with left:
    st.subheader("Disbursement per Branch")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        x=branch_disbursement,
        y=branches,
        palette="Greens_r",
        ax=ax
    )
    ax.set_xlabel("Sum of Disbursed Amount (M)")
    ax.set_ylabel("")
    st.pyplot(fig)

with right:
    st.subheader("Market Price Forecast")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(future_months, future_prices, marker="o")
    ax.set_ylabel("Market Price")
    ax.set_xlabel("Time")
    st.pyplot(fig)

# =================================================
# BOTTOM ROW (FULL WIDTH)
# =================================================
st.subheader("Disbursed Amt by Disbursement Date: Month")
fig, ax = plt.subplots(figsize=(15, 4))
ax.plot(months, monthly_disbursement, marker="o", color="green")
ax.set_ylabel("Disbursed Amount")
ax.set_xlabel("Month")
plt.xticks(rotation=0)
st.pyplot(fig)

# =================================================
# OPTIONAL: COLLAPSIBLE DETAILS (DOES NOT AFFECT SCREEN)
# =================================================
with st.expander("Detailed Breakdown"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Price Forecast Table")
        st.dataframe(forecast_df, use_container_width=True)

    with col2:
        st.markdown("### Disbursement by Employment & Marital Status")
        fig, ax = plt.subplots(figsize=(6, 4))
        disbursed_by_status.plot(kind="bar", ax=ax)
        ax.set_ylabel("Disbursed Amount")
        ax.set_xlabel("Employment Status")
        ax.legend(title="Marital Status")
        st.pyplot(fig)



# =================================================
# OPTIONAL: COLLAPSIBLE DETAILS (SCREEN-SAFE)
# =================================================
with st.expander("Explanation & Recommended Actions"):
    
    col1, col2 = st.columns(2)

    # -------- Explanation --------
    with col1:
        st.subheader("Why is the price changing?")
        st.write("""
        - Rising production and energy costs  
        - Increasing water scarcity risk  
        - Higher market demand  
        """)

    # -------- Actions --------
    with col2:
        st.subheader("Recommended Actions")
        st.success("Increase inventory before Month +3")
        st.warning("Monitor water risk and supplier prices")

