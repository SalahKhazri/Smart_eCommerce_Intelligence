from agents.shopify_agent import ShopifyAgent

from agents.woocommerce_agent import WooCommerceAgent

from utils.helpers import save_to_json
from utils.helpers import save_to_csv


def main():

    all_products = []

    print("\n===== SHOPIFY AGENT =====\n")

    # shopify_store = "https://gymshark.com"
    stores = [

        "https://gymshark.com",

        "https://allbirds.com",

        "https://colourpop.com",

        "https://kith.com",

        "https://nomadgoods.com"
    ]

    for shopify_store in stores:
        shopify_agent = ShopifyAgent(shopify_store)
        shopify_products = shopify_agent.fetch_products()

        print(f"{len(shopify_products)} produits Shopify récupérés")

        all_products.extend(shopify_products)

    

    print("\n===== WOOCOMMERCE AGENT =====\n")

    woocommerce_store = "https://demo.woostify.com/shop/"

    woocommerce_agent = WooCommerceAgent(woocommerce_store)

    woocommerce_products = woocommerce_agent.fetch_products()

    print(f"{len(woocommerce_products)} produits WooCommerce récupérés")

    all_products.extend(woocommerce_products)

    print("\n===== PRODUITS =====\n")

    for product in all_products[:5]:

        print(product)
        print("-" * 50)

    save_to_json(all_products, "data/products.json")

    save_to_csv(all_products, "data/products.csv")


if __name__ == "__main__":
    main()