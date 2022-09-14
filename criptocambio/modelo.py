import sqlite3
import requests
import csv
from unittest import result
from . import APIKEY
from . import FICHERO

# consultar clases del 11 y 12 de julio directamente para crear mi formulario.
# clase de ayer con Axel para ver cómo se agrupan los datos de la DB. 

class APIError(Exception):
    pass


class DataBase:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultaSQL(self, consulta):
        # 1. conectar con la base de datos
        conexion = sqlite3.connect(self.ruta)

        # 2. abrir un cursor
        cursor = conexion.cursor()

        # 3. ejecutar consulta SQL
        cursor.execute(consulta)

        # 4. tratar los datos
        #   4.1 obtengo los nombres de columna
        #       ( ('nom_col', ...), (), ()... )
        #   4.2 pido todos los datos (registros)
        #   4.3 recorrer los resultados:
        #       4.3.1 crear un diccionario
        #             - recorro la lista de los nombres de columna
        #             - para cada columna: nombre + valor
        #       4.3.1 guardar en la lista de movimientos
        # [  {'nom_col1': 'val_col1, ...}  ]

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])
        # nombres_columnas = ['nom_col1', 'nom_col2'....]
        # nombres_columnas = ['id', 'fecha', 'concepto', 'tipo', 'cantidad']

        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos


class CriptoModelo:  # Esto es lo que quiero hacer (vacío de contenido)

    def __init__(self,):
        self.moneda_origen = ""
        self.cantidad_moneda_origen = ""
        self.moneda_destino = ""
        self.cantidad_moneda_destino = ""
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

    # Esto tiene que llamar a una base de datos
    def consultar_inversiones(self):
        pass

    def consultar_cambio(self):  # Esto es la consulta a la API con tipo de cambio

        headers = {"X-CoinAPI-Key": APIKEY}
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=headers)
        codigo = respuesta.status_code

        if codigo == 200:
            self.cambio = respuesta.json()['rate']
            # la respuesta de la consulta (debería ir a la vista)
            return self.cambio

        else:
            raise APIError("Ha ocurrido un error {}{} al consultar la API".format(
                codigo, respuesta.reason))

        pass


# Esto es la consulta a la SQL (no se como integrar esta mierda)
