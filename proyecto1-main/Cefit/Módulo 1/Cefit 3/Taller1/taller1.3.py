longitud = int(input("Ingrese la cantidad de palabras para la lista: "))
palabra = [input("Ingrese una lista de palabras: ") for i in range(longitud)]
letra = input("Ingrese la letra con la que debe de comenzar la lista de palabras: ")
def ordenar(x):
    return x[0] == letra
print(palabra.sort(key = ordenar))