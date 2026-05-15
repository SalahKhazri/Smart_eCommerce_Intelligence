from sklearn.cluster import KMeans, DBSCAN

FEATURES = ["price", "is_available", "price_level", "title_length"]


def kmeans_cluster(df, n_clusters=5):

    features = df[FEATURES]

    model = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = model.fit_predict(features)

    return df, model


def dbscan_cluster(df):

    features = df[FEATURES]

    model = DBSCAN(eps=0.5, min_samples=5)
    df["dbscan_cluster"] = model.fit_predict(features)

    return df, model