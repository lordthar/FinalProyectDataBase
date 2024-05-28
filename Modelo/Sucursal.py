from Conexion import *
class Sucursal:


    @staticmethod
    def ingresarSucursal(codigo_sucursal, nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Sucursal (codigo_sucursal, nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (codigo_sucursal, nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Sucursal ingresada con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    @staticmethod
    def obtener_departamentos(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_departamento FROM Departamento")
            departamentos = cursor.fetchall()
            return [nombre for nombre, in departamentos]
        except mysql.connector.Error as error:
            print("Error al obtener departamentos: {}".format(error))
            return []

    @staticmethod
    def obtener_municipio(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_Municipio FROM Municipio")
            municipio = cursor.fetchall()
            return [nombre for nombre, in municipio]
        except mysql.connector.Error as error:
            print("Error al obtener los municipios: {}".format(error))
            return []


    @staticmethod
    def obtener_codigo_departamento_seleccionado(conection, nombre_departamento):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_departamento FROM Departamento WHERE nombre_departamento = %s", (nombre_departamento,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_departamento = resultado[0]
                return codigo_departamento
            else:
                print("No se encontró el código del departamento para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código del departamento: {error}")
            return None

    @staticmethod
    def obtener_codigo_municipio_seleccionado(conection, nombre_tipo_municipio):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_Municipio FROM Municipio WHERE nombre_Municipio = %s", (nombre_tipo_municipio,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_municipio = resultado[0]
                return codigo_municipio
            else:
                print("No se encontró el código del municipio para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código del tipo de municipio: {error}")
            return None

    @staticmethod
    def eliminarSucursal(codigo_sucursal, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Sucursal WHERE codigo_sucursal = %s"
            cursor.execute(sql, (codigo_sucursal,))
            conection.commit()
            print(cursor.rowcount, "Sucursal eliminada con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al eliminar la sucursal: {}".format(error))

    @staticmethod
    def actualizarSucursal(codigo_sucursal, nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Sucursal SET nombre_sucursal = %s, direccion_sucursal = %s, telefono_sucursal = %s, codigo_municipio = %s, codigo_departamento = %s, sucursal_presupuesto = %s WHERE codigo_sucursal = %s"
            valores = (nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto, codigo_sucursal)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Sucursal actualizada con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al actualizar la sucursal: {}".format(error))

    @staticmethod
    def buscarSucursal(codigo_sucursal, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Sucursal WHERE codigo_sucursal = %s"
            cursor.execute(sql, (codigo_sucursal,))
            sucursal = cursor.fetchone()
            conection.close()
            return sucursal
        except mysql.connector.Error as error:
            print("Error al buscar la sucursal: {}".format(error))
            return None

    @staticmethod
    def obtener_codigos_sucursal(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT codigo_sucursal FROM Sucursal"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Profesión: {}".format(error))
            return []