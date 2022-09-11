import requests

apikey = "E1608E4F-F1D1-4449-B8A4-513461E57ECD"
headers = {"X-CoinAPI-Key": apikey}

api_url = "http://rest-sandbox.coinapi.io"
endpoint = "/v1/assets"

url = api_url + endpoint

respuesta = requests.get(url, headers=headers)
codigo = respuesta.status_code

if codigo == 200:
    print("Las monedas dispnibles son:")
    respuesta_json = respuesta.json()

    for moneda in respuesta_json:
        if moneda["asset_id"].startswith("BTC"):
            print(moneda["asset_id"], moneda["name"])


else:
    print(f"La petición a la API ha fallado")
    print(f"Código de error {codigo}")
    print(f"Razón del error:{respuesta.reason}")
    print(respuesta.text)
