# src/main.py
from tienda import Tienda
from productos import Camisa, Pantalon, Zapato

def ejecutar_tienda():
    tienda = Tienda()
    tienda.mostrar_menu()

    while True:
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "1":
            tienda.agregar_al_carrito(Camisa("Camisa Azul", 30, "M", "Formal"))
            print("Camisa agregada al carrito.")
        elif opcion == "2":
            tienda.agregar_al_carrito(Pantalon("Pantalón Jeans", 50, "32", "Casual"))
            print("Pantalón agregado al carrito.")
        elif opcion == "3":
            tienda.agregar_al_carrito(Zapato("Zapato Deportivo", 70, "42", "Cuero"))
            print("Zapato agregado al carrito.")
        elif opcion == "4":
            tienda.mostrar_resumen()
        elif opcion == "5":
            print("Gracias por su compra.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        tienda.mostrar_menu()

if __name__ == "__main__":
    ejecutar_tienda()

