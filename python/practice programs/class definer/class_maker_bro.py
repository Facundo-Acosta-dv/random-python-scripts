############: automatting shit w/python; class maker :#################
import os
def intv(inputx):
    val=True
    while val:
        try:
            nx=int(input(inputx))
            val=False
        except ValueError:
            print("solo números")
    return nx
name=input("nombre de clase: ").capitalize()
cantidad=intv("cantidad de atributos: ")
attrx=[]
for _ in range(cantidad):
    atr=str(input("inserte atributo: "))
    attrx.append(atr)
attrstr=', '.join(attrx)
os.system("clear")
print(f"import random as r\n\nclass {name}:\n    def __init__(self, {attrstr}) -> None:")
for i in attrx:
    if i != "id":
        print(f"        self.{i} = {i}")
    if i == "id":
        print(f"        self.{i} = r.randint(1, 10000)")
print("#getters\n")
for i in attrx:
    print(f"    def get_{i}(self):\n"
    f"        return self.{i}\n")
print("#setters\n")
for i in attrx:
    if i != "id":
        print(f"    def set_{i}(self, {i}_nuevo):\n"
            f"        self.{i} = {i}_nuevo\n")
