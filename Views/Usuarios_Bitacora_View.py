from tkinter import ttk
import tkinter as tk
from Conexion import *

class usuarios_bitacora_view(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_table()

    def create_table(self):
        self.table_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.table_frame.pack(padx=100, pady=50)


        lbl_title = tk.Label(self.table_frame, text="Bitácora de Usuarios", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        self.table = ttk.Treeview(self.table_frame, columns=("Login Usuario", "Acción", "Fecha y Hora"))
        self.table.heading("#0", text="ID")
        self.table.heading("Login Usuario", text="Login Usuario")
        self.table.heading("Acción", text="Acción")
        self.table.heading("Fecha y Hora", text="Fecha y Hora")
        self.table.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')



        self.update_table()

    def update_table(self):

        for row in self.table.get_children():
            self.table.delete(row)

        conexion = CConexion.ConexionBasedeDatos()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM BitacoraUsuario")
        bitacora = cursor.fetchall()

        for i, (id_usuario, login_usuario, accion, fecha_hora) in enumerate(bitacora, 1):
            self.table.insert("", "end", text=str(i), values=(login_usuario, accion, fecha_hora))

        conexion.close()