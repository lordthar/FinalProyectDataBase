from Conexion import *
class Municipio:
    @staticmethod
    def ingresarMunicipio(codigo_municipio, nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "INSERT INTO Municipio (codigo_municipio, nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio) VALUES (%s, %s, %s, %s, %s)"
            valores = (codigo_municipio, nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Municipio ingresado con exito")
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
            print("Error al obtener municipios: {}".format(error))
            return []

    @staticmethod
    def obtener_tipos_municipio(conexion):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre_Municipio FROM Tipo_Municipio")
            tipos_municipio = cursor.fetchall()
            return [nombre for nombre, in tipos_municipio]
        except mysql.connector.Error as error:
            print("Error al obtener tipos de municipio: {}".format(error))
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
    def obtener_codigo_tipo_municipio_seleccionado(conection, nombre_tipo_municipio):
        try:
            cursor = conection.cursor()
            cursor.execute("SELECT codigo_Tipo_Municipio FROM Tipo_Municipio WHERE nombre_Municipio = %s", (nombre_tipo_municipio,))
            resultado = cursor.fetchone()
            if resultado:
                codigo_tipo_municipio = resultado[0]
                return codigo_tipo_municipio
            else:
                print("No se encontró el código del tipo de municipio para el nombre seleccionado.")
                return None
        except mysql.connector.Error as error:
            print(f"Error al obtener el código del tipo de municipio: {error}")
            return None



    @staticmethod
    def eliminarMunicipio(codigo_municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "DELETE FROM Municipio WHERE codigo_municipio = %s"
            cursor.execute(sql, (codigo_municipio,))
            conection.commit()
            print(cursor.rowcount, "Municipio eliminado con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al eliminar municipio:", error)

    @staticmethod
    def actualizarMunicipio(codigo_municipio, nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "UPDATE Municipio SET nombre_municipio = %s, poblacion_municipio = %s, codigo_departamento = %s, codigo_tipo_municipio = %s WHERE codigo_municipio = %s"
            valores = (nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio, codigo_municipio)
            cursor.execute(sql, valores)
            conection.commit()
            print(cursor.rowcount, "Municipio actualizado con éxito")
            conection.close()
        except mysql.connector.Error as error:
            print("Error al actualizar municipio:", error)

    @staticmethod
    def buscarMunicipio(codigo_municipio, self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT * FROM Municipio WHERE codigo_municipio = %s"
            cursor.execute(sql, (codigo_municipio,))
            municipio = cursor.fetchone()
            conection.close()
            return municipio
        except mysql.connector.Error as error:
            print("Error al buscar municipio:", error)
            return None

    @staticmethod
    def obtener_codigos_municipio(self=None):
        try:
            conection = CConexion.ConexionBasedeDatos(self)
            cursor = conection.cursor()
            sql = "SELECT codigo_municipio FROM Municipio"
            cursor.execute(sql)
            codigos = cursor.fetchall()
            conection.close()
            return [codigo[0] for codigo in codigos]
        except mysql.connector.Error as error:
            print("Error al obtener códigos de Profesión: {}".format(error))
            return []