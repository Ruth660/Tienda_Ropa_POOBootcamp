
class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_resumen(self):
        total = 0
        print("\nResumen de compra:")
        for producto in self._productos:
            producto.mostrar_info()
            total += producto.get_precio()
        print(f"Total a pagar: ${total}")
