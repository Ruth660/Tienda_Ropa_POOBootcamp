
# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def mostrar_info(self):
        pass


# Clase derivada Ropa
class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def get_talla(self):
        return self._talla

    def mostrar_info(self):
        print(f"{self.get_nombre()} - Talla: {self._talla} - Precio: ${self.get_precio()}")


# Clase Camisa
class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo):
        super().__init__(nombre, precio, talla)
        self._tipo = tipo

    def mostrar_info(self):
        print(f"Camisa: {self.get_nombre()} - Tipo: {self._tipo} - Talla: {self.get_talla()} - Precio: ${self.get_precio()}")


# Clase Pantalon
class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, estilo):
        super().__init__(nombre, precio, talla)
        self._estilo = estilo

    def mostrar_info(self):
        print(f"Pantalón: {self.get_nombre()} - Estilo: {self._estilo} - Talla: {self.get_talla()} - Precio: ${self.get_precio()}")


# Clase Zapato
class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, material):
        super().__init__(nombre, precio, talla)
        self._material = material

    def mostrar_info(self):
        print(f"Zapato: {self.get_nombre()} - Material: {self._material} - Talla: {self.get_talla()} - Precio: ${self.get_precio()}")
