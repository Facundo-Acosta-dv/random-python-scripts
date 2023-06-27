#clases en mayus
from Controller.controller import Controller
import os
from Models.jugador import Jugador

controller = Controller()

def objetosEnLista(variable):
    for objeto in variable:
        print(f"Id: {objeto['id']}-: {objeto['nombre']}")

def forObjetoInConsumibles(variable):
    for objeto in consumibles[f'{variable}']:
        print(f"Id: {objeto['id']}-: {objeto['nombre']}")

jugador = controller.get_jugador()
nombre_jugador = jugador.getNombre()
vida_jugador = jugador.getVida()
energia_jugador = jugador.getEnergia()
inventario = jugador.getInventario()
consumibles = jugador.inventario['consumibles']
elixires = jugador.inventario['consumibles']['elixir']

lista_melee = jugador.getObjeto("armas", "melee")
lista_ranged = jugador.getObjeto("armas", "ranged")

os.system("cls")

print("\nDatos del jugador:")
print("-----------------------------------")
print(
    f"Nombre: {nombre_jugador}\n"
    f"Vida: {vida_jugador}\n"
    f"Energia: {energia_jugador}\n"
    )
print("-----------------------------------")
print("Inventario del jugador: \n")
print("            •Armas•")

print("-Melee:")
for i, arma in enumerate(lista_melee):
    print(f"{i + 1}•{arma['nombre']}")
print("")

print("-Ranged:")
for i, arma in enumerate(lista_ranged):
    print(f"{i + 1}•{arma['nombre']}")

print("            •Consumibles• ")
print("-Elixires:")

for i, elixir in enumerate(consumibles['elixir']):
    print(f"{elixir['nombre']} ({elixir['cantidad']})")
print("")

print("-Comida: ")

for i, comida in enumerate(consumibles['comida']):
    print(f"{comida['nombre']} ({comida['cantidad']})")
print("")
# for arma in lista:
#     print(arma['id'])

print("Ids de objetos: ")
objetosEnLista(lista_melee)
objetosEnLista(lista_ranged)
forObjetoInConsumibles('comida')
forObjetoInConsumibles('elixir')


