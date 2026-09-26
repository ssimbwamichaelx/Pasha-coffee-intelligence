import json
import urllib.request
from datetime import datetime, timezone

url = "https://allratestoday.com/api/open/central-bank/bou?source=USD&target=UGX"

with urllib.request.urlopen(url, timeout=20) as response:
    exchange = json.load(response)
        print(response.read().decode())

data = {
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "usd_ugx": exchange["rate"],
    "currency_source": "Bank of Uganda"
}

with open("data/market.json", "w") as f:
    json.dump(data, f, indent=2)

print("USD/UGX updated:", exchange["rate"])
