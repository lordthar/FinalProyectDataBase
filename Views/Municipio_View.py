import tkinter as tk
from tkinter import ttk, messagebox

from Conexion import CConexion
from Modelo.Municipio import Municipio  # Importamos la clase Municipio

class MunicipiosFrame(tk.Frame):
    def __init__(self, master=None, conection=None):
        super().__init__(master)
        self.master = master
        self.conection = conection
        self.create_widgets()

    def create_widgets(self):
        inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        inner_frame.pack(padx=100, pady=50)

        style = ttk.Style()
        style.configure('TLabel', background='#f0f0f0', foreground='#333333', font=('Arial', 12))
        style.configure('TEntry', background='#ffffff', foreground='#333333', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10), width=10)

        lbl_title = tk.Label(inner_frame, text="Municipios", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(inner_frame, text="Código Municipio:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        lbl_id = ttk.Label(inner_frame, text="ID Profesion:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Municipio.obtener_codigos_municipio(self.conection)

        self.entry_codigo = ttk.Entry(inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(inner_frame, text="Nombre Municipio:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = ttk.Entry(inner_frame, width=20)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_poblacion = ttk.Label(inner_frame, text="Población Municipio:")
        lbl_poblacion.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_poblacion = ttk.Entry(inner_frame, width=20)
        self.entry_poblacion.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        lbl_departamento = ttk.Label(inner_frame, text="Departamento:")
        lbl_departamento.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_departamento = ttk.Combobox(inner_frame, width=18)
        self.combobox_departamento.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.combobox_departamento['values'] = Municipio.obtener_departamentos(self.conection)

        lbl_tipo_municipio = ttk.Label(inner_frame, text="Tipo de Municipio:")
        lbl_tipo_municipio.grid(row=5, column=0, padx=10, pady=10, sticky="e")

        self.combobox_tipo_municipio = ttk.Combobox(inner_frame, width=18)
        self.combobox_tipo_municipio.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.combobox_tipo_municipio['values'] = Municipio.obtener_tipos_municipio(self.conection)

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton', command=self.crear_registro)
        btn_crear.grid(row=6, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton', command= self.eliminarRegistros)
        btn_eliminar.grid(row=6, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton',command=self.actualizarRegistros)
        btn_actualizar.grid(row=6, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton', command= self.buscarRegistros)
        btn_buscar.grid(row=6, column=3, padx=5, pady=20, sticky="we")

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")
    def crear_registro(self):
        try:
            codigo_municipio = self.entry_codigo.get()
            nombre_municipio = self.entry_nombre.get()
            poblacion_municipio = self.entry_poblacion.get()
            nombre_departamento = self.combobox_departamento.get()
            nombre_tipo_municipio = self.combobox_tipo_municipio.get()

            if not codigo_municipio or not nombre_municipio or not poblacion_municipio or not nombre_departamento or not nombre_tipo_municipio:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return

            conection = CConexion.ConexionBasedeDatos()
            codigo_departamento = Municipio.obtener_codigo_departamento_seleccionado(conection, nombre_departamento)
            codigo_tipo_municipio = Municipio.obtener_codigo_tipo_municipio_seleccionado(conection, nombre_tipo_municipio)

            if not codigo_departamento or not codigo_tipo_municipio:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para el departamento o el tipo de municipio.")
                return

            Municipio.ingresarMunicipio(codigo_municipio, nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio)
            messagebox.showinfo("Registrado", "Municipio Registrado exitosamente")

            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_poblacion.delete(0, tk.END)
            self.combobox_departamento.set('')
            self.combobox_tipo_municipio.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminarRegistros(self):
        try:
            codigo_municipio = self.combobox_id.get()

            if not codigo_municipio:
                messagebox.showinfo("Error", "Por favor, ingrese el código del municipio que desea eliminar")
                return

            confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar este municipio?")
            if confirmacion:
                Municipio.eliminarMunicipio(codigo_municipio)
                messagebox.showinfo("Eliminado", "Municipio eliminado exitosamente")

                self.entry_codigo.delete(0, tk.END)
                self.entry_nombre.delete(0, tk.END)
                self.entry_poblacion.delete(0, tk.END)
                self.combobox_departamento.set('')
                self.combobox_tipo_municipio.set('')
        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizarRegistros(self):
        try:
            codigo_municipio = self.combobox_id.get()
            nombre_municipio = self.entry_nombre.get()
            poblacion_municipio = self.entry_poblacion.get()
            codigo_departamento = self.combobox_departamento.get()
            codigo_tipo_municipio = self.combobox_tipo_municipio.get()

            if not codigo_municipio:
                messagebox.showinfo("Error", "Por favor, ingrese el código del municipio que desea actualizar")
                return


            conection = CConexion.ConexionBasedeDatos()
            codigo_departamento = Municipio.obtener_codigo_departamento_seleccionado(conection, codigo_departamento)
            codigo_tipo_municipio = Municipio.obtener_codigo_tipo_municipio_seleccionado(conection, codigo_tipo_municipio)
            Municipio.actualizarMunicipio(codigo_municipio, nombre_municipio, poblacion_municipio, codigo_departamento, codigo_tipo_municipio)
            messagebox.showinfo("Actualizado", "Municipio actualizado exitosamente")

            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_poblacion.delete(0, tk.END)
            self.combobox_id.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscarRegistros(self):
        try:
            codigo_municipio = self.combobox_id.get()

            if not codigo_municipio:
                messagebox.showinfo("Error", "Por favor, ingrese el código del municipio que desea buscar")
                return

            municipio = Municipio.buscarMunicipio(codigo_municipio)
            if municipio:
                messagebox.showinfo("Información", f"Nombre: {municipio[1]}, Población: {municipio[2]}, Código de Departamento: {municipio[3]}, Código de Tipo de Municipio: {municipio[4]}")
            else:
                messagebox.showinfo("No encontrado", "No se encontró ningún municipio con el código proporcionado")
        except ValueError as error:
            messagebox.showinfo("Error", str(error))
