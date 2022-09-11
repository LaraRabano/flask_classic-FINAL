from flask import render_template  # Esto es para que Flask lea html

from criptocambio import app
from criptocambio.modelo import ListaMovimientos  # Esto es la aplicación Flask
from criptocambio.modelo import * 


class CriptoVista():

    def pedir_monedas(self):
        moneda_origen = input("¿Qué moneda quieres cambiar?")
        moneda_destino = input("¿Qué moneda quieres obtener?")
        return(moneda_origen, moneda_destino)

    def mostrar_cambio(self, moneda_origen, cambio, moneda_destino):
        print("Un {} equivale a {:,.2f} {}".format(
            moneda_origen, cambio, moneda_destino))

    def quieres_seguir(self):
        seguir = input("¿Quieres cambiar algo más? (S/N)")
        return seguir.upper()


@app.route('/')
def home():
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    # Esto hace que se vea lo que hay en el html.
    return render_template("inicio.html", movs=movimientos.lista_movimientos)


@app.route('/Consultar cambio')
def tipo_cambio():
    cambio = consultar_cambio()  #Intento llamar a la función de consultar cambio del modelo para que se pinte en la vista. 
    


@app.route('/nuevo')
def nuevo():
    return "Nuevo movimiento"


@app.route('/modificar')
def actualizar():
    return "Actualizar movimientos"


@app.route('/borrar')
def borrar():
    return "Borrar movimiento"
