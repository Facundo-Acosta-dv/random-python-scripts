from Models.jugador import Jugador
from Models.ogro import Ogro
import math
import random
import os

jugador = Jugador()
ogro = Ogro()




def atacar(dano, probabilidad, multiplicador):
    rng = random.randint(0, 100)
    return (dano * multiplicador) if rng < probabilidad else dano


# print(atacar(ogro.get_dmg(), ogro.get_probcritica(), ogro.get_dmgc()))

# print(ogro.get_dmg() * ogro.get_dmgc())
# print(ogro.get_dmg())

# def enfrentamiento():

power = True


print("enfrentamiento!")

while power:
    dano_a_ogrinho = atacar(jugador.get_dmg(), jugador.get_probcritica(), jugador.get_dmgc())
    dano_a_jugador = atacar(ogro.get_dmg(), ogro.get_probcritica(), ogro.get_dmgc())
    jugador.set_vida(dano_a_jugador)
    ogro.set_vida(dano_a_ogrinho)
    print(f"Hp de Ogrinho: {ogro.get_vida()}")
    print(f"Hp de Jugador: {jugador.get_vida()}")
    if ogro.get_vida() < 1:
        print("Jugador gana!")
        print(f"Hp de jugador: {jugador.get_vida()}")
        power = False
    if jugador.get_vida() < 1:
        print("Ogrinho gana!")
        print(f"Hp de ogrinho: {ogro.get_vida()}")
        power = False
input("")
os.system("cls")
