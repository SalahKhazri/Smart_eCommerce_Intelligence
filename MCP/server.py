from MCP.client import MCPClient

class MCPServer:

    def __init__(self):
        self.client = MCPClient()

    def analyze(self, df):

        top = self.client.run_topk(df)

        results = []

        for _, row in top.iterrows():
            insight = self.client.run_llm_analysis(row)
            results.append((row["title"], insight))

        return results