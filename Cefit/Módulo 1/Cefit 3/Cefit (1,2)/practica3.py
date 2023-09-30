def my_counter():
    count = 0
    while count < 101:
        count += 1
        print(count)

def my_infinityCounter():
    write = 1
    count = 0
    suma = 0
    while write != 0:
        count += 1
        write = int(input(f'Ingrese el número {count}: '))
        suma += write
    print(f'La suma de todos los números es {suma}')

def my_counter30():
    count = 0
    while count < 30:
        print(count)
        count += 1

summit = int(input('Ingrese al ejercicio que quiere ingresar ( 1 - 3 ) '))
if(summit == 1):
    my_counter()
if(summit == 2):
    my_infinityCounter()
if(summit == 3):
    my_counter30()
else:
    print('Error, ese ejercicio no está')