import json
from MCP.tools import get_top_products, explain_product
from MCP.logger import log_action

class MCPClient:

    def __init__(self, permissions_path="MCP/permissions.json"):
        self.permissions = json.load(open(permissions_path))

    def run_topk(self, df):

        if not self.permissions["data_access"]:
            raise Exception("Access denied to data")

        log_action("TOPK_REQUEST", "user requested top products")

        return get_top_products(df)

    def run_llm_analysis(self, product):

        if not self.permissions["llm_access"]:
            raise Exception("LLM access denied")

        log_action("LLM_REQUEST", product["title"])

        return explain_product(product)