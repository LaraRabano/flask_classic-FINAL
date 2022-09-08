from .models import CriptoModel
from .view import CriptoView


class CriptoController:

    def __init__(self):
        self.modelo = CriptoModel()
        self.vista = CriptoView()
        pass

    def consultar(self):
        seguir = "S"
        while seguir == "S":

            desde, hasta = self.vista.pedir_monedas()
            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            cambio = float(self.modelo.consultar_cambio())
            self.vista.mostrar_cambio(desde, cambio, hasta)
            seguir = self.vista.quieres_seguir()
            
            while seguir not in ("S", "N"):
                seguir = self.vista.quieres_seguir()
