num = int(input("Ingrese un número entre 1 y 3: "))
numText = ""
if(num == 1):
    numText = "uno"
elif(num == 2):
    numText = "dos"
elif(num == 3):
    numText = "tres"
else:
    numText = "No es un número entre 1 y 3"
print(numText)