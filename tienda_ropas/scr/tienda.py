# src/tienda.py
from productos import Camisa, Pantalon, Zapato
from carrito import Carrito

class Tienda:
    def __init__(self):
        self._carrito = Carrito()

    def agregar_al_carrito(self, producto):
        self._carrito.agregar_producto(producto)

    def mostrar_resumen(self):
        self._carrito.mostrar_resumen()

    def mostrar_menu(self):
        print("\nBienvenido a la tienda. Seleccione una opción:")
        print("1. Comprar Camisa")
        print("2. Comprar Pantalón")
        print("3. Comprar Zapato")
        print("4. Mostrar Carrito")
        print("5. Salir")
      

