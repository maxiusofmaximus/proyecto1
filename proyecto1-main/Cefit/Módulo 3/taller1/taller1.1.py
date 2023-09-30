# Queremos guardar los nombres y las edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se
# introduzca como nombre un asterisco (*).
# Al finalizar se mostrará los siguientes datos: 
# Todos los estudiantes mayores de edad.
# Los alumnos mayores de edad (los que tienen más edad).
class Estudiantes:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando mucho😊")

def main():
    lista_mayores_de_edad = []
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").lower().title()
        edad = int(input("Ingrese la edad del estudiante: "))
        if nombre == "*":
            break
        else:
            estudiante = Estudiantes(nombre, edad)
            if edad >= 18:
                lista_mayores_de_edad.append((estudiante.nombre, estudiante.edad))
    print("Los mayores de edad son: ")
    for i in lista_mayores_de_edad:
        print(*i)
    print(estudiante.estudiar())

if __name__ == "__main__":
    main()
    print("El programa ha finalizado")
    global nombre