class Jugador:

    def __init__(self, nombre, energia, vida, estado, inventario):
        self.nombre = nombre
        self.energia = energia
        self.vida = vida
        self.estado = estado
        self.inventario = inventario

    #--------------getters-------------------

    def getNombre(self):
        return self.nombre

    def getInventario(self):
        return self.inventario

    def getEnergia(self):
        return self.energia

    def getVida(self):
        return self.vida

    def getEstado(self):
        return self.estado

    #------------------setters-------------------

    def setNombre(self, nombre):
        self.nombre = nombre
        #atributo = variable

    def setEnergia(self, energia):
        self.energia = energia

    def setVida(self, vida):
        self.vida = vida

    def setEstado(self, estado):
        self.estado = estado

    def getArmas(self, tipo):
        return self.inventario['armas'][tipo]

    def getObjeto(self, categoria, tipo):
        lista = self.inventario[categoria][tipo]
        return lista

    def getObjectById(self, lista, id):
        objeto = next((x for _, x in enumerate(lista) if x['id'] == id), None)
        return objeto

