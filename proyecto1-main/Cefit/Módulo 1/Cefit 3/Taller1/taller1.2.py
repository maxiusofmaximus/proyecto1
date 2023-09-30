posicion = ["primer", "segundo", "tercero", "cuarto", "quinto", "sexto", "séptimo", "octavo", "noveno", "décimo"]
cantidad_nombres = int(input("Ingrese la cantidad de nombres que va a digitar: "))
lista = [input(f"Ingrese el {posicion[i]} nombre: ") for i in range(cantidad_nombres)]
print(sorted([i.lower() for i in lista]))