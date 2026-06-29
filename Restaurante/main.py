# Archivo principal del programa

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurantee import Restaurante


# Creacion del restaurante
restaurante = Restaurante()


# Crear productos
producto1 = Producto("Cuy Asado", "Plato Principal", 9.50, True)
producto2 = Producto("Jugo Natural", "Bebida", 2.75, True)


# Crear clientes
cliente1 = Cliente("Hugo Lombardi", 22, "0987654321", True)
cliente2 = Cliente("Armando Mendoza", 30, "0991234567", False)


# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)


# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()