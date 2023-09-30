# Compra de artículos, Si los artículos comprados son menores a 3 Pagar en efectivo, caso 
# contrario pagar con tarjeta.
def punto1():
    articulos = int(input("Ingrese la cantidad de artículos: "))
    if articulos < 3:
        print("Pagar en efectivo")
    else:
        print("Pagar con tarjeta")

# Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las 
# variables num1, num2, num3 respectivamente. El algoritmo debe imprimir cual es el 
# mayor. Recuerde constatar que los tres valores introducidos por el teclado sean valores 
# distintos.
def punto2():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    if num1 > num2 and num1 > num3:
        print("el numero 1 es el mayor es de todos:")
    elif num2 > num1 and num2 > num3:
        print("el numero 2 es el mayor es de todos:")
    elif num3 > num1 and num3 > num2:
        print("el numero 3 es el mayor es de todos:")

# Ingresar por teclado 3 números enteros y mostrar el menor de los 3 números ingresados 
# y la suma de dichos números

def punto3():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    if num1 < num2 and num1 < num3:
        print("el numero 1 es el menor es de todos:")
        print(num1)
        print(num2)
        print(num3)
        print(num1 + num2 + num3)
        
#A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. si la 
#cantidad de horas trabajadas es mayor a 40 horas. la tarifa se incrementa en un 50% para 
#las horas extras. calcular el salario del trabajador dadas las horas trabajadas y la tarifa.
def punto4():
    salario = 1250000
    horas = int(input("Ingrese la cantidad de horas trabajadas: "))
    if horas > 40:
        tarifa = (salario/30/8) * (horas - 40) * 1.5
        print("El salario del trabajador es de: ", tarifa + salario)

#Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran 
#tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son
#menos de tres camisas un descuento del 10%

def punto5():
    camisas = int(input("Ingrese la cantidad de camisas: "))
    total = int(input("ingrese el valor de las camisas: "))
    if camisas >= 3:
        descuento = (total*camisas) * 0.80
        print("El total a pagar es de: ", descuento)
    if camisas < 3:
        descuento = (total*camisas) * 0.90
        print("El total a pagar es de: ",descuento)

#A un trabajador le descuentan de su sueldo el 10%, si su sueldo es menor o igual a 1000. 
#por encima de 1000 y hasta 2000 el 5% del adicional, y por encima de 2000 el 3% del 
#adicional. calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo.

def punto6():
    sueldo = float(input("Ingrese su sueldo: "))
    if sueldo <= 1000:
        descuento = sueldo * 0.1
        print("El descuento es de: ", descuento)
        sueldo = sueldo - descuento
        print("El sueldo neto es de: ", sueldo)
    elif sueldo > 2000:
        descuento = sueldo * 0.05
        print("El descuento es de: ", descuento)
        sueldo = sueldo + descuento
        print("El sueldo neto es de: ", sueldo)
    elif sueldo >= 1000 and sueldo <= 2000:
        descuento = sueldo * 0.03
        print("El descuento es de: ", descuento)
        sueldo = sueldo + descuento
        print("El sueldo neto es de: ", sueldo)