import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Modelo.Tipo_Municipio import Tipo_Municipio
from Conexion import *

class TipoMunicipio_Frame(tk.Frame):
    def __init__(self, master=None, conection = None):
        super().__init__(master)
        self.master = master
        self.entry_codigo = None
        self.entry_nombre = None
        self.inner_frame = None
        self.conexion = conection
        self.create_formulario()

    def create_formulario(self):
        self.inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.inner_frame.pack(padx=100, pady=100)

        style = ttk.Style()
        style.configure('TLabel', background='#f0f0f0', foreground='#333333', font=('Arial', 12))
        style.configure('TEntry', background='#ffffff', foreground='#333333', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10), width=10)

        lbl_title = tk.Label(self.inner_frame, text="Tipo Municipio", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(self.inner_frame, text="Código del Tipo Municipio:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_codigo = ttk.Entry(self.inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_id = ttk.Label(self.inner_frame, text="ID Tipo Municipio:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(self.inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Tipo_Municipio.obtener_ids_tipo_municipio(self.conexion)

        lbl_nombre = ttk.Label(self.inner_frame, text="Nombre del Tipo Municipio:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = ttk.Entry(self.inner_frame, width=20)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

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
            codigo_Tipo_Municipio = self.entry_codigo.get()
            nombre_Municipio = self.entry_nombre.get()

            if not codigo_Tipo_Municipio or not nombre_Municipio:
                messagebox.showinfo("Error", "Por favor, Ingrese el codigo del Tipo de Municipio y el nombre del mismo")
                return

            Tipo_Municipio.ingresarTipo_Municipio(codigo_Tipo_Municipio, nombre_Municipio)
            messagebox.showinfo("Registrado", "Tipo de Municipio Registrado exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.entry_codigo.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminarRegistros(self):
        try:
            combobox_ids = self.combobox_id.get()

            if not combobox_ids:
                messagebox.showinfo("Error", "Por favor, Ingrese el código del Tipo de Municipio")
                return

            Tipo_Municipio.eliminarTipo_Municipio(combobox_ids)
            messagebox.showinfo("Eliminado", "Tipo de Municipio Eliminado exitosamente")

            self.combobox_id.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizarRegistros(self):
        try:
            combobox_ids = self.combobox_id.get()
            nombre_Municipio = self.entry_nombre.get()

            if not combobox_ids or not nombre_Municipio:
                messagebox.showinfo("Error", "Por favor, Ingrese el código y nombre del Tipo de Municipio")
                return

            Tipo_Municipio.actualizarTipo_Municipio(combobox_ids, nombre_Municipio)
            messagebox.showinfo("Actualizado", "Tipo de Municipio Actualizado exitosamente")

            self.combobox_id.set('')
            self.entry_nombre.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscarRegistros(self):
        try:
            combobox_ids = self.combobox_id.get()

            if not combobox_ids:
                messagebox.showinfo("Error", "Por favor, Ingrese el código del Tipo de Municipio")
                return

            tipo_municipio = Tipo_Municipio.buscarTipo_Municipio(combobox_ids)
            if tipo_municipio:
                self.entry_nombre.delete(0, tk.END)
                self.entry_nombre.insert(0, tipo_municipio[1])
                messagebox.showinfo("Encontrado", f"Tipo_Municipio: {tipo_municipio[1]}")
            else:
                messagebox.showinfo("No Encontrado", "No se encontró el Tipo de Municipio con el código proporcionado")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))
