import matplotlib.pyplot as plt

def plot_top_products(df):
    top = df.head(10)
    plt.bar(top["name"], top["score"])
    plt.xticks(rotation=45)
    plt.show()