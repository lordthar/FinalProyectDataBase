import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Modelo.Departamento import *
from Conexion import *

class DepartamentosFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entry_codigo = None
        self.entry_nombre = None
        self.entry_poblacion = None
        self.inner_frame = None
        self.create_formulario()

    def create_formulario(self):
        self.inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.inner_frame.pack(padx=100, pady=100)

        style = ttk.Style()
        style.configure('TLabel', background='#f0f0f0', foreground='#333333', font=('Arial', 12))
        style.configure('TEntry', background='#ffffff', foreground='#333333', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10), width=10)

        lbl_title = tk.Label(self.inner_frame, text="Departamentos", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(self.inner_frame, text="Código Departamento:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_codigo = ttk.Entry(self.inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(self.inner_frame, text="Nombre Departamento:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = ttk.Entry(self.inner_frame, width=20)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_poblacion = ttk.Label(self.inner_frame, text="Población Departamento:")
        lbl_poblacion.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_poblacion = ttk.Entry(self.inner_frame, width=20)
        self.entry_poblacion.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(self.inner_frame, text="Crear", style='TButton.TButton', command=self.crearRegistros)
        btn_crear.grid(row=4, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(self.inner_frame, text="Eliminar", style='TButton.TButton', command=self.eliminarRegistro)
        btn_eliminar.grid(row=4, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(self.inner_frame, text="Actualizar", style='TButton.TButton')
        btn_actualizar.grid(row=4, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(self.inner_frame, text="Buscar", style='TButton.TButton')
        btn_buscar.grid(row=4, column=3, padx=5, pady=20, sticky="we")

        self.inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crearRegistros(self):
        try:
            nombre_departamento = self.entry_nombre.get()
            poblacion_departamento = self.entry_poblacion.get()

            if not nombre_departamento or not poblacion_departamento:
                messagebox.showinfo("Error", "Por favor, Ingrese el nombre y poblacion del departamento")
                return

            Departamento.ingresarDeptos(nombre_departamento, poblacion_departamento)
            messagebox.showinfo("Registrado", "Departamento Registrado exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.entry_poblacion.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminarRegistro(self):
        try:
            codigo_deparamento= self.entry_codigo.get()

            if not codigo_deparamento:
                messagebox.showinfo("Error", "Ingresar Codigo Departamento")
                return
            Departamento.eliminarDatos(codigo_deparamento)
            messagebox.showinfo("Eliminado", "Departamento Eliminado Correctamente")

            self.entry_codigo.delete(0,tk.END)
        except ValueError as error:
            messagebox.showinfo("Error", str(error))

