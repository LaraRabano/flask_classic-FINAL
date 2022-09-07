import requests

apikey = "E1608E4F-F1D1-4449-B8A4-513461E57ECD"
headers = {"X-CoinAPI-Key": apikey}

moneda_origen = input("¿Qué moneda quieres cambiar?")
moneda_destino = input("¿Qué moneda quieres obtener?")

url = f"http://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}"


respuesta = requests.get(url, headers=headers)
codigo = respuesta.status_code
tipo_cambio = respuesta.json()

if codigo == 200:
    print(
        f"Un {tipo_cambio['asset_id_base']} es {tipo_cambio['rate']} {tipo_cambio['asset_id_quote']}")
