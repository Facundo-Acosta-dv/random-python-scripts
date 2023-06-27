
#auto
class Auto:

    def __init__(self, marca, modelo, placa) -> None:
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_placa(self):
        return self.placa

