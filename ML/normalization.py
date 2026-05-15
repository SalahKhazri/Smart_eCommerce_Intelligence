from sklearn.preprocessing import StandardScaler

def normalize(df, cols):

    scaler = StandardScaler()

    # keep only existing columns
    cols = [c for c in cols if c in df.columns]

    df[cols] = scaler.fit_transform(df[cols])

    return df