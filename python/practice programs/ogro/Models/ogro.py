class Ogro:

    def __init__(self) -> None:
        self.nombre = "ogro Master"
        self.nivel = 1
        self.vida = self.__escalado(2000, self.nivel)
        self.energia = 20
        self.dmg = 150
        self.dmg_critico = 2
        self.prob_critica = 25
        self.armadura = 100
        self.arma = "garrote"

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

    def get_armadura(self):
        return self.armadura

    def get_nivel(self):
        return self.nivel

    def set_vida(self, dano):
        self.vida = self.vida - dano

    def __escalado(self, vida, nivel):
        return vida * ((nivel * 10 + 100) / 100)
