import tkinter as tk
from tkinter import ttk

class SucursalFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
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
        entry_codigo = ttk.Entry(inner_frame)
        entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(inner_frame, text="Nombre de Sucursal:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        entry_nombre = ttk.Entry(inner_frame)
        entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_ubicacion = ttk.Label(inner_frame, text="Ubicación:")
        lbl_ubicacion.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        entry_departamento = ttk.Entry(inner_frame, width=15)
        entry_departamento.grid(row=3, column=1, padx=5, pady=10, sticky="w")
        entry_municipio = ttk.Entry(inner_frame, width=15)
        entry_municipio.grid(row=3, column=2, padx=5, pady=10, sticky="w")

        lbl_director = ttk.Label(inner_frame, text="Director de Sucursal:")
        lbl_director.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        entry_director = ttk.Entry(inner_frame)
        entry_director.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        lbl_presupuesto = ttk.Label(inner_frame, text="Presupuesto Anual:")
        lbl_presupuesto.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        entry_presupuesto = ttk.Entry(inner_frame)
        entry_presupuesto.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton')
        btn_crear.grid(row=6, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton')
        btn_eliminar.grid(row=6, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton')
        btn_actualizar.grid(row=6, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton')
        btn_buscar.grid(row=6, column=3, padx=5, pady=20, sticky="we")

        style.map('TButton.TButton',
                  background=[('active', '#448aff'), ('pressed', '#2979ff')],
                  foreground=[('active', 'black'), ('pressed', 'black')])

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")