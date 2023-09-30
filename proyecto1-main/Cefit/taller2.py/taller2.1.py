# 1. Crear una lista con n números, ingresados por teclado y mostrar sus valores elevados al cuadrado.
n = int(input("Ingrese la longitud de la lista de números: "))
lista = []
for i in range(n):
    n = int(input("Ingrese un número: "))
    print("Has ingresado el", n)
    lista.append(n * n)
print(lista)