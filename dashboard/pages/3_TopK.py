import streamlit as st
import pandas as pd

st.title("🏆 Top-K Products")

df = pd.read_csv("../reports/topk_products.csv")

top_products = df.sort_values(
    by="score",
    ascending=False
)

st.dataframe(top_products)

best = top_products.iloc[0]

st.success(
    f"""
    Best Product:
    {best['title']}
    
    Score: {best['score']:.2f}

    Category: {best['category']}
    """
)