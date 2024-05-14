from Conexion import *

class Usuario:
    @staticmethod
    def ingresarUser(login_user, password_user, level_user, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Usuario VALUES (null, %s, %s, %s)"
            valores = (login_user, password_user, level_user)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Usuario Ingresado Correctamente")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    @staticmethod
    def verificar_login(login_user, password_user, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Usuario WHERE login_user = %s AND password_user = %s"
            valores = (login_user, password_user)
            cursor.execute(sql, valores)
            user = cursor.fetchone() 
            conection.close()

            return user is not None
        except mysql.connector.Error as error:
            print("Error de verificación de inicio de sesión: {}".format(error))


    @staticmethod
    def obtener_nivel_acceso(username, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT level_user FROM Usuario WHERE login_user = %s"
            cursor.execute(sql, (username,))
            nivel_acceso = cursor.fetchone()[0]
            conection.close()
            return nivel_acceso
        except mysql.connector.Error as error:
            print("Error al obtener nivel de acceso del usuario: {}".format(error))



