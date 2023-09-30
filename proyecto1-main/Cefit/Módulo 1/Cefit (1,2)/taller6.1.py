#Aquí se hace el factorial del número que el usuario determine
factorial = int(input("Ingrese el número factorial: "))

#Aquí se hace el factorial al multiplicar el número por cada iteración
for i in range(1, factorial):
    factorial *= i
print(f"El factorial es: {factorial}")