from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, Spacer
from Conexion import *
from datetime import datetime

class Reportes:

    @staticmethod
    def generar_reporte_sucursales(ruta_archivo):
        try:

            conexion = CConexion.ConexionBasedeDatos()
            cursor = conexion.cursor()


            consulta_sql = """
                SELECT Departamento.nombre_departamento AS Nombre_Departamento,
                       Municipio.nombre_municipio AS Nombre_Municipio,
                       Tipo_Municipio.nombre_Municipio AS Tipo_Municipio,
                       Sucursal.nombre_sucursal AS Nombre_Sucursal
                FROM ((Sucursal
                INNER JOIN Municipio ON Sucursal.codigo_municipio = Municipio.codigo_municipio)
                INNER JOIN Departamento ON Sucursal.codigo_departamento = Departamento.codigo_departamento)
                INNER JOIN Tipo_Municipio ON Municipio.codigo_Tipo_Municipio = Tipo_Municipio.codigo_Tipo_Municipio
                ORDER BY Departamento.nombre_departamento, Municipio.nombre_municipio, Sucursal.nombre_sucursal;
                """
            cursor.execute(consulta_sql)


            sucursales = cursor.fetchall()


            c = canvas.Canvas(ruta_archivo, pagesize=letter)
            ancho_pagina, alto_pagina = letter


            estilo_encabezado = getSampleStyleSheet()['Heading1']


            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(ancho_pagina / 2, alto_pagina - 50, "BancoUQ")
            c.setFont("Helvetica", 12)
            c.drawRightString(ancho_pagina - 30, alto_pagina - 70, f"Fecha de Generación: {datetime.now().strftime('%A, %d de %B de %Y %H:%M:%S')}")
            c.line(30, alto_pagina - 80, ancho_pagina - 30, alto_pagina - 80)


            titulo = "Reporte de Sucursales"
            ancho_titulo = c.stringWidth(titulo, "Helvetica-Bold", 14)
            c.setFont("Helvetica-Bold", 14)
            c.drawString((ancho_pagina - ancho_titulo) / 2, alto_pagina - 100, titulo)


            tabla_data = [["Departamento", "Municipio", "Tipo de Municipio", "Sucursal"]]
            tabla_data.extend(sucursales)

            tabla = Table(tabla_data)
            tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]))


            ancho_tabla, alto_tabla = tabla.wrapOn(c, ancho_pagina - 60, alto_pagina - 150)


            tabla.drawOn(c, (ancho_pagina - ancho_tabla) / 2, alto_pagina - 120 - alto_tabla)


            c.save()

            cursor.close()
            conexion.close()

        except Exception as e:
            print(f"Error al generar el reporte de sucursales: {e}")

    @staticmethod
    def generar_reporte_contratos(ruta_archivo):
        try:
            conexion = CConexion.ConexionBasedeDatos()
            cursor = conexion.cursor()

            consulta_sql = """
            SELECT Departamento.nombre_departamento AS Nombre_Departamento,
                   Empleado.nombre_empleado AS Nombre_Empleado,
                   Contrato.fecha_inicio_contrato AS Fecha_Inicio,
                   Contrato.fecha_terminacion_contrato AS Fecha_Terminacion,
                   Municipio.nombre_municipio AS Nombre_Municipio,
                   Sucursal.nombre_sucursal AS Nombre_Sucursal
            FROM (((Empleado
                   INNER JOIN Contrato ON Empleado.codigo_empleado = Contrato.empleado_contrato)
                   INNER JOIN Sucursal ON Contrato.sucursal_contrato = Sucursal.codigo_sucursal)
                   INNER JOIN Departamento ON Sucursal.codigo_departamento = Departamento.codigo_departamento)
                   INNER JOIN Municipio ON Sucursal.codigo_municipio = Municipio.codigo_municipio
            ORDER BY Departamento.nombre_departamento;
            """
            cursor.execute(consulta_sql)

            contratos = cursor.fetchall()

            c = canvas.Canvas(ruta_archivo, pagesize=letter)
            ancho_pagina, alto_pagina = letter

            # Estilo del encabezado
            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(ancho_pagina / 2, alto_pagina - 50, "BancoUQ")
            c.setFont("Helvetica", 12)
            c.drawRightString(ancho_pagina - 30, alto_pagina - 70, f"Fecha de Generación: {datetime.now().strftime('%A, %d de %B de %Y %H:%M:%S')}")
            c.line(30, alto_pagina - 80, ancho_pagina - 30, alto_pagina - 80)

            titulo = "Reporte de Contratos"
            ancho_titulo = c.stringWidth(titulo, "Helvetica-Bold", 14)
            c.setFont("Helvetica-Bold", 14)
            c.drawString((ancho_pagina - ancho_titulo) / 2, alto_pagina - 100, titulo)

            # Datos de la tabla
            tabla_data = [["Nombre Dep.", "Nombre Empl.", "Fecha Inicio", "Fecha Term.", "Nombre Mun.", "Nombre Suc."]]
            tabla_data.extend(contratos)

            # Ajustar el ancho de las columnas
            col_widths = [80, 80, 70, 70, 80, 80]

            tabla = Table(tabla_data, colWidths=col_widths)
            tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('FONTSIZE', (0, 0), (-1, -1), 10),  # Tamaño de fuente reducido
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

            ancho_tabla, alto_tabla = tabla.wrapOn(c, ancho_pagina - 60, alto_pagina - 150)
            tabla.drawOn(c, (ancho_pagina - ancho_tabla) / 2, alto_pagina - 120 - alto_tabla)

            c.save()

            cursor.close()
            conexion.close()

        except Exception as e:
            print(f"Error al generar el reporte de contratos: {e}")



