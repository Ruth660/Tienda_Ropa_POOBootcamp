# ropa_hombre.py
from prenda import Prenda

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"Ropa de Hombre: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}, Talla: {self._talla}"
