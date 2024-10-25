# main.py
from tienda import Tienda

def main():
    tienda = Tienda()

    while True:
        print("\n1. Mostrar inventario")
        print("2. Agregar producto al carrito")
        print("3. Finalizar compra")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tienda.mostrar_inventario()
        elif opcion == "2":
            tienda.mostrar_inventario()
            try:
                seleccion = int(input("Seleccione el número del producto: "))
                tienda.seleccionar_producto(seleccion)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            tienda.finalizar_compra()
            break
        elif opcion == "4":
            print("Gracias por su visita.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
