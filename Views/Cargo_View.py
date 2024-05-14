import tkinter as tk
from tkinter import ttk

class CargosFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
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

        entry_codigo = ttk.Entry(inner_frame, width=20)
        entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(inner_frame, text="Nombre Cargo:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        entry_nombre = ttk.Entry(inner_frame, width=20)
        entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_salario = ttk.Label(inner_frame, text="Salario Cargo:")
        lbl_salario.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        entry_salario = ttk.Entry(inner_frame, width=20)
        entry_salario.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton')
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton')
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton')
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton')
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")