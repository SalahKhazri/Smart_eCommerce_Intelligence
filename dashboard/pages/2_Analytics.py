import streamlit as st
import pandas as pd

from components.charts import (
    score_chart,
    price_chart,
    category_chart
)

st.title("📊 Analytics")

df = pd.read_csv("../reports/topk_products.csv")

score_chart(df)

price_chart(df)

category_chart(df)