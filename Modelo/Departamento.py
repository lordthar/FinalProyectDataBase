from Conexion import *

class Departamento:
        @staticmethod
        def ingresarDeptos(codigo_departamento, nombre_departamento, poblacion_departamento, self=None):
            try:
                conection = CConexion.ConexionBasedeDatos(self)
                cursor = conection.cursor()
                sql = "INSERT INTO Departamento VALUES (%s, %s, %s)"
                valores = (codigo_departamento, nombre_departamento, poblacion_departamento)
                cursor.execute(sql, valores)
                conection.commit()
                print(cursor.rowcount, "Departamento ingresado con exito")
                conection.close()
            except mysql.connector.Error as error:
                print("Error de ingreso de datos: {}".format(error))

        @staticmethod
        def obtener_ids_departamento(conexion):
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT codigo_departamento FROM Departamento")
                ids_departamento = cursor.fetchall()
                return [id_dep for id_dep, in ids_departamento]
            except mysql.connector.Error as error:
                print("Error al obtener los IDs de departamento: {}".format(error))
                return []


        @staticmethod
        def actualizarDeptos(codigo_departamento, nombre_departamento, poblacion_departamento, self=None):
            try:
                conection = CConexion.ConexionBasedeDatos(self)
                cursor = conection.cursor()
                sql = "UPDATE Departamento SET nombre_departamento = %s, poblacion_departamento = %s WHERE codigo_departamento = %s"
                valores = (nombre_departamento, poblacion_departamento, codigo_departamento)
                cursor.execute(sql, valores)
                conection.commit()
                print(cursor.rowcount, "Departamento actualizado con exito")
                conection.close()
            except mysql.connector.Error as error:
                print("Error al actualizar datos: {}".format(error))

        @staticmethod
        def eliminarDeptos(codigo_departamento, self=None):
            try:
                conection = CConexion.ConexionBasedeDatos(self)
                cursor = conection.cursor()
                sql = "DELETE FROM Departamento WHERE codigo_departamento = %s"
                valores = (codigo_departamento,)
                cursor.execute(sql, valores)
                conection.commit()
                print(cursor.rowcount, "Departamento eliminado con exito")
                conection.close()
            except mysql.connector.Error as error:
                print("Error al eliminar datos: {}".format(error))

        @staticmethod
        def buscarDeptos(codigo_departamento, self=None):
            try:
                conection = CConexion.ConexionBasedeDatos(self)
                cursor = conection.cursor()
                sql = "SELECT * FROM Departamento WHERE codigo_departamento = %s"
                valores = (codigo_departamento,)
                cursor.execute(sql, valores)
                departamento = cursor.fetchone()
                if departamento:
                    return departamento
                else:
                    print("No se encontró el departamento con el código especificado.")
                    return None
            except mysql.connector.Error as error:
                print("Error al buscar datos: {}".format(error))
                return None