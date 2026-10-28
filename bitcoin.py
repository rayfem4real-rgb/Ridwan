import sys
import requests

API_KEY = "8356c0e3c21593af3e17dbefe592f10e59f1090ff0230ceb09bfe3e180ed2614"

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
    )
    response.raise_for_status()
except requests.RequestException:
    sys.exit("Could not reach CoinCap")

price = float(response.json()["data"]["priceUsd"])
print(f"${price * amount:,.4f}")
