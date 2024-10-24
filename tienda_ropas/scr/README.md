# Tienda de Ropa POO Bootcamp

Este proyecto es una simulación de una tienda de ropa utilizando Programación Orientada a Objetos (POO) en Python. Permite a los usuarios comprar diferentes ítems de ropa, como camisas, pantalones y zapatos, y ver un resumen de su compra.

## Estructura del proyecto
- `src/`: Carpeta que contiene el código fuente del proyecto.
  - `productos.py`: Clases que representan los productos (Producto, Ropa, Camisa, Pantalon, Zapato).
  - `carrito.py`: Clase `Carrito` que almacena los productos seleccionados.
  - `tienda.py`: Clase `Tienda` que gestiona la lógica de compra y el carrito.
  - `main.py`: Punto de entrada del programa.

## Requisitos
- Python 3.7 o superior

## Instrucciones para ejecutar
1. Clona este repositorio:
2. Navega a la carpeta del proyecto:
3. Ejecuta el programa:

## Pilares de POO utilizados
- **Encapsulamiento**: Los atributos de las clases están encapsulados usando `_`.
- **Herencia**: `Ropa` hereda de `Producto`, y `Camisa`, `Pantalon`, y `Zapato` heredan de `Ropa`.
- **Polimorfismo**: Método `mostrar_info` sobrescrito en las clases derivadas para mostrar la información específica de cada producto.
- **Abstracción**: La interacción con el usuario se simplifica a través del menú y el proceso de compra, ocultando detalles internos.
