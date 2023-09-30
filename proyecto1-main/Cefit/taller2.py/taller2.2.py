# 2. Diseñe una lista en el que se ingrese la cantidad de
# productos y sus respectivos precios, para la preparación
# de un plato, también se debe mostrar al final el costo a gastar.
cantidad_de_productos = []
cantidad = int(input("Ingrese la cantidad de productos: "))
valor = sum([int(input("Ingrese el valor de cada uno de los productos: $")) for _ in range(cantidad)])
cantidad_de_productos.append(cantidad)
cantidad_de_productos.append(valor)
print(f"La cantidad de productos es de: {cantidad_de_productos[0]}","\n"
      f"El valor total de los productos es de: {cantidad_de_productos[1]}")