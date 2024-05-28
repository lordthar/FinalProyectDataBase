from Conexion import *

class Usuario_Bitacora:
    @staticmethod
    def registrar_inicio_sesion(login_user):
        try:
            conexion = CConexion.ConexionBasedeDatos()
            cursor = conexion.cursor()
            sql = "INSERT INTO BitacoraUsuario (login_usuario, accion, fecha_hora) VALUES (%s, %s, NOW())"
            valores = (login_user, "Inicio de sesión")
            cursor.execute(sql, valores)
            conexion.commit()
            print("Inicio de sesión registrado en la bitácora")
            conexion.close()
        except mysql.connector.Error as error:
            print("Error al registrar inicio de sesión en la bitácora: {}".format(error))

    @staticmethod
    def registrar_cierre_sesion(login_user):
        try:
            conexion = CConexion.ConexionBasedeDatos()
            cursor = conexion.cursor()
            sql = "INSERT INTO BitacoraUsuario (login_usuario, accion, fecha_hora) VALUES (%s, %s, NOW())"
            valores = (login_user, "Cierre de sesión")
            cursor.execute(sql, valores)
            conexion.commit()
            print("Cierre de sesión registrado en la bitácora")
            conexion.close()
        except mysql.connector.Error as error:
            print("Error al registrar cierre de sesión en la bitácora: {}".format(error))