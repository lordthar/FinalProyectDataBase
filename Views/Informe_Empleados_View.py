import tkinter as tk
from tkinter import ttk
from Conexion import *
from datetime import datetime
from Modelo.Reportes import *
from Modelo.Consultas import *

class InformeEmpleadosView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="Listar Empleados", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Cuadro de búsqueda
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        search_button = tk.Button(self, text="Buscar", command=self.search)
        search_button.grid(row=1, column=2, padx=5, pady=5)

        # Crear tabla vacía
        self.table = ttk.Treeview(self, columns=("Nombre_Empleado", "Numero_Contrato", "Fecha_Contrato", "Fecha_Inicio", "Fecha_Terminacion", "Cargo", "Descripcion_Contrato"))
        self.table.heading("Nombre_Empleado", text="Nombre Empleado")
        self.table.heading("Numero_Contrato", text="Número Contrato")
        self.table.heading("Fecha_Contrato", text="Fecha Contrato")
        self.table.heading("Fecha_Inicio", text="Fecha Inicio")
        self.table.heading("Fecha_Terminacion", text="Fecha Terminación")
        self.table.heading("Cargo", text="Cargo")
        self.table.heading("Descripcion_Contrato", text="Descripción Contrato")
        self.table.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')

        generate_button = tk.Button(self, text="Generar Reporte", command=self.generar_reporte)
        generate_button.grid(row=3, column=0, columnspan=4, pady=10)

    def search(self):
        nombre_empleado = self.search_entry.get()
        resultados = Consultas.buscar_empleado(nombre_empleado)

        # Limpiar la tabla
        for row in self.table.get_children():
            self.table.delete(row)

        # Llenar la tabla con los resultados
        for row in resultados:
            self.table.insert("", "end", values=row)

    def generar_reporte(self):
        ruta_archivo = r"C:\Users\migue\Desktop\reportes\reporte_empleados.pdf"

