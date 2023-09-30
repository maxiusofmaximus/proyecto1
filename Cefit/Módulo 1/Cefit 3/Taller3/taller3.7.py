# 7. Desarrolle un programa que calcule el promedio de edades de hombres
# y mujeres de un grupo de estudiantes.

def main():
    hombres = int(input("Ingrese la cantidad de hombres en el grupo de estudiantes: "))
    mujeres = int(input("Ingrese la cantidad de mujeres en el grupo de estudiantes: "))
    edad_hombres = [int(input("Ingrese las edades de los hombres: ")) for i in range(hombres)]
    edad_mujeres = [int(input("Ingrese las edades de los mujeres: ")) for i in range(mujeres)]
    print("Promedio de edades de hombres: ", sum(edad_hombres) / len(edad_hombres))
    print("Promedio de edades de mujeres: ", sum(edad_mujeres) / len(edad_mujeres))

if __name__ == "__main__":
    main()
    print("Fin del programa")