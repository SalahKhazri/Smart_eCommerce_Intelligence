import plotly.express as px
import streamlit as st

# =========================
# SCORE CHART
# =========================
def score_chart(df):

    fig = px.bar(
        df,
        x="title",
        y="score",
        color="category",
        title="🏆 Product Score Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)


# =========================
# PRICE CHART
# =========================
def price_chart(df):

    fig = px.histogram(
        df,
        x="price",
        nbins=20,
        title="💰 Price Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


# =========================
# CATEGORY CHART
# =========================
def category_chart(df):

    fig = px.pie(
        df,
        names="category",
        title="📦 Products by Category"
    )

    st.plotly_chart(fig, use_container_width=True)