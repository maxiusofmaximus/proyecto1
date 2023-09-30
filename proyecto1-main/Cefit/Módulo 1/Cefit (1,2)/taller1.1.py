# En este código se ingresa el peso y altura de Pedrito,
# luego se calcula el IMC (Indice de Masa Corporal)
pedritoPeso = float(input("Ingrese el peso de Pedrito: "))
pedritoAltura = float(input("Ingrese estatura de Pedrito: "))
IMC = pedritoPeso / (pedritoAltura * pedritoAltura)
print(f"El indice de masa corporal de pedrito es: {IMC}")

# Este trozo de código me indica su rango de IMC (Indice de Masa Corporal)
if(IMC < 18.5):
    print("El IMC de Pedrito está en un rango de bajo peso")
if(IMC > 18.5 and IMC < 24.9):
    print("El IMC de Pedrito está en un rango de peso normal")
if(IMC > 24.9 and IMC < 29.9):
    print("El IMC de Pedrito está en un rango de sobrepeso")
if(IMC > 29.9 and IMC < 34.9):
    print("El IMC de Pedrito está en un rango de obesidad grado 1")
if(IMC > 34.9 and IMC < 39.9):
    print("El IMC de Pedrito está en un rango de obesidad grado 2")
if(IMC > 39.9):
    print("El IMC de Pedrito está en un rango de obesidad grado 3 (Obesidad mórbida)")