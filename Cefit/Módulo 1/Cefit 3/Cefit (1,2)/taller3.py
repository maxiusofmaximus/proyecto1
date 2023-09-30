# Hola mundo
def punto1():
    print("Hola mundo")

# Suma de números
def punto2():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print(a + b)

# Calcular la edad
def punto3():
    anno = int(input("Ingrese su año de nacimiento: "))
    actually = int(input("Ingrese el año actual: "))
    print("Su edad es: " + actually - anno)

# Calcular el IMC
def punto4():
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))
    imc = peso / (altura ** 2)
    print("Su IMC es: " + imc)

# Hallar el número par e impar
def punto5():
    numero = int(input("Ingrese el número"))
    if(numero % 2 == 0):
        print("Su número es par")
    elif(numero % 2 == 1):
        print("Su número es impar")
    else:
        print("Su número es cero o algo raro")

# Hallar el área del cuadrado
def punto6():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print("Su área es: " + area)

# Hallar el área del triángulo
def punto7():
    lado1 = float(input("Ingrese el lado 1 del triángulo: "))
    lado2 = float(input("Ingrese el lado 2 del triángulo: "))
    lado3 = float(input("Ingrese el lado 3 del triángulo: "))
    if(lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2):
        area = (lado1 + lado2 + lado3) / 2
        print("Su área es: " + area)