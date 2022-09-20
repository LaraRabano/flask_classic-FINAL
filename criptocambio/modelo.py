import sqlite3
import requests
from unittest import result
from . import APIKEY
from . import FICHERO


class ConsultaApi:

    def APIError(self):
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



class DataBase:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultaSQL(self, consulta):

        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])

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

    def SumaEurosSQL(self):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        suma = cursor.execute("SELECT SUM(EUR) FROM movimientos")
        conexion.close()
        return suma

    def obtenerMovimientoPorId(self, id):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        consulta = "SELECT * FROM movimientos WHERE id=?"
        cursor.execute(consulta, (id,))

        datos = cursor.fetchone()
        resultado = None

        if datos:
            nombres_columnas = []

            for desc_columna in cursor.description:
                nombres_columnas.append(desc_columna[0])

            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = datos[indice]
                indice += 1
            resultado = movimiento

        conexion.close()
        return resultado

    def consultaConParametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except:
            conexion.rollback()
        conexion.close()
        return resultado


class CriptoModelo:

    def __init__(self,):
        self.moneda_origen = ""
        self.cantidad_moneda_origen = ""
        self.moneda_destino = ""
        self.cantidad_moneda_destino = ""
        self.cambio = 0.0
        self.inversion_euros = ""
        self.valor_euros = ""

    pass

    def invertir_euros(self):
        pass

    def invertir_criptomonedas(self):
        pass

    def vender(self):
        pass
