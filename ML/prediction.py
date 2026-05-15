from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


# =========================
# FEATURES (COMMON)
# =========================
FEATURES = ["price", "is_available", "price_level", "title_length"]


# =========================
# RANDOM FOREST MODEL
# =========================
def train_random_forest(df):

    features = df[FEATURES]
    target = df["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    df["rf_prediction"] = model.predict(features)

    return df, model


# =========================
# XGBOOST MODEL
# =========================
def train_xgboost(df):

    features = df[FEATURES]
    target = df["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    df["xgb_prediction"] = model.predict(features)

    return df, model