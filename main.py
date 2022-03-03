




#Como? Acompanhar a cotação das criptos.

import json
from requests import Session
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout, TooManyRedirects

sua_api_key =                                                                                 "64994445-d3b2-42aa-8660-94cd653cfda6"  

url = """
https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"""

parameters = {
    "start":"1",
    "limit":"400",
    "convert":"USD",
}

headers = {
    "Accepts":"application/json",
    "X-CMC_PRO_API_KEY": sua_api_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data_full = json.loads(response.text)["data"]

    for data in data_full:
        id = data["id"]
        simbolo_da_criptomoeda = data["symbol"]
        preco_da_criptomoeda = data["quote"]["USD"]["price"]

        print("-"*100)
        print(id,":",simbolo_da_criptomoeda, ":","R$",preco_da_criptomoeda)
        print("-"*100)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

