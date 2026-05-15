class BaseAgent:

    def __init__(self, site_name):
        self.site_name = site_name

    def fetch_products(self):
        raise NotImplementedError(
            "La méthode fetch_products doit être implémentée"
        )