import json

import pandas as pd


def save_to_json(products, filename):

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            products,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Données sauvegardées dans {filename}")


def save_to_csv(products, filename):

    df = pd.DataFrame(products)

    df.to_csv(filename, index=False, encoding="utf-8")

    print(f"Données sauvegardées dans {filename}")