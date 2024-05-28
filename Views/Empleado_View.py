import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from Modelo.Empleado import Empleado
from Conexion import *

class VentanaEmpleado(tk.Frame):
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

        lbl_title = tk.Label(inner_frame, text="Empleado", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=(0, 20))

        lbl_codigo = ttk.Label(inner_frame, text="Código Empleado:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        lbl_id = ttk.Label(inner_frame, text="ID Empleado:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Empleado.obtener_codigos_empleado(self.conection)

        self.entry_codigo = ttk.Entry(inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_cedula = ttk.Label(inner_frame, text="Cédula Empleado:")
        lbl_cedula.grid(row=1, column=3, padx=10, pady=10, sticky="e")

        self.entry_cedula = ttk.Entry(inner_frame, width=20)
        self.entry_cedula.grid(row=1, column=4, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(inner_frame, text="Nombre Empleado:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = ttk.Entry(inner_frame, width=20)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_telefono = ttk.Label(inner_frame, text="Teléfono Empleado:")
        lbl_telefono.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        self.entry_telefono = ttk.Entry(inner_frame, width=20)
        self.entry_telefono.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        lbl_direccion = ttk.Label(inner_frame, text="Dirección Empleado:")
        lbl_direccion.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_direccion = ttk.Entry(inner_frame, width=20)
        self.entry_direccion.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        lbl_profesion = ttk.Label(inner_frame, text="Profesión Empleado:")
        lbl_profesion.grid(row=3, column=2, padx=10, pady=10, sticky="e")

        self.combo_profesion = ttk.Combobox(inner_frame, width=18)
        self.combo_profesion['values'] = Empleado.obtener_profesiones(self.conection)
        self.combo_profesion.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        genero_frame = tk.Frame(inner_frame, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        genero_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        lbl_genero = ttk.Label(genero_frame, text="Género Empleado:")
        lbl_genero.grid(row=0, column=0, padx=(10, 5), pady=10)

        self.genero_value = tk.StringVar()

        radio_masculino = ttk.Radiobutton(genero_frame, text="Masculino", variable=self.genero_value, value="Masculino")
        radio_masculino.grid(row=0, column=1, padx=(5, 15), pady=10)

        radio_femenino = ttk.Radiobutton(genero_frame, text="Femenino", variable=self.genero_value, value="Femenino")
        radio_femenino.grid(row=0, column=2, padx=5, pady=10)

        radio_otro = ttk.Radiobutton(genero_frame, text="Otro", variable=self.genero_value, value="Otro")
        radio_otro.grid(row=0, column=3, padx=(15, 10), pady=10)

        lbl_fecha_nacimiento = ttk.Label(inner_frame, text="Fecha de Nacimiento Empleado:")
        lbl_fecha_nacimiento.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="e")

        self.date_entry = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        self.date_entry.grid(row=5, column=1, padx=10, pady=(0, 10), sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton', command= self.crear_registro)
        btn_crear.grid(row=6, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton', command=self.eliminar_registro)
        btn_eliminar.grid(row=6, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton', command=self.actualizar_registro)
        btn_actualizar.grid(row=6, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton', command=self.buscar_registro)
        btn_buscar.grid(row=6, column=3, padx=5, pady=20, sticky="we")

        style.map('TButton.TButton',
                  background=[('active', '#448aff'), ('pressed', '#2979ff')],
                  foreground=[('active', 'black'), ('pressed', 'black')])

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crear_registro(self):
        try:
            codigo_empleado = self.entry_codigo.get()
            nombre_empleado = self.entry_nombre.get()
            telefono_empleado = self.entry_telefono.get()
            cedula_empleado = self.entry_cedula.get()
            direccion_empleado = self.entry_direccion.get()
            nombre_profesion = self.combo_profesion.get()
            genero_empleado = self.genero_value.get()
            fechaNTO_empleado = self.date_entry.get_date().strftime('%Y-%m-%d')

            if not cedula_empleado or not codigo_empleado or not nombre_empleado or not telefono_empleado or not direccion_empleado or not nombre_profesion or not genero_empleado or not fechaNTO_empleado:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return

            conection = CConexion.ConexionBasedeDatos()
            codigo_profesion = Empleado.obtener_codigo_profesion_seleccionada(conection, nombre_profesion)

            if not codigo_profesion:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para la profesión.")
                return

            Empleado.ingresarEmpleado(codigo_empleado, nombre_empleado, telefono_empleado,  cedula_empleado, direccion_empleado, codigo_profesion, genero_empleado, fechaNTO_empleado)
            messagebox.showinfo("Registrado", "Empleado registrado exitosamente")

            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_cedula.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_direccion.delete(0, tk.END)
            self.combo_profesion.set('')
            self.genero_value.set('')
            self.date_entry.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminar_registro(self):
        try:
            codigo_empleado = self.combobox_id.get()

            if not codigo_empleado:
                messagebox.showinfo("Error", "Ingrese el código del empleado a eliminar")
                return

            respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este registro?")
            if respuesta:
                Empleado.eliminarEmpleado(codigo_empleado)
                messagebox.showinfo("Eliminado", "Empleado eliminado exitosamente")

                self.combobox_id.set('')
                self.entry_nombre.delete(0, tk.END)
                self.entry_cedula.delete(0, tk.END)
                self.entry_telefono.delete(0, tk.END)
                self.entry_direccion.delete(0, tk.END)
                self.combo_profesion.set('')
                self.genero_value.set('')
                self.date_entry.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizar_registro(self):
        try:
            codigo_empleado = self.combobox_id.get()
            nombre_empleado = self.entry_nombre.get()
            telefono_empleado = self.entry_telefono.get()
            direccion_empleado = self.entry_direccion.get()
            nombre_profesion = self.combo_profesion.get()
            genero_empleado = self.genero_value.get()
            fechaNTO_empleado = self.date_entry.get_date().strftime('%Y-%m-%d')

            if not codigo_empleado:
                messagebox.showinfo("Error", "Ingrese el código del empleado a actualizar")
                return

            codigo_profesion = Empleado.obtener_codigo_profesion_seleccionada(self.conection, nombre_profesion)

            if not codigo_profesion:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para la profesión.")
                return

            Empleado.actualizarEmpleado(codigo_empleado, nombre_empleado, telefono_empleado, direccion_empleado, codigo_profesion, genero_empleado, fechaNTO_empleado)
            messagebox.showinfo("Actualizado", "Empleado actualizado exitosamente")

            self.combobox_id.set('')
            self.entry_nombre.delete(0, tk.END)
            self.entry_cedula.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_direccion.delete(0, tk.END)
            self.combo_profesion.set('')
            self.genero_value.set('')
            self.date_entry.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscar_registro(self):
        try:
            codigo_empleado = self.combobox_id.get()

            if not codigo_empleado:
                messagebox.showinfo("Error", "Por favor ingrese el código del empleado a buscar.")
                return

            empleado = Empleado.buscarEmpleado(codigo_empleado)

            if empleado:
                message = (
                    f"Código Empleado: {empleado[0]}\n"
                    f"Nombre: {empleado[1]}\n"
                    f"Teléfono: {empleado[2]}\n"
                    f"Dirección: {empleado[3]}\n"
                    f"Profesión: {empleado[4]}\n"
                    f"Género: {empleado[5]}\n"
                    f"Fecha de Nacimiento: {empleado[6]}"
                )
                messagebox.showinfo("Información del Empleado", message)
            else:
                messagebox.showinfo("Error", "No se encontró ningún empleado con el código proporcionado.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))
