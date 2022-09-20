from flask import render_template  # Esto es para que Flask lea html

from criptocambio import app
from criptocambio.modelo import ListaMovimientos  # Esto es la aplicación Flask
from criptocambio.modelo import *


class CriptoVista():

    def pedir_monedas(self):
        moneda_origen = input("¿Qué divisa quieres invertir?")
        cantidad_moneda_origen = input(
            f"¿Cuántos {moneda_origen} quieres invertir?")  # -->int
        moneda_destino = input("¿Qué divisa quieres comprar?")
        cantidad_moneda_destino = input(
            f"¿Cuántos {moneda_destino} quieres comprar?")  # --> int
        return(moneda_origen, cantidad_moneda_origen, moneda_destino, cantidad_moneda_destino)

    def mostrar_cambio(self, moneda_origen, cambio, moneda_destino):
        print("Un {} equivale a {:,.2f} {}".format(
            moneda_origen, cambio, moneda_destino))

    def quieres_seguir(self):
        seguir = input("¿Quieres hacer otra inversión? (S/N)")
        return seguir.upper()

    @app.route('/')
    def home():  # esto llama a mi db y selecciona los movimientos guardados
        db = DataBase()
        movimientos = db.consultaSQL(
            "SELECT * FROM movimientos ORDER BY fecha, id")
        suma = db.SumaEurosSQL()
        # Esto llama al template de inicio y hace que el html pinte los movimientos.
        return render_template("inicio.html", movs=movimientos, suma=suma)

    @app.route('/nuevo')
    def nuevo():
        return "Nuevo movimiento"

    @app.route('/modificar')
    def actualizar():
        return "Actualizar movimientos"

    @app.route('/borrar')
    def borrar():
        return "Borrar movimiento"
