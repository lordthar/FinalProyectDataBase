import tkinter as tk
from tkinter import ttk, messagebox
from Modelo.Cargo import Cargo


class CargosFrame(tk.Frame):
    def __init__(self, master=None, conection=None):
        super().__init__(master)
        self.master = master
        self.conexion = conection
        self.create_formulario()

    def create_formulario(self):
        inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        inner_frame.pack(padx=100, pady=50)

        style = ttk.Style()
        style.configure('TLabel', background='#f0f0f0', foreground='#333333', font=('Arial', 12))
        style.configure('TEntry', background='#ffffff', foreground='#333333', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10), width=10)

        lbl_title = tk.Label(inner_frame, text="Cargos", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(inner_frame, text="Código Cargo:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        lbl_id = ttk.Label(inner_frame, text="ID Cargo:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Cargo.obtener_codigos_Cargo(self.conexion)

        self.entry_codigo = ttk.Entry(inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(inner_frame, text="Nombre Cargo:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = ttk.Entry(inner_frame, width=20)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_salario = ttk.Label(inner_frame, text="Salario Cargo:")
        lbl_salario.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_salario = ttk.Entry(inner_frame, width=20)
        self.entry_salario.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton', command=self.crear_registro)
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton', command= self.eliminarRegistros)
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton', command=self.actualizarRegistros)
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton', command=self.buscarRegistros)
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crear_registro(self):
        try:
            codigo_cargo = self.entry_codigo.get()
            nombre_cargo = self.entry_nombre.get()
            salario_cargo = self.entry_salario.get()

            if not codigo_cargo or not nombre_cargo or not salario_cargo:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return


            Cargo.ingresarCargos(codigo_cargo, nombre_cargo, salario_cargo)
            messagebox.showinfo("Registrado", "Cargo Registrado exitosamente")

            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_salario.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminarRegistros(self):
        try:
            codigo_cargo = self.combobox_id.get()

            if not codigo_cargo:
                messagebox.showinfo("Error", "Por favor, Ingrese el código del Cargo")
                return

            Cargo.eliminarCargo(codigo_cargo, self.conexion)
            messagebox.showinfo("Eliminado", "Cargo Eliminado exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.entry_salario.delete(0, tk.END)
            self.combobox_id.set("")


        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizarRegistros(self):
        try:
            codigo_cargo = self.combobox_id.get()
            nombre_cargo = self.entry_nombre.get()
            salario_cargo = self.entry_salario.get()

            if not codigo_cargo or not nombre_cargo or not salario_cargo:
                messagebox.showinfo("Error", "Por favor, Ingrese todos los datos del Cargo")
                return

            Cargo.actualizarCargo(codigo_cargo, nombre_cargo, salario_cargo, self.conexion)
            messagebox.showinfo("Actualizado", "Cargo Actualizado exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.entry_salario.delete(0, tk.END)
            self.combobox_id.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscarRegistros(self):
        try:
            codigo_cargo = self.combobox_id.get()

            if not codigo_cargo:
                messagebox.showinfo("Error", "Por favor, Ingrese el código del Cargo")
                return

            cargo = Cargo.buscarCargo(codigo_cargo, self.conexion)
            if cargo:
                message = (
                    f"Código Cargo: {cargo[0]}\n"
                    f"Nombre: {cargo[1]}\n"
                    f"Salario: {cargo[2]}"
                )
                messagebox.showinfo("Información del Cargo", message)
            else:
                messagebox.showinfo("No encontrado", "No se encontró ningún Cargo con el código proporcionado.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))