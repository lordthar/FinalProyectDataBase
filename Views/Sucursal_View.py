import tkinter as tk
from tkinter import ttk, messagebox
from Modelo.Sucursal import *

class SucursalFrame(tk.Frame):
    def __init__(self, master=None, conection=None):
        super().__init__(master)
        self.master = master
        self.conection = conection
        self.create_formulario()

    def create_formulario(self):
        inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        inner_frame.pack(padx=50, pady=50, ipadx=50, ipady=50)

        style = ttk.Style()
        style.configure('TLabel', background='#f0f0f0', foreground='#333333', font=('Arial', 12))
        style.configure('TEntry', background='#ffffff', foreground='#333333', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10), width=10)

        lbl_title = tk.Label(inner_frame, text="Sucursal", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(inner_frame, text="Código de Sucursal:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_codigo = ttk.Entry(inner_frame)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_id = ttk.Label(inner_frame, text="ID Profesion:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Sucursal.obtener_codigos_sucursal(self.conection)

        lbl_nombre = ttk.Label(inner_frame, text="Nombre de Sucursal:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_nombre = ttk.Entry(inner_frame)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_ubicacion = ttk.Label(inner_frame, text="Ubicación Sucursal:")
        lbl_ubicacion.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_ubicacion = ttk.Entry(inner_frame, width=15)
        self.entry_ubicacion.grid(row=3, column=1, padx=5, pady=10, sticky="w")

        lbl_telefono = ttk.Label(inner_frame, text="Telefono Sucursal")
        lbl_telefono.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry_telefono = ttk.Entry(inner_frame)
        self.entry_telefono.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        lbl_municipio = ttk.Label(inner_frame, text="Municipio Sucursal:")
        lbl_municipio.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.combobox_municipio = ttk.Combobox(inner_frame, width=18)
        self.combobox_municipio.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.combobox_municipio['values'] = Sucursal.obtener_municipio(self.conection)

        lbl_departamento = ttk.Label(inner_frame, text="Departamento Sucursal :")
        lbl_departamento.grid(row=6, column=0, padx=10, pady=10, sticky="e")

        self.combobox_departamento = ttk.Combobox(inner_frame, width=18)
        self.combobox_departamento.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.combobox_departamento['values'] = Sucursal.obtener_departamentos(self.conection)

        lbl_presupuesto = ttk.Label(inner_frame, text="Presupuesto Sucursal:")
        lbl_presupuesto.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        self.entry_presupuesto = ttk.Entry(inner_frame)
        self.entry_presupuesto.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton', command= self.crear_registro)
        btn_crear.grid(row=8, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton', command= self.eliminar_registro)
        btn_eliminar.grid(row=8, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton', command= self.actualizar_registro)
        btn_actualizar.grid(row=8, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton', command=self.buscar_registro)
        btn_buscar.grid(row=8, column=3, padx=5, pady=20, sticky="we")

        style.map('TButton.TButton',
                  background=[('active', '#448aff'), ('pressed', '#2979ff')],
                  foreground=[('active', 'black'), ('pressed', 'black')])

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crear_registro(self):
        try:
            codigo_sucursal = self.entry_codigo.get()
            nombre_sucursal = self.entry_nombre.get()
            direccion_sucursal = self.entry_ubicacion.get()
            telefono_sucursal = self.entry_telefono.get()
            nombre_municipio = self.combobox_municipio.get()
            nombre_departamento = self.combobox_departamento.get()
            sucursal_presupuesto = self.entry_presupuesto.get()

            if not codigo_sucursal or not nombre_sucursal or not direccion_sucursal or not telefono_sucursal or not nombre_municipio or not nombre_departamento or not sucursal_presupuesto:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return

            conection = CConexion.ConexionBasedeDatos()
            codigo_municipio = Sucursal.obtener_codigo_municipio_seleccionado(conection, nombre_municipio)
            codigo_departamento = Sucursal.obtener_codigo_departamento_seleccionado(conection, nombre_departamento)

            if not codigo_municipio or not codigo_departamento:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para el municipio o el departamento.")
                return

            Sucursal.ingresarSucursal(codigo_sucursal, nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto)
            messagebox.showinfo("Registrado", "Sucursal registrada exitosamente")

            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_ubicacion.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.combobox_municipio.set('')
            self.combobox_departamento.set('')
            self.entry_presupuesto.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminar_registro(self):
        try:
            codigo_sucursal = self.combobox_id.get()

            if not codigo_sucursal:
                messagebox.showinfo("Error", "Por favor ingrese el código de la sucursal a eliminar.")
                return

            conection = CConexion.ConexionBasedeDatos()
            success = Sucursal.eliminarSucursal(codigo_sucursal)

            if success:
                messagebox.showinfo("Eliminado", "Sucursal eliminada exitosamente")
                self.combobox_id.set('')
            else:
                messagebox.showinfo("Error", "No se pudo eliminar la sucursal. Verifique el código ingresado.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizar_registro(self):
        try:
            codigo_sucursal = self.combobox_id.get()
            nombre_sucursal = self.entry_nombre.get()
            direccion_sucursal = self.entry_ubicacion.get()
            telefono_sucursal = self.entry_telefono.get()
            nombre_municipio = self.combobox_municipio.get()
            nombre_departamento = self.combobox_departamento.get()
            sucursal_presupuesto = self.entry_presupuesto.get()

            if not codigo_sucursal:
                messagebox.showinfo("Error", "Por favor ingrese el código de la sucursal a actualizar.")
                return

            conection = CConexion.ConexionBasedeDatos()
            codigo_municipio = Sucursal.obtener_codigo_municipio_seleccionado(conection, nombre_municipio)
            codigo_departamento = Sucursal.obtener_codigo_departamento_seleccionado(conection, nombre_departamento)

            if not codigo_municipio or not codigo_departamento:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para el municipio o el departamento.")
                return

            success = Sucursal.actualizarSucursal(codigo_sucursal, nombre_sucursal, direccion_sucursal, telefono_sucursal, codigo_municipio, codigo_departamento, sucursal_presupuesto)

            if success:
                messagebox.showinfo("Actualizado", "Sucursal actualizada exitosamente")
                self.combobox_id.set('')
                self.entry_nombre.delete(0, tk.END)
                self.entry_ubicacion.delete(0, tk.END)
                self.entry_telefono.delete(0, tk.END)
                self.combobox_municipio.set('')
                self.combobox_departamento.set('')
                self.entry_presupuesto.delete(0, tk.END)
            else:
                messagebox.showinfo("Error", "No se pudo actualizar la sucursal. Verifique los datos ingresados.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscar_registro(self):
        try:
            codigo_sucursal = self.combobox_id.get()

            if not codigo_sucursal:
                messagebox.showinfo("Error", "Por favor ingrese el código de la sucursal a buscar.")
                return

            sucursal = Sucursal.buscarSucursal(codigo_sucursal)

            if sucursal:
                message = (
                    f"Nombre: {sucursal[1]}\n"
                    f"Ubicación: {sucursal[2]}\n"
                    f"Teléfono: {sucursal[3]}\n"
                    f"Municipio: {sucursal[4]}\n"
                    f"Departamento: {sucursal[5]}\n"
                    f"Presupuesto: {sucursal[6]}"
                )
                messagebox.showinfo("Información de la Sucursal", message)
            else:
                messagebox.showinfo("Error", "No se encontró ninguna sucursal con el código proporcionado.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))