import math
from random import random as rand

class Mascota:

    def __init__(self, nombre, raza) -> None:
        self.id = self.__gen_id()
        self.nombre = nombre
        self.raza = raza

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_raza(self):
        return self.raza

    def set_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def set_raza(self, raza_nueva):
        self.raza = raza_nueva

    def __gen_id(self, min=1):
        id = ""
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890"

        for _ in range(3):
            rdm = int(math.floor(rand() * ((len(caracteres) + 1 - min) - 1) + min))
            id += caracteres[rdm]

        return id
