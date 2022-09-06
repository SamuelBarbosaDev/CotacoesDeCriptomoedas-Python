




#Como? Acompanhar a cotação das criptos.

from email.policy import default
import json
from requests import Session
from decouple import config
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout, TooManyRedirects


sua_api_key = config('sua_chave', default=None)
print(sua_api_key)
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

