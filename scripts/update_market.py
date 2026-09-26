import json
import urllib.request
from datetime import datetime, timezone

url = "https://allratestoday.com/api/open/central-bank/bou?source=USD&target=UGX"

with urllib.request.urlopen(url, timeout=20) as response:
    raw = response.read().decode()
    print("API response:", raw)
    exchange = json.loads(raw)

rate = exchange.get("rate")

if rate is None:
    raise ValueError("USD/UGX rate was not found")

try:
    with open("data/market.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

if "fx" not in data:
    data["fx"] = {}

data["fx"]["usd_ugx"] = rate
data["fx"]["source"] = "Bank of Uganda"
data["fx"]["updated"] = datetime.now(timezone.utc).isoformat()

data["status"] = "live_data"

with open("data/market.json", "w") as f:
    json.dump(data, f, indent=2)

print("USD/UGX updated:", rate)
