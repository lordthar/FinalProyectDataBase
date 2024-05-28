from Conexion import *
class Profesion:
    @staticmethod
    def ingresarProfesion(codigo_profesion, nombre_profesion, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Profesion VALUES (%s, %s)"
            valores = (codigo_profesion, nombre_profesion)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Profesión ingresada con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    @staticmethod
    def eliminarProfesion(codigo_profesion, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Profesion WHERE codigo_profesion = %s"
            cursor.execute(sql, (codigo_profesion,))
            conection.commit()
            print(cursor.rowcount, "Profesión eliminada con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al eliminar Profesión: {}".format(error))

    @staticmethod
    def actualizarProfesion(codigo_profesion, nombre_profesion, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Profesion SET nombre_profesion = %s WHERE codigo_profesion = %s"
            valores = (nombre_profesion, codigo_profesion)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Profesión actualizada con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al actualizar Profesión: {}".format(error))

    @staticmethod
    def buscarProfesion(codigo_profesion, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Profesion WHERE codigo_profesion = %s"
            cursor.execute(sql, (codigo_profesion,))
            profesion = cursor.fetchone()
            conection.close()
            return profesion
        except mysql.connector.Error as error:
            print("Error al buscar Profesión: {}".format(error))
            return None

    @staticmethod
    def obtener_codigos_Profesion(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT codigo_profesion FROM Profesion"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Profesión: {}".format(error))
            return []