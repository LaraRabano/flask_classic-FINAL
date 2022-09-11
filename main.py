from criptocambio import app 

from criptocambio.vista import *
from criptocambio.modelo import *

class CriptoController:

    def __init__(self):
        self.modelo = CriptoModelo()
        self.vista = CriptoVista()
        pass