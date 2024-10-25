# Tienda_Ropa_POOBootcamp

Este proyecto es un sistema de compra de ropas utilizando Programación Orientada a Objetos (POO) en Python. Permite al usuario seleccionar entre diferentes ítems de ropa y realizar una compra.

## Estructura del Proyecto

- `producto.py`: Clase base `Producto` que representa un producto general.
- `ropa.py`: Clase `Ropa` que hereda de `Producto` y añade atributos de la ropa.
- `camisa.py`, `pantalon.py`, `zapato.py`: Clases específicas de ropa.
- `carrito.py`: Clase para gestionar el carrito de compras.
- `tienda.py`: Clase que maneja el inventario de productos y el proceso de compra.
- `main.py`: Archivo principal para la interacción con el usuario.

## Cómo Ejecutar

1. Clona el repositorio.
2. Navega a la carpeta del proyecto.
3. Ejecuta el siguiente comando:


## Requisitos

- Python 3.10 o superior.

## Conceptos de POO

- **Encapsulamiento**: Atributos privados y métodos `get` y `set` para acceder a ellos.
- **Herencia**: `Ropa` hereda de `Producto`, y `Camisa`, `Pantalon` y `Zapato` heredan de `Ropa`.
- **Polimorfismo**: Método `mostrar_info` sobrescrito en cada clase de ropa.
- **Abstracción**: Simplificación de la interacción del usuario con la tienda y el carrito.


