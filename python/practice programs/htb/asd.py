palabra: str = input("ingrese una palabra: ")

def eval(palabra):
    if palabra[::-1] == palabra:
        return True

    return False

def palix(palabra):
    for i in range(len(palabra)):
        aux = [x for x in palabra]
        aux.pop(i)
        if eval("".join(aux)):
            return "".join(aux)

def palix2(palabra):
    for i, _ in enumerate(palabra):
        aux = [x for x in palabra]
        if i != len(palabra) - 1:
            aux.pop(i)
            aux.pop(i)
        if eval("".join(aux)):
            return "".join(aux)

cock = palix(palabra)

if cock == None:
    cock = palix2(palabra)

if cock != None:
    print(cock)

if cock == None:
    print("no palincock")
