from sklearn.decomposition import PCA

FEATURES = ["price", "is_available", "price_level", "title_length"]

def apply_pca(df, n_components=2):

    features = df[FEATURES]

    pca = PCA(n_components=n_components)
    components = pca.fit_transform(features)

    df["pca_1"] = components[:, 0]
    df["pca_2"] = components[:, 1]

    return df, pca