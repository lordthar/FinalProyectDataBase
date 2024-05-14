import tkinter as tk
from tkinter import messagebox

class PopupAcercaDe(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acerca de")

        self.geometry("750x150")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        info_label = tk.Label(self, text="Hola, Bienvenido a la Aplicación Para Crear la Base de Datos de tu Banco")
        info_label.pack(padx=20, pady=10)

        nombre_label = tk.Label(self, text="Somos Huendy Caicedo T y Miguel Angel Garcia Osorio")
        nombre_label.pack(padx=20, pady=5)

        info_label = tk.Label(self, text="Esta app fue desarrollada con el fin de solucionar la necesidad de los bancos de gestionar su información mediante bases de datos")
        info_label.pack(padx=20, pady=5)

        close_button = tk.Button(self, text="Aceptar", command=self.destroy)
        close_button.pack(padx=20, pady=10)