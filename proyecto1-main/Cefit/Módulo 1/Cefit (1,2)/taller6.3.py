# Tabla de multiplicar
tabla = int(input("Ingrese la tabla de multiplicar: "))

# Aquí se itera la tabla de multiplicar
for i in range(1, 101):
    print(f"La tabla del {tabla} es: {tabla} X {i} = {tabla * i}")