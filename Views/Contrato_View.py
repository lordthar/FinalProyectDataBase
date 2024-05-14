import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class ContratoFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_formulario()

    def create_formulario(self):
        inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        inner_frame.pack(padx=50, pady=50, ipadx=50, ipady=50)

        lbl_codigo = ttk.Label(inner_frame, text="Código Contrato:")
        lbl_codigo.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        entry_codigo = ttk.Entry(inner_frame, width=20)
        entry_codigo.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        lbl_fecha_contrato = ttk.Label(inner_frame, text="Fecha Contrato:")
        lbl_fecha_contrato.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        date_entry_contrato = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        date_entry_contrato.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_numero_contrato = ttk.Label(inner_frame, text="Número Contrato:")
        lbl_numero_contrato.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        entry_numero_contrato = ttk.Entry(inner_frame, width=20)
        entry_numero_contrato.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_fecha_inicio = ttk.Label(inner_frame, text="Fecha Inicio:")
        lbl_fecha_inicio.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        date_entry_inicio = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        date_entry_inicio.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        lbl_fecha_fin = ttk.Label(inner_frame, text="Fecha Fin:")
        lbl_fecha_fin.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        date_entry_fin = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        date_entry_fin.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear")
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar")
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar")
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar")
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")