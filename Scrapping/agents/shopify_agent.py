import requests

from agents.base_agent import BaseAgent


class ShopifyAgent(BaseAgent):

    def __init__(self, store_url):

        super().__init__("Shopify")

        self.store_url = store_url

    def fetch_products(self):

        all_products = []

        page = 1

        MAX_PAGES = 10

        while page <= MAX_PAGES:

            url = (
                f"{self.store_url}/products.json"
                f"?limit=250&page={page}"
            )

            print(f"Scraping page {page}...")

            try:

                response = requests.get(url, timeout=10)

                if response.status_code != 200:
                    break

                data = response.json()

                products = data.get("products", [])

                if not products:
                    break

                for product in products:

                    variants = product.get("variants", [])
                    images = product.get("images", [])

                    product_data = {

                        "platform": "Shopify",

                        "id": product.get("id"),

                        "title": product.get("title"),

                        "vendor": product.get("vendor"),

                        "category": product.get("product_type"),

                        "description": product.get("body_html"),

                        "tags": product.get("tags"),

                        "created_at": product.get("created_at"),

                        "updated_at": product.get("updated_at"),

                        "price": (
                            variants[0].get("price")
                            if variants else None
                        ),

                        "availability": (
                            variants[0].get("available")
                            if variants else False
                        ),

                        "variants_count": len(variants),

                        "image": (
                            images[0].get("src")
                            if images else None
                        )
                    }

                    all_products.append(product_data)

                page += 1

            except Exception as e:

                print(e)
                break

        return all_products