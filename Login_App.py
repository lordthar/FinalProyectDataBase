import tkinter as tk
from tkinter import ttk, messagebox
from AppBancoUQ.App import BancoUQApp
from Modelo.Usuario import Usuario

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Framed.TFrame", background="#f0f0f0", borderwidth=5, relief="sunken")
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))

        main_frame = ttk.Frame(self, style="Framed.TFrame")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_label = ttk.Label(main_frame, text="Inicio de Sesión", style="Title.TLabel")
        title_label.grid(row=0, columnspan=2, pady=10)

        self.username_label = ttk.Label(main_frame, text="Usuario:", font=("Arial", 12))
        self.password_label = ttk.Label(main_frame, text="Contraseña:", font=("Arial", 12))
        self.username_entry = ttk.Entry(main_frame, font=("Arial", 12))
        self.password_entry = ttk.Entry(main_frame, show="*", font=("Arial", 12))
        self.login_button = ttk.Button(main_frame, text="Iniciar sesión", command=self.login)

        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.login_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")



    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        nivel_usuario = Usuario.obtener_nivel_acceso(username)
        if not username or not password:
            messagebox.showinfo("Alerta", "Por favor, ingrese el nombre de usuario y la contraseña")
            return

        if Usuario.verificar_login(username, password, nivel_usuario):
            messagebox.showinfo("Acceso Correcto", "¡Bienvenido de nuevo!, tu nivel de acceso es: " + nivel_usuario)
            self.destroy()
            root = tk.Tk()
            root.title("BancoUQ")
            BancoUQApp(root, nivel_usuario)
            root.mainloop()
        else:
            messagebox.showinfo("Acceso Denegado", "Nombre de usuario o contraseña incorrectos")


if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
