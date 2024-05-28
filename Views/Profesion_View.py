import tkinter as tk
from tkinter import ttk, messagebox
from Modelo.Profesion import Profesion

class ProfesionesFrame(tk.Frame):
    def __init__(self, master=None, conection= None):
        super().__init__(master)
        self.master = master
        self.conection = conection
        self.create_formulario()

    def create_formulario(self):
        inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        inner_frame.pack(padx=100, pady=50)

        style = ttk.Style()
        style.configure('TLabel', background='#f0f0f0', foreground='#333333', font=('Arial', 12))
        style.configure('TEntry', background='#ffffff', foreground='#333333', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10), width=10)

        lbl_title = tk.Label(inner_frame, text="Profesiones", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0,pady=(0, 20))

        lbl_codigo = ttk.Label(inner_frame, text="Código Profesión:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_codigo = ttk.Entry(inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_id = ttk.Label(inner_frame, text="ID Profesion:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Profesion.obtener_codigos_Profesion(self.conection)

        lbl_nombre = ttk.Label(inner_frame, text="Nombre Profesión:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = ttk.Entry(inner_frame, width=20)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton',command= self.crear_registro)
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton', command= self.eliminarRegistros)
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton', command= self.actualizarRegistros)
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton', command= self.buscarRegistros)
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crear_registro(self):
        try:
            codigo_profesion = self.entry_codigo.get()
            nombre_profesion = self.entry_nombre.get()

            if not codigo_profesion or not nombre_profesion:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return


            Profesion.ingresarProfesion(codigo_profesion, nombre_profesion)
            messagebox.showinfo("Registrado", "Profesión Registrada exitosamente")

            self.entry_codigo.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminarRegistros(self):
        try:
            codigo_profesion = self.combobox_id.get()

            if not codigo_profesion:
                messagebox.showinfo("Error", "Por favor, Ingrese el código de la Profesión")
                return

            Profesion.eliminarProfesion(codigo_profesion)
            messagebox.showinfo("Eliminado", "Profesión Eliminada exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.combobox_id.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizarRegistros(self):
        try:
            codigo_profesion = self.combobox_id.get()
            nombre_profesion = self.entry_nombre.get()

            if not codigo_profesion or not nombre_profesion:
                messagebox.showinfo("Error", "Por favor, Ingrese todos los datos de la Profesión")
                return

            Profesion.actualizarProfesion(codigo_profesion, nombre_profesion)
            messagebox.showinfo("Actualizado", "Profesión Actualizada exitosamente")

            self.entry_nombre.delete(0, tk.END)
            self.combobox_id.set('')


        except ValueError as error:
            messagebox.showinfo("Error", str(error))


    def buscarRegistros(self):
        try:
            codigo_profesion = self.combobox_id.get()

            if not codigo_profesion:
                messagebox.showinfo("Error", "Por favor, Ingrese el código de la Profesión")
                return

            profesion = Profesion.buscarProfesion(codigo_profesion)
            if profesion:
                message = (
                    f"Código Profesión: {profesion[0]}\n"
                    f"Nombre: {profesion[1]}"
                )
                messagebox.showinfo("Información de la Profesión", message)
            else:
                messagebox.showinfo("No encontrado", "No se encontró la Profesión con el código especificado")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))
