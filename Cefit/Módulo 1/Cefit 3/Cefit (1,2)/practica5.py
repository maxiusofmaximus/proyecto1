
# Calcular el descuento en un producto según su precio (10% ó 20%)
def ejercicio5():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento: "))
    descuento = (precio * (descuento / 100))
    print(f"El descuento es de: {descuento} y el precio con descuento es de: {precio - descuento}")

#Determinar si un año es bisiesto o no
def ejercicio3():
    anno = int(input("Ingrese el año: "))
    if((anno % 4) == 0):
        print(f"El año sí es bisiesto")
    else:
        print(f"El año no es bisiesto")
    
ingresoDeDatos = int(input("A qué ejercicio quiere ingresar (5 - 3) "))
if(ingresoDeDatos == 5):
    ejercicio5()
if(ingresoDeDatos == 3):
    ejercicio3()
