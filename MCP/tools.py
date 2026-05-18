from LLM.recommender import analyze_product

def get_top_products(df, k=5):
    return df.sort_values("score", ascending=False).head(k)

def explain_product(product):
    return analyze_product(product)