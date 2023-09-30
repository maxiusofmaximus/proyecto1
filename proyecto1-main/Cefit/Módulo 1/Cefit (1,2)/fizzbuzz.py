"""
lista de números del 1 al 100, pero cuando un número es divisible por 3,
imprimirá "Fizz" en su lugar, cuando es divisible por 5 imprimirá "Buzz", y
cuando es divisible por ambos (es decir, 15), imprimirá "FizzBuzz".
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz:", i)
    elif i % 3 == 0:
        print("Fizz:", i)
    elif i % 5 == 0:
        print("Buzz:", i)