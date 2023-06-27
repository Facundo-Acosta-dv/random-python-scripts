from models.persona import Persona
from controllers.conexion import Conexion
from os import system

if __name__ == '__main__':
    val = True

    while val:
        conexion = Conexion()
        print("Ingrese opcion")
        print("1. ingresar persona")
        print("2. listar personas")
        print("3. salir")
        opcion = input("opcion > ")

        match opcion:
            case '1':
                system("clear")
                nombre = input("Ingrese nombre > ")
                edad = int(input("Ingrese edad > "))
                email = input("Ingrese email > ")

                persona = Persona(nombre, edad, email)

                res = conexion.insert(persona)

                system("clear")
                print(res)

            case '2':
                system("clear")

                personas = conexion.select_data()

                for persona in personas:
                    print("-----------------------------------------")
                    print(f"Persona numero {persona.get_id()}")
                    print(f"nombre: {persona.get_nombre()}")
                    print(f"edad: {persona.get_edad()}")
                    print(f"email: {persona.get_email()}")
                    print("-----------------------------------------")
                    print("\n")

            case '3':
                val = False
