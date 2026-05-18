import streamlit as st
import pandas as pd

from components.kpi_cards import show_kpis

st.title("📌 KPI Dashboard")

df = pd.read_csv("../reports/topk_products.csv")

show_kpis(df)