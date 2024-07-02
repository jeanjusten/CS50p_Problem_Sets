import json
import sys
import requests

if len(sys.argv) <=1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) ==2:
    sys_replace = sys.argv[1].replace(".","")

    if sys_replace.isnumeric():
        bitcoin = float(sys.argv[1])

# Queries the API for the CoinDesk Bitcoin Price Index
        try:
            bitcoin_request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# Storing the requested data in json format inside a variable
            btc_info = bitcoin_request.json()
# Extracting the btc 'Rate' out of its lists
            btc_price = btc_info["bpi"]["USD"]["rate"]
# Transforming the string extracted into a float
            btc_price = float(btc_price.replace(",",""))
# Multiplying the number of btc the user inputed on sys.argv by the current bitcoin rate in USD
            total = bitcoin * btc_price
            print(f"${total:,.4f}")
        except requests.RequestException:
            pass
    else:
        sys.exit("Command-line argument is not a number")