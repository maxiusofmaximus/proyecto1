def ejercicio6():
    numero = int(input("Número entre 0, -1~, 1~: "))
    if(numero == 0):
        print("Es 0")
    elif(numero >= 1):
        print("Es positivo")
    elif(numero <= -1):
        print("Es negativo")
    else:
        print("No es un número")

def ejercicio7():
    gradosC = int(input("Ingrese los grados Celcius: "))
    gradosF = gradosC * 1.8 + 32
    print(f"Los grados Celcius son {gradosC}, y en grados Fahrenheit {gradosF}")
    
ingresoDeDatos = int(input("A qué ejercicio quiere ingresar (6 - 7) "))
if(ingresoDeDatos == 6):
    ejercicio6()
if(ingresoDeDatos == 7):
    ejercicio7()
