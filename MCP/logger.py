import json
import os
from datetime import datetime

def log_action(action, data):
    MCP_DIR = os.path.dirname(__file__)
    log_path = os.path.join(MCP_DIR, "logs.json")

    log_entry = {
        "time": str(datetime.now()),
        "action": action,
        "data": str(data)
    }

    with open(log_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")