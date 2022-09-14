import requests
from . import APIKEY


class APIError(Exception):
    pass


class CriptoModel:

    def __init__(self,):
        self.moneda_origen = ""
        self.moneda_destino = ""
        self.cambio = 0.0
        pass
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


# Esto consulta el archivo csv con el que ya no trabajamos.
class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                mov = Movimiento(linea)
                self.movimientos.append(mov)

    def agregar(self, movimiento):
        self.movimientos.append(movimiento)
        self.guardar_archivo()

    def guardar_archivo(self):
        nombres = list(self.movimientos[0].__dict__.keys())
        for nombre in nombres:
            if nombre in CLAVES_IGNORADAS:
                nombres.remove(nombre)

        with open(FICHERO, "w") as fichero:
            writer = csv.DictWriter(fichero, nombres)
            writer.writeheader()
            for mov in self.movimientos:
                dic_mov = mov.__dict__
                for nombre in CLAVES_IGNORADAS:
                    dic_mov.pop(nombre)
                writer.writerow(dic_mov)

    def __str__(self):
        return f"Lista de {len(self.movimientos)} movimientos"

    def __repr__(self) -> str:
        return self.__str__()
