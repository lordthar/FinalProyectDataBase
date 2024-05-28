from Conexion import *
from Modelo.Usuario_Bitacora import *

class Usuario:
    @staticmethod
    def ingresarUser(codigo_usuario, login_user, password_user, level_user, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Usuario VALUES (%s, %s, %s, %s)"
            valores = (codigo_usuario, login_user, password_user, level_user)
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
            if user:
                Usuario_Bitacora.registrar_inicio_sesion(login_user)
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


    @staticmethod
    def eliminarUser(codigo_usuario, self= None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Usuario WHERE codigo_usuario = %s"
            valores = (codigo_usuario,)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Usuario eliminado correctamente")
        except mysql.connector.Error as error:
            print("Error al eliminar el usuario: {}".format(error))


    @staticmethod
    def actualizarUser(codigo_usuario, login_user, password_user, level_user, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Usuario SET login_user = %s, password_user = %s, level_user = %s WHERE codigo_usuario = %s"
            valores = (login_user, password_user, level_user, codigo_usuario)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Usuario actualizado correctamente")
        except mysql.connector.Error as error:
            print("Error al actualizar el usuario: {}".format(error))


    @staticmethod
    def buscarUser(codigo_usuario, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Usuario WHERE codigo_usuario = %s"
            valores = (codigo_usuario,)
            cursor.execute(sql, valores)
            usuario = cursor.fetchone()
            return usuario
        except mysql.connector.Error as error:
            print("Error al buscar el usuario: {}".format(error))

    @staticmethod
    def obtener_codigos_users(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT codigo_usuario FROM Usuario"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Profesión: {}".format(error))
            return []





