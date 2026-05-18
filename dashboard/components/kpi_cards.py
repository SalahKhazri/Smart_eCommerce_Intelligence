import streamlit as st

def show_kpis(df):

    col1, col2, col3 = st.columns(3)

    col1.metric("Products", len(df))

    col2.metric("Avg Price", f"{df['price'].mean():.2f}")

    col3.metric("Avg Score", round(df["score"].mean(), 3))