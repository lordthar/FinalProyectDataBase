
from Conexion import CConexion

class Consultas:
    @staticmethod
    def buscar_sucursal(nombre_sucursal):
        try:
            # Establecer conexión a la base de datos
            conexion = CConexion.ConexionBasedeDatos()
            cursor = conexion.cursor()

            # Consulta SQL para buscar la sucursal por nombre
            consulta_sql = """
                SELECT Sucursal.nombre_sucursal AS Nombre_Sucursal,
                       Departamento.nombre_departamento AS Nombre_Departamento,
                       Municipio.nombre_municipio AS Nombre_Municipio,
                       COUNT(Empleado.codigo_empleado) AS Cantidad_Empleados
                FROM (((Empleado
                       INNER JOIN Contrato ON Empleado.codigo_empleado = Contrato.empleado_contrato)
                       INNER JOIN Sucursal ON Contrato.sucursal_contrato = Sucursal.codigo_sucursal)
                       INNER JOIN Departamento ON Sucursal.codigo_departamento = Departamento.codigo_departamento)
                       INNER JOIN Municipio ON Sucursal.codigo_municipio = Municipio.codigo_municipio
                WHERE Sucursal.nombre_sucursal LIKE %s
                GROUP BY Sucursal.nombre_sucursal, Departamento.nombre_departamento, Municipio.nombre_municipio
                ORDER BY Sucursal.nombre_sucursal;
            """
            cursor.execute(consulta_sql, (f'%{nombre_sucursal}%',))

            resultados = cursor.fetchall()

            cursor.close()
            conexion.close()

            return resultados

        except Exception as e:

            print(f"Error al buscar la sucursal: {e}")
            return None

    @staticmethod
    def buscar_empleado(nombre_empleado):
        try:
            # Establecer conexión a la base de datos
            conexion = CConexion.ConexionBasedeDatos()
            cursor = conexion.cursor()

            # Consulta SQL para buscar empleados por nombre
            consulta_sql = """
                SELECT Empleado.nombre_empleado AS Nombre_Empleado,
                       Contrato.numero_contrato AS Numero_Contrato,
                       Contrato.fecha_contrato AS Fecha_Contrato,
                       Contrato.fecha_inicio_contrato AS Fecha_Inicio,
                       Contrato.fecha_terminacion_contrato AS Fecha_Terminacion,
                       Contrato.cargo_contrato AS Cargo,
                       Contrato.descripcion_contrato AS Descripcion_Contrato
                FROM Empleado
                INNER JOIN Contrato ON Empleado.codigo_empleado = Contrato.empleado_contrato
                WHERE Empleado.nombre_empleado LIKE %s
                ORDER BY Empleado.nombre_empleado;
            """
            cursor.execute(consulta_sql, (f'%{nombre_empleado}%',))

            resultados = cursor.fetchall()

            cursor.close()
            conexion.close()

            return resultados

        except Exception as e:
            print(f"Error al buscar el empleado: {e}")
            return None
