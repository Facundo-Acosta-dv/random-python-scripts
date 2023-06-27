import mysql.connector
from mysql.connector import errorcode
from models.persona import Persona


class Conexion:
    # inicializa los datos necesarios para la conexion de la base de datos
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 3306
        self.user = 'dagaret' # usuario a usar
        self.password = 'lsycwds95' # clave del usuario
        self.database = 'persona' # base de datos a usar

        self.connect()

    # conecta la base de datos
    def connect(self):
        try:
            self.conexion = mysql.connector.connect(
                user=self.user,
                host=self.host,
                password=self.password,
                database=self.database,
                port=self.port
            )
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")

    # desconecta la base de datos
    def close_connexion(self):
        self.conexion.close()

    # hace un insert a una tabla en especifico, lo ideal es tener un insert por cada tabla con la que se ejecunten inserts
    def insert(self, persona: Persona):

        try:
            self.connect()  # se conecta a la base de datos

            cursor = self.conexion.cursor()  # se inicializa un cursor

            # se hace la consulta
            sql = "INSERT INTO persona VALUES(NULL, %s, %s, %s)"
            values = (persona.get_nombre(),
                      persona.get_edad(),
                      persona.get_email()
                      )  # se entregan los parametros en el orden que la tabla se crea para la insersion, debe ser tupla

            cursor.execute(sql, values)  # se ejecuta el sql

            self.conexion.commit()  # se guardan los cambios

        except Exception:
            print("ups, somethings went wrong")

        finally:
            self.close_connexion()  # se cierra la conexion

        return "insert done"

    def select_data(self):

        try:
            self.connect()

            cursor = self.conexion.cursor()
            sql = "SELECT * FROM persona"
            cursor.execute(sql)

            # se obtiene los datos del select como lista de tupla, cada tupla es una fila de la tabla persona que haga match con el tipo de selec
            personas = cursor.fetchall()

            lista = []
            for data in personas:  # se recorren las lista de tupla para crear una persona por vuelta
                persona = Persona(data[1], data[2], data[3])
                persona.set_id(data[0]) # seteo el id aparte ya que el constructor no lo inicializa
                lista.append(persona)

        except Exception:
            print("ups, somethings went wrong")

        finally:
            self.close_connexion()

        return lista  # se retorna una lista de personas
