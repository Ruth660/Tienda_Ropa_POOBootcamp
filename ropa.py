# ropa.py
from producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def mostrar_info(self):
        return f"{self._nombre} (Talla: {self._talla}) - Precio: ${self._precio}"
