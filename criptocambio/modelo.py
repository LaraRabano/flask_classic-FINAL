import requests
import csv
from . import APIKEY
from . import FICHERO


class APIError(Exception):
    pass


class CriptoModelo:  #Esto es lo que quiero hacer (vacío de contenido)

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



    def consultar_cambio(self): #Esto es la consulta a la API con tipo de cambio

        headers = {"X-CoinAPI-Key": APIKEY}
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=headers)
        codigo = respuesta.status_code

        if codigo == 200:
            self.cambio = respuesta.json()['rate']
            return self.cambio    #la respuesta de la consulta (debería ir a la vista)

        else:
            raise APIError("Ha ocurrido un error {}{} al consultar la API".format(
                codigo, respuesta.reason))

        pass


class ListaMovimientos:  #Esto es la consulta a la SQL (no se como integrar esta mierda)
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
