import random as rand

class melee:

    for wp in self.melee:
        print("a")

    def __init__(self, nombre, rareza, daño, id) -> None:
        self.nombre = nombre
        self.rareza = rand.randint(1, 10)
        self.daño = daño
        self.id = rand()
