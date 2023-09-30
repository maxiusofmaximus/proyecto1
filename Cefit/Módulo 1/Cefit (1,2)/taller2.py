# ¿Cuál es el resultado de cada una de las siguientes operaciones?
def punto1():
    a = (5 + 5) * 5
    b = 5 + (5 * 5)
    c = 5 % 2
    d = (5 - (6 - 2)) * 2
    print(a, b, c, d)

# Si a=7 y b=3, ¿Cuál es el resultado de cada una de las siguientes comparaciones?
def punto2():
    a = 7
    b = 3
    print(a != b)
    print(a == b)
    print(a > b)
    print((a + b) < 2)
    print((a > 7) and (b == 3))
    print((a < 7) or (b == 3))
    print((a < 7) or (b != 3))

# Realizar prueba de escritorio e indique qué resultados generan los siguientes algoritmos:
# Asumiendo: Caso 1: a=3, b=2, c=1 _|_ Caso 2: a=1, b=3, c=2 _|_ Caso 3: a=1, b=2, c=3
def punto3():
    # Caso 1: a = 3, b = 2, c = 1.
    # Caso 2: a = 1, b = 3, c = 2.
    # Caso 3: a = 1, b = 2, c = 3.
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    c = int(input("Ingrese el valor de c: "))
    if (a > b and a > c):
        print("a es mayor que b y c")
    elif (a < b and a < c and b > c):
        print("a es menor que b y c, y b es mayor que c")
    elif (a < b and a < c and b < c):
        print("a es mayor que b y menor que c, y b es menor que c")

#  En un curso de “fundamentos de algoritmos”, se tienen las siguientes notas (Cada 
#  una de ellas entre 1 y 5) con sus respectivos porcentajes:
def punto4():
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

# Realizar un algoritmo que permita convertir metros a millas.
def punto5():
    metros = float(input("Ingrese el valor de metros: "))
    millas = metros * 1000
    print(f"metros son: {metros}, y en millas son: {millas} ")

# El gobierno nacional ha decretado un incremento del 4,2% para el salario mínimo del 
# próximo año. Elabore un algoritmo que muestre el nuevo salario mínimo para el siguiente 
# año.
def punto6():
    salario = float(input("Ingrese el salario mínimo: "))
    incremento = salario * 0.042
    nuevoSalario = salario + incremento
    print(f"El nuevo salario mínimo es: {nuevoSalario}")

# Realizar un algoritmo que permita convertir pesos colombianos a dólares.
def punto7():
    pesos = float(input("Ingrese el valor de pesos colombianos: "))
    dolares = pesos / 4119.60
    print(f"En pesos colombianos son: {pesos}, y en dólares son: {dolares}")