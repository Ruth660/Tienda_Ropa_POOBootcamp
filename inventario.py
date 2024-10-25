# inventario.py
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
        print(f"{prenda.mostrar_info()} ha sido añadida al inventario.")

    def mostrar_inventario(self):
        print("\nInventario de la tienda:")
        for prenda in self.prendas:
            print(prenda.mostrar_info())
