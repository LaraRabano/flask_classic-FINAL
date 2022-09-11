import requests
import csv
from . import APIKEY


class APIError(Exception):
    pass


class CriptoModelo:

    def __init__(self,):
        self.moneda_origen = ""
        self.moneda_destino = ""
        self.cambio = 0.0
        self.inversion_euros = ""
        self.valor_euros = ""
        pass
    pass

    def invertir_euros(self):
        pass

    def invertir_criptomonedas(self):
        pass

    def vender(self):
        pass

    def consultar_inversiones(self): #Esto tiene que llamar a una base de datos
        pass





    def consultar_cambio(self):

        headers = {"X-CoinAPI-Key": APIKEY}
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=headers)
        codigo = respuesta.status_code

        if codigo == 200:
            self.cambio = respuesta.json()['rate']
            return self.cambio

        else:
            raise APIError("Ha ocurrido un error {}{} al consultar la API".format(
                codigo, respuesta.reason))

        pass
