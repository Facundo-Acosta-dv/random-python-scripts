class Persona:

    # los datos del modelo deben ser los mismos que el de la tabla en la bd, aca omiti el id por que no altero datos, pedo debe estar
    def __init__(self, nombre: str, edad: int, email: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.email: str = email
        self.id: int

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
