from ML.load_data import load_data
from ML.clean_data import clean_data
from ML.feature_engineering import create_features
from ML.normalization import normalize
from ML.scoring import compute_score
from ML.topk_selection import get_top_k
from ML.shop_analysis import shop_ranking

# ML modules
from ML.clustering import kmeans_cluster, dbscan_cluster
from ML.dimensionality import apply_pca
from ML.prediction import train_random_forest, train_xgboost
from ML.association_rules import generate_association_rules


def run_pipeline():

    print("🚀 Pipeline started")

    # =========================
    # 1. LOAD
    # =========================
    df = load_data()
    print("✔ Load:", df.shape)

    # =========================
    # 2. CLEAN
    # =========================
    df = clean_data(df)
    print("✔ Clean:", df.shape)

    # =========================
    # 3. FEATURES
    # =========================
    df = create_features(df)
    print("✔ Features:", df.shape)

    # =========================
    # 4. NORMALIZATION
    # =========================
    df = normalize(df, ["price", "is_available", "price_level", "title_length"])
    print("✔ Normalize:", df.shape)

    # =========================
    # 5. SCORING
    # =========================
    df = compute_score(df)
    print("✔ Score computed")

    # =========================
    # 6. TOP-K + SHOP RANKING
    # =========================
    topk = get_top_k(df, k=20)
    shops = shop_ranking(df)

    topk.to_csv("outputs/topk_products.csv", index=False)
    shops.to_csv("outputs/shop_ranking.csv")

    print("✔ Top-K & Shops saved")

    # =========================
    # 7. CLUSTERING
    # =========================
    df, _ = kmeans_cluster(df)
    df, _ = dbscan_cluster(df)
    print("✔ Clustering done")

    # =========================
    # 8. PCA
    # =========================
    df, _ = apply_pca(df)
    print("✔ PCA done")

    # =========================
    # 9. ML MODELS
    # =========================
    df, rf_model = train_random_forest(df)
    df, xgb_model = train_xgboost(df)
    print("✔ ML predictions done")

    # =========================
    # 10. ASSOCIATION RULES
    # =========================
    rules = generate_association_rules(df)

    # =========================
    # 11. SAVE OUTPUTS
    # =========================
    df.to_csv("outputs/final_products_ml.csv", index=False)
    rules.to_csv("outputs/association_rules.csv", index=False)

    print("🚀 Advanced ML pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()