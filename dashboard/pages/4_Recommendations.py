import streamlit as st
import pandas as pd

import os
import sys






BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.append(BASE_DIR)

from LLM.recommender import analyze_product

from MCP.server import MCPServer


st.title("🤖 AI Product Recommendations")

# =========================
# LOAD DATA
# =========================


DATA_PATH = os.path.join(
    BASE_DIR,
    "reports",
    "topk_products.csv"
)

df = pd.read_csv(DATA_PATH)

# fallback score
if "score" not in df.columns:
    df["score"] = 1 / (df["price"] + 1)

# =========================
# TOP PRODUCTS
# =========================

top_products = df.sort_values(
    by="score",
    ascending=False
).head(5)

# =========================
# AI ANALYSIS
# =========================

for _, row in top_products.iterrows():

    st.subheader(row["title"])

    with st.spinner("Generating AI insight..."):

        insight = analyze_product(row)

    st.write(insight)

    st.markdown("---")

# =========================
# MCP
# =========================

server = MCPServer()

results = server.analyze(df)

for title, insight in results:

    st.subheader(title)
    st.write(insight)