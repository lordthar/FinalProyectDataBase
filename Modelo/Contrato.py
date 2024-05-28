from Conexion import *
class Contrato:

    @staticmethod
    def ingresarContrato(numero_contrato, fecha_contrato,fecha_inicio_contrato ,fecha_terminacion_contrato, cargo_contrato, descripcion_contrato, sucursal_contrato, empleado_contrato, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Contrato (numero_contrato, fecha_contrato, fecha_inicio_contrato,fecha_terminacion_contrato, cargo_contrato, descripcion_contrato, sucursal_contrato, empleado_contrato) VALUES (%s, %s, %s ,%s, %s, %s, %s, %s)"
            valores = (numero_contrato, fecha_contrato, fecha_inicio_contrato,fecha_terminacion_contrato, cargo_contrato, descripcion_contrato, sucursal_contrato, empleado_contrato)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Contrato ingresado con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    @staticmethod
    def eliminarContrato(numero_contrato, self=None):
        conection = CConexion.ConexionBasedeDatos(self)
        try:
            cursor = conection.cursor()
            sql = "DELETE FROM Contrato WHERE numero_contrato = %s"
            valores = (numero_contrato,)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Contrato eliminado con éxito")
        except mysql.connector.Error as error:
            print("Error al eliminar el contrato: {}".format(error))


    @staticmethod
    def actualizarContrato(numero_contrato, fecha_contrato,fecha_inicio_contrato ,fecha_terminacion_contrato, cargo_contrato, descripcion_contrato, sucursal_contrato, empleado_contrato, self=None):

        conection = CConexion.ConexionBasedeDatos(self)
        try:
            cursor = conection.cursor()
            sql = "UPDATE Contrato SET fecha_contrato = %s, fecha_inicio_contrato = %s,fecha_terminacion_contrato = %s, cargo_contrato = %s, descripcion_contrato = %s, sucursal_contrato = %s, empleado_contrato = %s WHERE numero_contrato = %s"
            valores = (fecha_contrato, fecha_inicio_contrato, fecha_terminacion_contrato, cargo_contrato, descripcion_contrato, sucursal_contrato, empleado_contrato, numero_contrato)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Contrato actualizado con éxito")
        except mysql.connector.Error as error:
            print("Error al actualizar el contrato: {}".format(error))

    @staticmethod
    def buscarContrato(numero_contrato, self=None):
        conection = CConexion.ConexionBasedeDatos(self)
        try:
            cursor = conection.cursor()
            sql = "SELECT * FROM Contrato WHERE numero_contrato = %s"
            valores = (numero_contrato,)
            cursor.execute(sql, valores)
            contrato = cursor.fetchone()
            return contrato
        except mysql.connector.Error as error:
            print("Error al buscar el contrato: {}".format(error))


    @staticmethod
    def obtener_cargo(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_cargo FROM Cargo")
            cargo = cursor.fetchall()
            return [nombre for nombre, in cargo]
        except mysql.connector.Error as error:
            print("Error al obtener cargo: {}".format(error))
            return []

    @staticmethod
    def obtener_codigo_cargo_seleccionado(conection, nombre_cargo):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_cargo FROM Cargo WHERE nombre_cargo = %s", (nombre_cargo,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_cargo = resultado[0]
                return codigo_cargo
            else:
                print("No se encontró el código del cargo para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código del cargo: {error}")
            return None

    @staticmethod
    def obtener_sucursal(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_sucursal FROM Sucursal")
            sucursal = cursor.fetchall()
            return [nombre for nombre, in sucursal]
        except mysql.connector.Error as error:
            print("Error al obtener la sucursal: {}".format(error))
            return []

    @staticmethod
    def obtener_codigo_sucursal_seleccionada(conection, nombre_sucursal):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_sucursal FROM Sucursal WHERE nombre_sucursal = %s", (nombre_sucursal,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_sucursal = resultado[0]
                return codigo_sucursal
            else:
                print("No se encontró el código de la sucursal para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código de la sucursal: {error}")
            return None

    @staticmethod
    def obtener_empleado(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_empleado FROM Empleado")
            empleado = cursor.fetchall()
            return [nombre for nombre, in empleado]
        except mysql.connector.Error as error:
            print("Error al obtener el empleado: {}".format(error))
            return []

    @staticmethod
    def obtener_codigo_empleado_seleccionado(conection, nombre_empleado):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_empleado FROM Empleado WHERE nombre_empleado = %s", (nombre_empleado,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_empleado = resultado[0]
                return codigo_empleado
            else:
                print("No se encontró el código del empleado para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código del empleado: {error}")
            return None

    @staticmethod
    def obtener_codigos_contrato(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT numero_contrato FROM Contrato"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Profesión: {}".format(error))
            return []