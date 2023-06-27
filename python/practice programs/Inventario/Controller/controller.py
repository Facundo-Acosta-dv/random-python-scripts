import math
from random import random as rand
from Models.jugador import Jugador as player

class Controller:

    def __init__(self) -> None:
        self.jugador = {
            "nombre": "Facundo",
            "vida": 1000,
            "estado": 1,
            "energia": 100,
            "inventario": {
                "armas": {
                    "melee": [
                        {
                            "id": self.__generateId(),
                            "nombre": "guadaña de la hermana frita",
                            "damage": 100,
                            "cc": .45,
                            "cd": 2,
                            "true damage": .03
                        },
                        {
                            "id": self.__generateId(),
                            "nombre": "espada soputa",
                            "damage": 90,
                            "cc": .15,
                            "cd": 4,
                            "true damage": .13
                        },
                        {
                            "id": self.__generateId(),
                            "nombre": "lanza lance",
                            "damage": 150,
                            "cc": .80,
                            "cd": 2.4,
                            "true damage": .3
                        },
                        {
                            "id": self.__generateId(),
                            "nombre": "alabarda",
                            "damage": 200,
                            "cc": .12,
                            "cd": 3,
                            "true damage": .7
                        }
                    ],
                    "ranged": [
                        {
                            "id": self.__generateId(),
                            "nombre": "Vectis",
                            "damage": 700,
                            "cc": .89,
                            "cd": 2.7,
                            "true damage": .03
                        },
                        {
                            "id": self.__generateId(),
                            "nombre": "escoputa",
                            "damage": 500,
                            "cc": .5,
                            "cd": 5,
                            "true damage": .03
                        },
                    ]
                },
                "consumibles": {
                    "elixir": [
                        {
                            "id": self.__generateId(),
                            "nombre": "elixir de vida",
                            "recupera": 200,
                            "cantidad": 10
                        },
                        {
                            "id": self.__generateId(),
                            "nombre": "elixir de mana",
                            "recupera": 100,
                            "cantidad": 15
                        }
                    ],
                    "comida": [
                        {
                            "id": self.__generateId(),
                            "nombre": "manzana",
                            "recupera": 200,
                            "cantidad": 3
                        },
                        {
                            "id": self.__generateId(),
                            "nombre": "vodka",
                            "recupera": -50,
                            "cantidad": 10
                        }
                    ]
                }
            }
        }

    def __generateId(self, min=1):
        """
        It generates a random string of 15 characters, using the characters in the string
        "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890"

        :param min: The minimum number of characters to be generated, defaults to 1 (optional)
        :return: A string of 15 characters.
        """
        id = ""
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890"

        for _ in range(3):
            rdm = int(math.floor(rand() * ((len(caracteres) + 1 - min) - 1) + min))
            id += caracteres[rdm]

        return id

    def get_jugador(self):
        nombre = self.jugador['nombre']
        energia = self.jugador['energia']
        vida = self.jugador['vida']
        estado = self.jugador['estado']
        inventario = self.jugador['inventario']

        jugador = player(nombre, energia, vida, estado, inventario)
        return jugador
