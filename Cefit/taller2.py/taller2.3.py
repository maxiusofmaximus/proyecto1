# 3. Buscar un elemento dentro de una lista que nosotros le pedimos por teclado.
#  Indicar la posición donde se encuentra. Si hay más de uno, indicar igualmente la posición.
lista = ["Leche", "Arroz", "Tomates", "Carne", "Lechuga", "Yuca", "Sal", "Pimienta"]
for i in range(len(lista)):
    print(i+1, lista[i])
posicion = int(input("Ingrese la posición del elemento deseado: ")) -1
print("La posición de la lista deseada es:", lista[posicion])