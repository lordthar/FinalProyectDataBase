import tkinter as tk
from tkinter import messagebox

class PopupAyudaAplicacion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acerca de")

        self.geometry("750x250")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        info_label = tk.Label(self, text="¿Te surgio alguna duda?")
        info_label.pack(padx=20, pady=(20, 10))

        about_label = tk.Label(self, text="No te preocupes Estamos aqui para ayudarte")
        about_label.pack(padx=20, pady=5, anchor="w")

        authors_label = tk.Label(self, text="Desarrolladores: Huendy Caicedo T. y Miguel Angel Garcia Osorio")
        authors_label.pack(padx=20, pady=5, anchor="w")

        contact_label = tk.Label(self, text="¿Tienes alguna pregunta o sugerencia? Contáctanos en: miguela.garciao@uqvirtual.edu.co y huendy.caidedot@uqvirtual.edu.co")
        contact_label.pack(padx=20, pady=5, anchor="w")

        faq_label = tk.Label(self, text="Para obtener respuestas a preguntas frecuentes, visitanos en el salon donde este el Profesor orlando dictando bases de datos 1")
        faq_label.pack(padx=20, pady=5, anchor="w")

        close_button = tk.Button(self, text="Aceptar", command=self.destroy)
        close_button.pack(padx=20, pady=(10, 20))