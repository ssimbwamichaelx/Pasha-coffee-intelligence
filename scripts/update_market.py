import json
import urllib.request
from datetime import datetime, timezone

url = "https://api.frankfurter.dev/v2/rate/usd/ugx"

with urllib.request.urlopen(url, timeout=20) as response:
    exchange = json.load(response)

data = {
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "usd_ugx": exchange["rate"],
    "currency_source": "Frankfurter API"
}

with open("data/market.json", "w") as f:
    json.dump(data, f, indent=2)

print("USD/UGX updated:", exchange["rate"])
