import tkinter as tk
from tkinter import ttk
from Conexion import *
from datetime import datetime
from Modelo.Reportes import *

class InformeDeptosView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="Listar Sucursales", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.table = ttk.Treeview(self, columns=("Login Usuario", "Acción", "Fecha y Hora"))
        self.table.heading("#0", text="ID")
        self.table.heading("Login Usuario", text="Login Usuario")
        self.table.heading("Acción", text="Acción")
        self.table.heading("Fecha y Hora", text="Fecha y Hora")
        self.table.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')

        generate_button = tk.Button(self, text="Generar Reporte")
        generate_button.grid(row=2, column=0, columnspan=4, pady=10)
