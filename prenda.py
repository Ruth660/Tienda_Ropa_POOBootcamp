# prenda.py
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def mostrar_info(self):
        return f"Prenda: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}"
