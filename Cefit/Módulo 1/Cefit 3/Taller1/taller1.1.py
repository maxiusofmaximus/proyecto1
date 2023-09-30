palabra = input("Ingrese la palabra de su parecer: ")
count = {"a": 0,"e": 0,"i": 0,"o": 0,"u": 0}
for i in palabra:
    if i in "a":
        count["a"[0]] += 1
    if i in "e":
        count["e"[0]] += 1
    if i in "i":
        count["i"[0]] += 1
    if i in "o":
        count["o"[0]] += 1
    if i in "u":
        count["u"[0]] += 1
def sum(count):
    return count["a"[0]] + count["e"[0]] + count["i"[0]] + count["o"[0]] + count["u"[0]]
print(f"La cantidad de vocales en la palabra es de: {sum(count)}\nY la cantidad de vocales de cada tipo es de: {count}")