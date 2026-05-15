import requests

from bs4 import BeautifulSoup

from agents.base_agent import BaseAgent


class WooCommerceAgent(BaseAgent):

    def __init__(self, shop_url):
        super().__init__("WooCommerce")
        self.shop_url = shop_url

    def fetch_products(self):

        try:

            response = requests.get(self.shop_url)

            if response.status_code != 200:
                print(f"Erreur WooCommerce : {response.status_code}")
                return []

            soup = BeautifulSoup(response.text, "lxml")

            products_html = soup.find_all("li", class_="product")

            products = []

            for item in products_html:

                title = None
                price = None
                image = None

                title_tag = item.find("h2")

                if title_tag:
                    title = title_tag.text.strip()

                price_tag = item.find("span", class_="price")

                if price_tag:
                    price = price_tag.text.strip()

                image_tag = item.find("img")

                if image_tag:
                    image = image_tag.get("src")

                product_data = {
                    "platform": "WooCommerce",
                    "title": title,
                    "price": price,
                    "image": image
                }

                products.append(product_data)

            return products

        except Exception as e:
            print(f"Erreur WooCommerce Agent : {e}")
            return []