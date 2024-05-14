import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class VentanaEmpleado(tk.Frame):
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

        lbl_title = tk.Label(inner_frame, text="Empleado", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_codigo = ttk.Label(inner_frame, text="Código Empleado:")
        lbl_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        entry_codigo = ttk.Entry(inner_frame, width=20)
        entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_cedula = ttk.Label(inner_frame, text="Cédula Empleado:")
        lbl_cedula.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        entry_cedula = ttk.Entry(inner_frame, width=20)
        entry_cedula.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        lbl_nombre = ttk.Label(inner_frame, text="Nombre Empleado:")
        lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        entry_nombre = ttk.Entry(inner_frame, width=20)
        entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_telefono = ttk.Label(inner_frame, text="Teléfono Empleado:")
        lbl_telefono.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        entry_telefono = ttk.Entry(inner_frame, width=20)
        entry_telefono.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        lbl_direccion = ttk.Label(inner_frame, text="Dirección Empleado:")
        lbl_direccion.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        entry_direccion = ttk.Entry(inner_frame, width=20)
        entry_direccion.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_profesion = ttk.Label(inner_frame, text="Profesión Empelado:")
        lbl_profesion.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        combo_profesion = ttk.Combobox(inner_frame, width=18)
        combo_profesion['values'] = ('Ingeniero', 'Médico', 'Abogado', 'Profesor', 'Otro')
        combo_profesion.grid(row=2, column=3, padx=10, pady=10, sticky="w")


        genero_frame = tk.Frame(inner_frame, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        genero_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        lbl_genero = ttk.Label(genero_frame, text="Género Empleado:")
        lbl_genero.grid(row=0, column=0, padx=(10, 5), pady=10)

        genero_value = tk.StringVar()

        radio_masculino = ttk.Radiobutton(genero_frame, text="Masculino", variable=genero_value, value="Masculino")
        radio_masculino.grid(row=0, column=1, padx=(5, 15), pady=10)

        radio_femenino = ttk.Radiobutton(genero_frame, text="Femenino", variable=genero_value, value="Femenino")
        radio_femenino.grid(row=0, column=2, padx=5, pady=10)

        radio_otro = ttk.Radiobutton(genero_frame, text="Otro", variable=genero_value, value="Otro")
        radio_otro.grid(row=0, column=3, padx=(15, 10), pady=10)

        lbl_fecha_nacimiento = ttk.Label(inner_frame, text="Fecha de Nacimiento Empleado:")
        lbl_fecha_nacimiento.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="e")

        date_entry = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        date_entry.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="w")

        btn_crear = ttk.Button(inner_frame, text="Crear", style='TButton.TButton')
        btn_crear.grid(row=5, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", style='TButton.TButton')
        btn_eliminar.grid(row=5, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", style='TButton.TButton')
        btn_actualizar.grid(row=5, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", style='TButton.TButton')
        btn_buscar.grid(row=5, column=3, padx=5, pady=20, sticky="we")

        # Configuración del estilo para los botones
        style.map('TButton.TButton',
                  background=[('active', '#448aff'), ('pressed', '#2979ff')],
                  foreground=[('active', 'black'), ('pressed', 'black')])

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")