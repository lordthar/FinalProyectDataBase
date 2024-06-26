import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Modelo.Departamento import *
from Conexion import *

class DepartamentosFrame(tk.Frame):
    def __init__(self, master=None, conection=None):
        super().__init__(master)
        self.master = master
        self.entry_codigo = None
        self.entry_nombre = None
        self.entry_poblacion = None
        self.conection = conection
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

        lbl_id = ttk.Label(self.inner_frame, text="ID Departamento:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(self.inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Departamento.obtener_ids_departamento(self.conection)

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

        btn_eliminar = ttk.Button(self.inner_frame, text="Eliminar", style='TButton.TButton', command=self.eliminarRegistros)
        btn_eliminar.grid(row=4, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(self.inner_frame, text="Actualizar", style='TButton.TButton', command=self.actualizarRegistros)
        btn_actualizar.grid(row=4, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(self.inner_frame, text="Buscar", style='TButton.TButton', command=self.buscarRegistros)
        btn_buscar.grid(row=4, column=3, padx=5, pady=20, sticky="we")

        self.inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crearRegistros(self):
        try:
            codigo_departamento = self.entry_codigo.get()
            nombre_departamento = self.entry_nombre.get()
            poblacion_departamento = self.entry_poblacion.get()


            if not codigo_departamento or not nombre_departamento or not poblacion_departamento:
                messagebox.showinfo("Error", "Por favor, Ingrese el codigo del departamento, el nombre del mismo  y poblacion del departamento")
                return

            Departamento.ingresarDeptos(codigo_departamento, nombre_departamento, poblacion_departamento)
            messagebox.showinfo("Registrado", "Departamento Registrado exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.entry_poblacion.delete(0, tk.END)
            self.entry_codigo.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminarRegistros(self):
        try:
            combobox_ids = self.combobox_id.get()

            if not combobox_ids:
                messagebox.showinfo("Error", "Por favor, Ingrese el codigo del departamento")
                return

            Departamento.eliminarDeptos(combobox_ids)
            messagebox.showinfo("Eliminado", "Departamento Eliminado exitosamente")

            self.combobox_id.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizarRegistros(self):
        try:
            combobox_ids = self.combobox_id.get()
            nombre_departamento = self.entry_nombre.get()
            poblacion_departamento = self.entry_poblacion.get()

            if not combobox_ids or not nombre_departamento or not poblacion_departamento:
                messagebox.showinfo("Error", "Por favor, Ingrese el codigo del departamento, el nombre del mismo  y poblacion del departamento")
                return

            Departamento.actualizarDeptos(combobox_ids, nombre_departamento, poblacion_departamento)
            messagebox.showinfo("Actualizado", "Departamento Actualizado exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.entry_poblacion.delete(0, tk.END)
            self.entry_codigo.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))


    def buscarRegistros(self):
        try:
            combobox_ids = self.combobox_id.get()

            if not combobox_ids:
                messagebox.showinfo("Error", "Por favor, Ingrese el codigo del departamento")
                return

            departamento = Departamento.buscarDeptos(combobox_ids)
            if departamento:
                messagebox.showinfo("Información", f"Nombre: {departamento[1]}, Población: {departamento[2]}")
            else:
                messagebox.showinfo("No encontrado", "No se encontró el departamento con el código especificado")

                self.combobox_id.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))


