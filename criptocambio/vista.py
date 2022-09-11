from criptocambio import app #Esto es Flask
from modelo import CriptoModel

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
    return "Página de inicio"

    


@app.route('/nuevo')
def nuevo():
    return "Nuevo movimiento"


@app.route('/modificar')
def actualizar():
    return "Actualizar movimientos"


@app.route('/borrar')
def borrar():
    return "Borrar movimiento"
