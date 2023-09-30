# 5. Una ONG tiene puntos de reparto de vacunas que se pretende funcionen
# de la siguiente manera. Cada día, empezar con 1000 vacunas disponibles
# y a través de un programa que controla las entregas avisar si el
# inventario baja de 200 unidades. Desarrollar el algoritmo.
day = 1
year = 2023
month = "enero"
bisiesto = False
inventario = 1000
def day_changed():
    global day, month, year, bisiesto, inventario
    if year % 100 == 0:
        pass
    elif year % 4 == 0 and bisiesto % 400 == 0:
        bisiesto = True
    match day, month, year, bisiesto:
        case 31, "enero", 2023, False:
            day = 1
            month = "febrero"
        case 28, "febrero", 2023, False:
            day = 1
            month = "marzo"
        case 31, "marzo", 2023, False:
            day = 1
            month = "abril"
        case 30, "abril", 2023, False:
            day = 1
            month = "mayo"
        case 31, "mayo", 2023, False:
            day = 1
            month = "junio"
        case 30, "junio", 2023, False:
            day = 1
            month = "julio"
        case 31, "julio", 2023, False:
            day = 1
            month = "agosto"
        case 31, "agosto", 2023, False:
            day = 1
            month = "septiembre"
        case 30, "septiembre", 2023, False:
            day = 1
            month = "octubre"
        case 31, "octubre", 2023, False:
            day = 1
            month = "noviembre"
        case 30, "noviembre", 2023, False:
            day = 1
            month = "diciembre"
        case 31, "diciembre", 2023, False:
            day = 1
            month = "enero"
        case 29, "febrero", 2023, True:
            day = 1
            month = "marzo"
        case other:
            day = day + 1
    inventario = 1000
while True:
    reparto = int(input(f"Ingrese las vacunas a entregar en el {day}/{month}/{year}: "))
    inventario -= reparto
    if(inventario <= 200):
        print(f"Alerta, las vacunas se están agotando, número actual {inventario}")
        day_changed()