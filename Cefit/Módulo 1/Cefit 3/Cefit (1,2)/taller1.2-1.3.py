minutos = int(input("Ingrese los minutos: "))
pais = int(input("Ingrese el país: "+
             "0 => Estados Unidos, "+
             "1 => Canadá, "+
             "2 => Europa, "+
             "3 => Resto del mundo: "))
region = {
    0: 900 * minutos,
    1: 800  * minutos,
    2: 950 * minutos,
    3: 1250 * minutos,
}
if(minutos > 15):
    print(f"El valor de su llamada es: {region[pais] * 0.80}")
else:
    print(f"El valor de su llamada es: {region[pais]}")