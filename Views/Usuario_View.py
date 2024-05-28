import tkinter as tk
from tkinter import ttk, messagebox
from Modelo.Usuario import Usuario


class UsuarioFrame(tk.Frame):
    def __init__(self, master=None, conection= None):
        super().__init__(master)
        self.master = master
        self.entry_codigo = None
        self.entry_login = None
        self.entry_password = None
        self.entry_level= None
        self.inner_frame = None
        self.conection = conection
        self.create_formulario()

    def create_formulario(self):

        self.inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.inner_frame.pack(padx=50, pady=50, ipadx=50, ipady=50)

        lbl_title = tk.Label(self.inner_frame, text="Usuarios", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(self.inner_frame, text="Código Usuario:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_codigo = ttk.Entry(self.inner_frame, width=20)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_id = ttk.Label(self.inner_frame, text="ID Users:")
        lbl_id.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.combobox_id = ttk.Combobox(self.inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Usuario.obtener_codigos_users(self.conection)

        lbl_login = ttk.Label(self.inner_frame, text="Login Usuario:")
        lbl_login.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_login = ttk.Entry(self.inner_frame, width=20)
        self.entry_login.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_password = ttk.Label(self.inner_frame, text="Password Usuario:")
        lbl_password.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = ttk.Entry(self.inner_frame, width=20)
        self.entry_password.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        lbl_level = ttk.Label(self.inner_frame, text="Level Usuario:")
        lbl_level.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        options = ["Principal", "Paramétrico", "Esporádico"]
        self.entry_level = ttk.Combobox(self.inner_frame, width=20, values=options)
        self.entry_level.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(self.inner_frame, text="Crear", command=self.crearUsuario)
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(self.inner_frame, text="Eliminar", command=self.eliminar_registro)
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(self.inner_frame, text="Actualizar", command= self.actualizar_registro)
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(self.inner_frame, text="Buscar", command=self.buscar_registro)
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        self.inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crearUsuario(self):
        try:
            login_user = self.entry_login.get()
            password_user = self.entry_password.get()
            level_user = self.entry_level.get()
            codigo_usuario = self.entry_codigo.get()

            if not codigo_usuario or not login_user or not password_user or not level_user:
                messagebox.showinfo("Error", "Por favor, llene los campos de codigo, usuario, password y level")
                return

            Usuario.ingresarUser(codigo_usuario, login_user, password_user, level_user)
            messagebox.showinfo("Registrado", "¡Usuario registrado exitosamente!")

            self.entry_codigo.delete(0, tk.END)
            self.entry_login.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.entry_level.delete(0, tk.END)

        except Exception as error:
            messagebox.showinfo("Error", "Error al crear usuario: {}".format(str(error)))

    def eliminar_registro(self):
        try:
            codigo_usuario = self.combobox_id.get()

            if not codigo_usuario:
                messagebox.showinfo("Error", "Por favor ingrese el código del usuario a eliminar.")
                return

            if messagebox.askyesno("Eliminar Usuario", "¿Está seguro de que desea eliminar este usuario?"):
                Usuario.eliminarUser(codigo_usuario)
                messagebox.showinfo("Eliminado", "Usuario eliminado exitosamente")

                self.combobox_id.set('')
                self.entry_login.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
                self.entry_level.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizar_registro(self):
        try:
            codigo_usuario = self.combobox_id.get()
            login_usuario = self.entry_login.get()
            password_usuario = self.entry_password.get()
            nivel_usuario = self.entry_level.get()

            if not codigo_usuario or not login_usuario or not password_usuario or not nivel_usuario:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return

            Usuario.actualizarUser(codigo_usuario, login_usuario, password_usuario, nivel_usuario)
            messagebox.showinfo("Actualizado", "Usuario actualizado exitosamente")

            self.combobox_id.set('')
            self.entry_login.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.entry_level.set('')

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscar_registro(self):
        try:
            codigo_usuario = self.combobox_id.get()

            if not codigo_usuario:
                messagebox.showinfo("Error", "Por favor ingrese el código del usuario a buscar.")
                return

            usuario = Usuario.buscarUser(codigo_usuario)

            if usuario:
                messagebox.showinfo("Usuario Encontrado",
                                    f"Código: {usuario[0]}\n"
                                    f"Login: {usuario[1]}\n"
                                    f"Contraseña: {usuario[2]}\n"
                                    f"Nivel: {usuario[3]}")
            else:
                messagebox.showinfo("Error", "No se encontró ningún usuario con el código proporcionado.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))