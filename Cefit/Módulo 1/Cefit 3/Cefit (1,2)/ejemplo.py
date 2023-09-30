import math
# Población en un salón de clase
mujeres = int(input("Colocar el censo de mujeres: "))
hombres = int(input("Colocar el censo de hombres: "))
def porcentaje(x):
    return math.ceil((x / (hombres + mujeres)) * 100)
print(f"El porcentaje de mujeres es de: {porcentaje(mujeres)}%")
print(f"El porcentaje de hombres es de: {porcentaje(hombres)}%")