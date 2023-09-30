#Estas son las edades de las 10 personas 
#edades = [10, 22, 34, 44, 55, 69, 33, 12, 27, 44]
personas = ["primera", "segunda", "tercera", "cuarta", "quinta", "sexta", "séptima", "octava", "novena", "décima"]
edades = [int(input(f"Ingrese la edad de la {personas[i]} persona: ")) for i in range(10)]

#Aquí se guardan la cantidad de edades según la condición del rango
rango = ["Este es el rango de 0 - 20 ", 0, "Este es el rango de 20 - 30 ", 0, "Este es el rango de 30 - 40 ", 0, "Este es el rango de 40 - 60 ", 0, "Este es el rango de mayores de 60 ", 0]

#Aquí se identifican las edades según el rango
for edad in edades:
    if(edad >= 0 and edad < 20):
        rango[1] += 1
    elif(edad >= 20 and edad < 30):
        rango[3] += 1
    elif(edad >= 30 and edad < 40):
        rango[5] += 1
    elif(edad >= 40 and edad < 60):
        rango[7] += 1
    elif(edad >= 60):
        rango[9] += 1
print(rango)