import tkinter as tk
from tkinter import ttk
from Conexion import *
from datetime import datetime
from Modelo.Reportes import *


class ListarContratosView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="Listar Contratos", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.table = ttk.Treeview(self, columns=("Número de Contrato", "Nombre del Empleado", "Fecha de Inicio", "Fecha de Terminación"))
        self.table.heading("#0", text="ID")
        self.table.heading("Número de Contrato", text="Número de Contrato")
        self.table.heading("Nombre del Empleado", text="Nombre del Empleado")
        self.table.heading("Fecha de Inicio", text="Fecha de Inicio")
        self.table.heading("Fecha de Terminación", text="Fecha de Terminación")
        self.table.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')

        generate_button = tk.Button(self, text="Generar Reporte", command=self.generar_reporte)
        generate_button.grid(row=2, column=0, columnspan=4, pady=10)

    def generar_reporte(self):
        ruta_archivo = r"C:\Users\migue\Desktop\reportes\reporte_Contratos.pdf"
        Reportes.generar_reporte_contratos(ruta_archivo)
