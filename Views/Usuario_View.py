import tkinter as tk
from tkinter import ttk, messagebox
from Modelo.Usuario import Usuario


class UsuarioFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entry_codigo = None
        self.entry_login = None
        self.entry_password = None
        self.entry_level= None
        self.inner_frame = None
        self.create_formulario()

    def create_formulario(self):

        self.inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.inner_frame.pack(padx=50, pady=50, ipadx=50, ipady=50)

        lbl_title = tk.Label(self.inner_frame, text="Usuarios", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(self.inner_frame, text="Código Usuario:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        entry_codigo = ttk.Entry(self.inner_frame, width=20)
        entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

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

        self.entry_level = ttk.Entry(self.inner_frame, width=20)
        self.entry_level.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(self.inner_frame, text="Crear", command=self.crearUsuario)
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(self.inner_frame, text="Eliminar")
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(self.inner_frame, text="Actualizar")
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(self.inner_frame, text="Buscar")
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        self.inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crearUsuario(self):
        try:
            login_user = self.entry_login.get()
            password_user = self.entry_password.get()
            level_user = self.entry_level.get()

            if not login_user or not password_user or not level_user:
                messagebox.showinfo("Error", "Por favor, llene los campos de usuario, password y level")
                return

            Usuario.ingresarUser(login_user, password_user, level_user)
            messagebox.showinfo("Registrado", "¡Usuario registrado exitosamente!")

            self.entry_login.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.entry_level.delete(0, tk.END)

        except Exception as error:
            messagebox.showinfo("Error", "Error al crear usuario: {}".format(str(error)))