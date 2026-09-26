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
    raise ValueError("USD/UGX rate was not found in API response")

data = {
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "usd_ugx": rate,
    "currency_source": "Bank of Uganda"
}

with open("data/market.json", "w") as f:
    json.dump(data, f, indent=2)

print("USD/UGX updated:", rate)
