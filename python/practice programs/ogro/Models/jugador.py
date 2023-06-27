class Jugador:

    def __init__(self) -> None:
        self.nombre = "facundo"
        self.nivel = 2
        self.vida = self.__escalado(1000, self.nivel)
        self.energia = 100
        self.dmg = 150
        self.dmg_critico = 3
        self.prob_critica = 50
        self.arma = "scythe"

    def get_nombre(self):
        return self.nombre

    def get_vida(self):
        return self.vida

    def get_energia(self):
        return self.energia

    def get_dmg(self):
        return self.dmg

    def get_dmgc(self):
        return self.dmg_critico

    def get_probcritica(self):
        return self.prob_critica

    def get_nivel(self):
        return self.nivel


    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_vida(self, dano):
        self.vida = self.vida - dano

    def __escalado(self, vida, nivel):
        return vida * ((nivel * 10 + 100) / 100)
