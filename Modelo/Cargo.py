from Conexion import *
class Cargo:
    @staticmethod
    def ingresarCargos(codigo_cargo, nombre_cargo, salario_cargo, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Cargo VALUES (%s, %s, %s)"
            valores = (codigo_cargo, nombre_cargo, salario_cargo)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Cargo ingresado con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    @staticmethod
    def eliminarCargo(codigo_cargo, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Cargo WHERE codigo_cargo = %s"
            cursor.execute(sql, (codigo_cargo,))
            conection.commit()
            print(cursor.rowcount, "Cargo eliminado con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al eliminar Cargo: {}".format(error))

    @staticmethod
    def actualizarCargo(codigo_cargo, nombre_cargo, salario_cargo, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Cargo SET nombre_cargo = %s, salario_cargo = %s WHERE codigo_cargo = %s"
            valores = (nombre_cargo, salario_cargo, codigo_cargo)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Cargo actualizado con exito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al actualizar Cargo: {}".format(error))

    @staticmethod
    def buscarCargo(codigo_cargo, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Cargo WHERE codigo_cargo = %s"
            cursor.execute(sql, (codigo_cargo,))
            cargo = cursor.fetchone()
            conection.close()
            return cargo
        except mysql.connector.Error as error:
            print("Error al buscar Cargo: {}".format(error))
            return None

    @staticmethod
    def obtener_codigos_Cargo(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT codigo_cargo FROM Cargo"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Cargo: {}".format(error))
            return []
