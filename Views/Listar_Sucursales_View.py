import tkinter as tk
from tkinter import ttk
from Conexion import *
from datetime import datetime
from Modelo.Reportes import *
from Modelo.Consultas import *

class ListarSucursalesView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="Listar Sucursales", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Cuadro de búsqueda
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def create_widgets(self):

        lbl_title = tk.Label(self, text="Listar Sucursales", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        search_button = tk.Button(self, text="Buscar", command=self.search)
        search_button.grid(row=1, column=2, padx=5, pady=5)

        # Tabla
        self.table = ttk.Treeview(self, columns=("Nombre_Sucursal", "Nombre_Departamento", "Nombre_Municipio", "Cantidad_Empleados"))
        self.table.heading("Nombre_Sucursal", text="Nombre Sucursal")
        self.table.heading("Nombre_Departamento", text="Nombre Departamento")
        self.table.heading("Nombre_Municipio", text="Nombre Municipio")
        self.table.heading("Cantidad_Empleados", text="Cantidad Empleados")
        self.table.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky='nsew')

        lbl_profesion = ttk.Label(self, text="Generar Reporte Sucursales:")
        lbl_profesion.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        generate_button = tk.Button(self, text="Generar Reporte", command=self.generar_reporte)
        generate_button.grid(row=3, column=2, columnspan=3, pady=10)

    def generar_reporte(self):
        ruta_archivo = r"C:\Users\migue\Desktop\reportes\reporte_sucursales.pdf"
        Reportes.generar_reporte_sucursales(ruta_archivo)

    def search(self):
        search_text = self.search_entry.get()
        resultados = Consultas.buscar_sucursal(search_text)

        self.clear_table()

        if resultados:
            for row in resultados:
                self.table.insert("", "end", values=row)

    def clear_table(self):
        for row in self.table.get_children():
            self.table.delete(row)
