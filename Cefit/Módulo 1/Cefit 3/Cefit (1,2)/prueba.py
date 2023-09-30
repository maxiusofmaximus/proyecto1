import random
palabra = "abcdefghijklmnñopqrstuvwxyz"
password = ""
random_0 = [random.randint(0, (len(palabra)-1)) for i in range(len(palabra))]
random_1 = random.randint(4, len(palabra))
for i in range(random_1):
    password += palabra[random_0[i]]
print(password)