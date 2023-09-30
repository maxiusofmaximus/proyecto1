estudiante = [float(input("Ingrese las notas del estudiante: ")) for x in range(4)]
promedio = sum(estudiante)/len(estudiante)
valorMatricula = float(input(f"\nIngrese el valor de la matrícula: "))
if(promedio >= 4):
    print(f"El promedio es de: {promedio} y es Excelente")
    print(f"Has sido beneficiado con un descuento del 20%, ahora la matrícula es de: {valorMatricula * 0.80}")
elif(promedio >= 3 and promedio < 4):
    print(f"El promedio es de: {promedio} y es Bueno")
    print(f"No has sido beneficiado con un descuento, la matrícula es de: {valorMatricula}")
elif(promedio < 3):
    print(f"El promedio es de: {promedio} y es Deficiente")
    print(f"No has sido beneficiado con un descuento, la matrícula es de: {valorMatricula}")
else:
    print(f"El promedio es de: {promedio} y es Inválido")