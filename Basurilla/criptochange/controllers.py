from tkinter import *
from .models import *
from .view import *


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



class CriptoControllerTk(Tk):
    def __init__(self):
        super().__init__()
        self.vista = CriptoViewTk(self, self.calcular_cambio)
        self.modelo = CriptoModel()

    def run(self):
        self.mainloop()

    def calcular_cambio(self):
        """
        Recoge los datos de la vista
        los pasa al modelo
        pide el cambio al modelo
        le pasa el resultado del cambio a la vista
        """
        self.modelo.moneda_origen = self.vista.moneda_origen()
        self.modelo.moneda_destino = self.vista.moneda_destino()
        self.modelo.consultar_cambio()

        self.vista.mostrar_cambio(self.modelo.cambio)