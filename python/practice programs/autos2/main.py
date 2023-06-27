from enum import auto
from Models.auto import Auto
import os

def validar(mensaje):
    val = True
    while val:
        try:
            sexo = int(input(mensaje))
            val = False
        except ValueError:
            print("Ingrese numero BRO")
            val = True
    return sexo


autos = []

def append_auto(marca, modelo, placa):
    global autos
    autos.append(Auto(marca, modelo, placa))

def añadir_autos():

    os.system("clear")
    print(f"{'_':_^50}")
    cantidad = validar("ingrese cantidad a ingresar: ")

    for _ in range(cantidad):
        marca_auto = input("ingrese marca: ")
        modelo_auto = input("ingrese modelo: ")
        placa_auto = input("ingrese placa: ")
        append_auto(marca_auto, modelo_auto, placa_auto)

añadir_autos()
print(dir(Auto))


for i, auto in enumerate(autos):
    print(
        f"{i + 1}👉",
        auto.get_marca(),
        auto.get_modelo(),
        auto.get_placa()
        )

def get_auto_wPlaca(placa):
    for _, auto in enumerate(autos):
        if auto.get_placa() == placa:
            return auto

sexo = input("placa: ")
exe = get_auto_wPlaca(sexo)
print(exe)

