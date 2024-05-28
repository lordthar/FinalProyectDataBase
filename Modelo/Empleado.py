from Conexion import *

class Empleado:

    @staticmethod
    def ingresarEmpleado(codigo_empleado, nombre_empleado, telefono_empleado,cedula_empleado, direccion_empleado, codigo_profesion, genero_empleado, fechaNTO_empleado, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Empleado (codigo_empleado, nombre_empleado, telefono_empleado, cedula_empleado,direccion_empleado, codigo_profesion, genero_empleado, fechaNTO_empleado) VALUES (%s, %s, %s, %s , %s, %s, %s, %s)"
            valores = (codigo_empleado, nombre_empleado, telefono_empleado, cedula_empleado, direccion_empleado, codigo_profesion, genero_empleado, fechaNTO_empleado)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Empleado ingresado con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))


    @staticmethod
    def obtener_profesiones(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_profesion FROM Profesion")
            profesion = cursor.fetchall()
            return [nombre for nombre, in profesion]
        except mysql.connector.Error as error:
            print("Error al obtener profesiones: {}".format(error))
            return []


    @staticmethod
    def obtener_codigo_profesion_seleccionada(conection, nombre_profesion):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_profesion FROM Profesion WHERE nombre_profesion = %s", (nombre_profesion,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_departamento = resultado[0]
                return codigo_departamento
            else:
                print("No se encontró el código de la profesion para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código de la profesion: {error}")
            return None

    @staticmethod
    def eliminarEmpleado(codigo_empleado, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Empleado WHERE codigo_empleado = %s"
            cursor.execute(sql, (codigo_empleado,))
            conection.commit()
            print(cursor.rowcount, "Empleado eliminado con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al eliminar empleado: {}".format(error))

    @staticmethod
    def actualizarEmpleado(codigo_empleado, nombre_empleado, telefono_empleado, direccion_empleado, codigo_profesion, genero_empleado, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Empleado SET nombre_empleado = %s, telefono_empleado = %s, direccion_empleado = %s, codigo_profesion = %s, genero_empleado = %s WHERE codigo_empleado = %s"
            valores = (nombre_empleado, telefono_empleado, direccion_empleado, codigo_profesion, genero_empleado, codigo_empleado)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Empleado actualizado con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al actualizar empleado: {}".format(error))

    @staticmethod
    def buscarEmpleado(codigo_empleado, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Empleado WHERE codigo_empleado = %s"
            cursor.execute(sql, (codigo_empleado,))
            empleado = cursor.fetchone()
            conection.close()
            return empleado
        except mysql.connector.Error as error:
            print("Error al buscar empleado: {}".format(error))

    @staticmethod
    def obtener_codigos_empleado(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT codigo_empleado FROM Empleado"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Profesión: {}".format(error))
            return []