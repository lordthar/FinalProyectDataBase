from Conexion import *

class Departamento:
        @staticmethod
        def ingresarDeptos(nombre_departamento, poblacion_departamento, self=None):
            try:
                conection = CConexion.ConexionBasedeDatos(self)
                cursor = conection.cursor()
                sql = "INSERT INTO Departamento VALUES (null, %s, %s)"
                valores = (nombre_departamento, poblacion_departamento)
                cursor.execute(sql, valores)
                conection.commit()
                print(cursor.rowcount, "Departamento ingresado con exito")
                conection.close()
            except mysql.connector.Error as error:
                print("Error de ingreso de datos: {}".format(error))

        @staticmethod
        def eliminarDatos(codigo_departamento, self=None):
            try:
                conection = CConexion.ConexionBasedeDatos(self)
                cursor = conection.cursor()
                sql = "DELETE FROM Departamento WHERE codigo_departamento = %s"
                valores = (codigo_departamento, )
                cursor.execute(sql, valores)
                conection.commit()
                print(cursor.rowcount, "Departamento eliminado")
                conection.close()
                conection.close()

            except mysql.connector.Error as error:
                print("Error de eliminacion de datos: {}".format(error))