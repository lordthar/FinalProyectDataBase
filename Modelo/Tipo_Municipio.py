from Conexion import *

class Tipo_Municipio:
    @staticmethod
    def ingresarTipo_Municipio(codigo_Tipo_Municipio, nombre_Municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Tipo_Municipio VALUES (%s, %s)"
            valores = (codigo_Tipo_Municipio, nombre_Municipio)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Tipo Municipio ingresado con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    @staticmethod
    def eliminarTipo_Municipio(codigo_Tipo_Municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Tipo_Municipio WHERE codigo_Tipo_Municipio = %s"
            cursor.execute(sql, (codigo_Tipo_Municipio,))
            conection.commit()
            print(cursor.rowcount, "Tipo Municipio eliminado con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al eliminar Tipo de Municipio: {}".format(error))

    @staticmethod
    def actualizarTipo_Municipio(codigo_Tipo_Municipio, nombre_Municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Tipo_Municipio SET nombre_Municipio = %s WHERE codigo_Tipo_Municipio = %s"
            valores = (nombre_Municipio, codigo_Tipo_Municipio)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Tipo Municipio actualizado con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al actualizar Tipo de Municipio: {}".format(error))

    @staticmethod
    def buscarTipo_Municipio(codigo_Tipo_Municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Tipo_Municipio WHERE codigo_Tipo_Municipio = %s"
            cursor.execute(sql, (codigo_Tipo_Municipio,))
            tipo_municipio = cursor.fetchone()
            conection.close()
            return tipo_municipio
        except mysql.connector.Error as error:
            print("Error al buscar Tipo de Municipio: {}".format(error))
            return None

    @staticmethod
    def obtener_ids_tipo_municipio(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo_Tipo_Municipio FROM Tipo_Municipio")
            ids_tipo_municipio = cursor.fetchall()
            return [codigo for codigo, in ids_tipo_municipio]
        except mysql.connector.Error as error:
            print("Error al obtener IDs de tipo de municipio: {}".format(error))
            return []

