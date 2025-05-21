import os
import json

USAGE_FILE = os.path.expanduser("~/.portfolio_roast_usage.json")
MAX_USES = 5

def load_usage():
    if not os.path.exists(USAGE_FILE):
        return 0
    try:
        with open(USAGE_FILE, "r") as f:
            data = json.load(f)
        return data.get("roast_count", 0)
    except:
        return 0

def save_usage(count):
    with open(USAGE_FILE, "w") as f:
        json.dump({"roast_count": count}, f)

def increment_and_check_limit():
    count = load_usage()
    if count >= MAX_USES:
        return False, count
    count += 1
    save_usage(count)
    return True, count
