""" 
    Pida al usuario adivinar un número secreto. El programa debe usar un bucle while para permitir al usuario adivinar hasta que lo haga correctamente
"""
import random
top = 10
number_secret = random.randint(0,top)
count = 3
while count > 0:
    print(f'Tienes {count} intentos para adivinar el número secreto')
    numero = int(input(f"Adivine el número (Entre el 0 - {top}): "))
    if numero != number_secret and numero > number_secret:
        print("El número es demasiado alto")
    elif numero != number_secret and numero < number_secret:
        print("El número es demasiado bajo")
    else:
        print("Felicitaciones el número es el correcto, lo adivinaste, eres mágico, el número es el:", number_secret)
        break
    count -= 1
    if count == 0:
        print("Game over, no lifes")