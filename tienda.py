# tienda.py
from camisa import Camisa
from pantalon import Pantalon
from zapato import Zapato
from carrito import Carrito

class Tienda:
    def __init__(self):
        self._inventario = [
            Camisa("Camisa Casual", 30.0, "M"),
            Pantalon("Jeans", 50.0, "L"),
            Zapato("Zapatos Deportivos", 70.0, "42")
        ]
        self._carrito = Carrito()

    def mostrar_inventario(self):
        print("\nInventario de la tienda:")
        for i, producto in enumerate(self._inventario, 1):
            print(f"{i}. {producto.mostrar_info()}")

    def seleccionar_producto(self, opcion):
        if 1 <= opcion <= len(self._inventario):
            producto = self._inventario[opcion - 1]
            self._carrito.agregar_producto(producto)
        else:
            print("Opción no válida.")

    def finalizar_compra(self):
        self._carrito.mostrar_carrito()
        total = self._carrito.calcular_total()
        print(f"\nTotal a pagar: ${total}")
