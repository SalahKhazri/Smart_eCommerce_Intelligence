import streamlit as st
import pandas as pd
from components.kpi_cards import show_kpis
from components.charts import score_chart, price_chart, category_chart
st.set_page_config(
    page_title="Smart eCommerce Dashboard",
    layout="wide"
)
st.title("📊 Smart eCommerce Intelligence")
# LOAD DATA
df = pd.read_csv("../data/raw/products.csv")
# CLEAN COLUMN NAMES (important)
df.columns = df.columns.str.strip()
# =========================
# FEATURE ENGINEERING
# =========================
if "score" not in df.columns:
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    # création d'un score simple ML-like
    df["score"] = (
        (df["price"].max() - df["price"]) / df["price"].max()
    )
# remove nulls
df = df.dropna(subset=["price"])
# # CLEAN
# df = df.dropna(subset=["price", "score"])
# KPI
show_kpis(df)
st.markdown("---")
# CHARTS
score_chart(df)
price_chart(df)
category_chart(df)
# TOP PRODUCTS
st.subheader("🏆 Top Products")
top = df.sort_values("score", ascending=False).head(10)
st.dataframe(top[["title", "price", "score", "category"]])