# camisa.py
from ropa import Ropa

class Camisa(Ropa):
    def mostrar_info(self):
        return f"Camisa: {super().mostrar_info()}"

# pantalon.py
from ropa import Ropa

class Pantalon(Ropa):
    def mostrar_info(self):
        return f"Pantalon: {super().mostrar_info()}"

# zapato.py
from ropa import Ropa

class Zapato(Ropa):
    def mostrar_info(self):
        return f"Zapato: {super().mostrar_info()}"
