# Costo de 10 productos
productos = [int(input("Ingrese el valor del producto: ")) for i in range(10)]

#Aquí se calcula el producto sin IVA
print(f"El valor de los productos sin IVA es de: {sum(productos)}")

#Aquí se calcula el producto con IVA
print(f"El valor de los productos con IVA es de: {(sum(productos)) * 1.19}")