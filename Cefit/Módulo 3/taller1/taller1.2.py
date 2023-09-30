# Hacer un programa que inicialice una lista de números
# con valores aleatorios, y posterior ordene los
# elementos de menor a mayor
import random
lista = random.sample(range(1,76), 10)
lista.sort()
print(lista)