import json
from datetime import datetime

def log_action(action, data):
    log_entry = {
        "time": str(datetime.now()),
        "action": action,
        "data": str(data)
    }

    with open("mcp/logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")