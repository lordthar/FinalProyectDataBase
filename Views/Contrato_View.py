import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from Modelo.Contrato import Contrato
from Conexion import CConexion

class ContratoFrame(tk.Frame):
    def __init__(self, master=None, conection=None):
        super().__init__(master)
        self.master = master
        self.conection = conection
        self.create_formulario()

    def create_formulario(self):
        inner_frame = tk.Frame(self, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        inner_frame.pack(padx=50, pady=50, ipadx=50, ipady=50)

        lbl_title = tk.Label(inner_frame, text="Contratos", bg="#f0f0f0", fg="#333333", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=4, pady=(0, 20))

        lbl_numero_contrato = ttk.Label(inner_frame, text="Número Contrato:")
        lbl_numero_contrato.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_numero_contrato = ttk.Entry(inner_frame, width=20)
        self.entry_numero_contrato.grid(row=1, column=1, padx=10, pady=10, sticky="w")


        self.combobox_id = ttk.Combobox(inner_frame, width=18)
        self.combobox_id.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.combobox_id['values'] = Contrato.obtener_codigos_contrato(self.conection)

        lbl_fecha_contrato = ttk.Label(inner_frame, text="Fecha Contrato:")
        lbl_fecha_contrato.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.date_entry_contrato = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        self.date_entry_contrato.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lbl_fecha_contrato = ttk.Label(inner_frame, text="Fecha Inicio Contrato:")
        lbl_fecha_contrato.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.date_entry_contrato_inicio = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        self.date_entry_contrato_inicio.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        lbl_fecha_terminacion = ttk.Label(inner_frame, text="Fecha Terminación:")
        lbl_fecha_terminacion.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.date_entry_terminacion = DateEntry(inner_frame, width=18, background='gray', foreground='white', borderwidth=2)
        self.date_entry_terminacion.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        lbl_cargo = ttk.Label(inner_frame, text="Cargo:")
        lbl_cargo.grid(row=5, column=0, padx=10, pady=10, sticky="e")

        self.combo_cargo = ttk.Combobox(inner_frame, width=18)
        self.combo_cargo['values'] = Contrato.obtener_cargo(self.conection)
        self.combo_cargo.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        lbl_descripcion = ttk.Label(inner_frame, text="Descripción:")
        lbl_descripcion.grid(row=6, column=0, padx=10, pady=10, sticky="ne")

        self.text_descripcion = tk.Text(inner_frame, width=50, height=5)
        self.text_descripcion.grid(row=6, column=1, columnspan=3, padx=10, pady=10, sticky="w")

        lbl_sucursal = ttk.Label(inner_frame, text="Sucursal:")
        lbl_sucursal.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        self.combo_sucursal = ttk.Combobox(inner_frame, width=18)
        self.combo_sucursal['values'] = Contrato.obtener_sucursal(self.conection)
        self.combo_sucursal.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        lbl_empleado = ttk.Label(inner_frame, text="Empleado(s):")
        lbl_empleado.grid(row=8, column=0, padx=10, pady=10, sticky="ne")

        self.listbox_empleado = tk.Listbox(inner_frame, selectmode=tk.MULTIPLE, width=50, height=5)
        self.listbox_empleado.grid(row=8, column=1, columnspan=3, padx=10, pady=10, sticky="w")
        for empleado in Contrato.obtener_empleado(self.conection):
            self.listbox_empleado.insert(tk.END, empleado)

        btn_crear = ttk.Button(inner_frame, text="Crear", command=self.crear_contrato)
        btn_crear.grid(row=9, column=0, padx=5, pady=20, sticky="we")

        btn_eliminar = ttk.Button(inner_frame, text="Eliminar", command=self.eliminar_contrato)
        btn_eliminar.grid(row=9, column=1, padx=5, pady=20, sticky="we")

        btn_actualizar = ttk.Button(inner_frame, text="Actualizar", command=self.actualizar_contrato)
        btn_actualizar.grid(row=9, column=2, padx=5, pady=20, sticky="we")

        btn_buscar = ttk.Button(inner_frame, text="Buscar", command=self.buscar_contrato)
        btn_buscar.grid(row=9, column=3, padx=5, pady=20, sticky="we")

        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

    def crear_contrato(self):
        try:
            numero_contrato = self.entry_numero_contrato.get()
            fecha_contrato = self.date_entry_contrato.get_date().strftime('%Y-%m-%d')
            fecha_incio = self.date_entry_contrato_inicio.get_date().strftime('%Y-%m-%d')
            fecha_terminacion = self.date_entry_terminacion.get_date().strftime('%Y-%m-%d')
            cargo_contrato = self.combo_cargo.get()
            descripcion_contrato = self.text_descripcion.get("1.0", tk.END).strip()
            sucursal_contrato = self.combo_sucursal.get()
            empleados_seleccionados = self.listbox_empleado.curselection()

            if not numero_contrato or not fecha_contrato or not fecha_terminacion or not cargo_contrato or not descripcion_contrato or not sucursal_contrato or not empleados_seleccionados:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return

            codigo_cargo = Contrato.obtener_codigo_cargo_seleccionado(self.conection, cargo_contrato)
            codigo_sucursal = Contrato.obtener_codigo_sucursal_seleccionada(self.conection, sucursal_contrato)

            if None in [codigo_cargo, codigo_sucursal]:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para el cargo o la sucursal.")
                return

            for index in empleados_seleccionados:
                empleado_seleccionado = self.listbox_empleado.get(index)
                codigo_empleado = Contrato.obtener_codigo_empleado_seleccionado(self.conection, empleado_seleccionado)
                if codigo_empleado is None:
                    messagebox.showinfo("Error", f"No se encontró el código del empleado para {empleado_seleccionado}")
                    continue

                Contrato.ingresarContrato(numero_contrato, fecha_contrato, fecha_incio, fecha_terminacion, codigo_cargo, descripcion_contrato, codigo_sucursal, codigo_empleado)

            messagebox.showinfo("Registrado", "Contrato(s) registrado(s) exitosamente")
            self.limpiar_formulario()

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def eliminar_contrato(self):
        try:
            numero_contrato = self.combobox_id.get()
            if not numero_contrato:
                messagebox.showinfo("Error", "Debe ingresar el número de contrato")
                return

            Contrato.eliminarContrato(numero_contrato)
            messagebox.showinfo("Eliminado", "Contrato eliminado exitosamente")
            self.limpiar_formulario()

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def actualizar_contrato(self):
        try:
            numero_contrato = self.combobox_id.get()
            fecha_contrato = self.date_entry_contrato.get_date().strftime('%Y-%m-%d')
            fecha_inicio = self.date_entry_contrato_inicio.get_date().strftime('%Y-%m-%d')
            fecha_terminacion = self.date_entry_terminacion.get_date().strftime('%Y-%m-%d')
            cargo_contrato = self.combo_cargo.get()
            descripcion_contrato = self.text_descripcion.get("1.0", tk.END).strip()
            sucursal_contrato = self.combo_sucursal.get()
            empleados_seleccionados = self.listbox_empleado.curselection()

            if not numero_contrato or not fecha_contrato or not fecha_terminacion or not cargo_contrato or not descripcion_contrato or not sucursal_contrato or not empleados_seleccionados:
                messagebox.showinfo("Error", "Todos los campos son obligatorios")
                return

            codigo_cargo = Contrato.obtener_codigo_cargo_seleccionado(self.conection, cargo_contrato)
            codigo_sucursal = Contrato.obtener_codigo_sucursal_seleccionada(self.conection, sucursal_contrato)

            if None in [codigo_cargo, codigo_sucursal]:
                messagebox.showinfo("Error", "No se pudo encontrar el código correspondiente para el cargo o la sucursal.")
                return

            for index in empleados_seleccionados:
                empleado_seleccionado = self.listbox_empleado.get(index)
                codigo_empleado = Contrato.obtener_codigo_empleado_seleccionado(self.conection, empleado_seleccionado)
                if codigo_empleado is None:
                    messagebox.showinfo("Error", f"No se encontró el código del empleado para {empleado_seleccionado}")
                    continue

                Contrato.actualizarContrato(numero_contrato, fecha_contrato, fecha_inicio,fecha_terminacion, codigo_cargo, descripcion_contrato, codigo_sucursal, codigo_empleado)

            messagebox.showinfo("Actualizado", "Contrato(s) actualizado(s) exitosamente")
            self.limpiar_formulario()

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def buscar_contrato(self):
        try:
            numero_contrato = self.combobox_id.get()

            if not numero_contrato:
                messagebox.showinfo("Error", "Por favor ingrese el número del contrato a buscar.")
                return

            contrato = Contrato.buscarContrato(numero_contrato)

            if contrato:
                detalles_contrato = (
                    f"Número Contrato: {contrato[0]}\n"
                    f"Fecha Contrato: {contrato[1]}\n"
                    f"Fecha Terminación: {contrato[2]}\n"
                    f"Cargo: {contrato[3]}\n"
                    f"Descripción: {contrato[4]}\n"
                    f"Sucursal: {contrato[5]}\n"
                    f"Empleados: {contrato[6:]}"
                )

                messagebox.showinfo("Detalles del Contrato", detalles_contrato)
            else:
                messagebox.showinfo("Error", "No se encontró ningún contrato con el número proporcionado.")

        except ValueError as error:
            messagebox.showinfo("Error", str(error))

    def limpiar_formulario(self):
        self.entry_numero_contrato.delete(0, tk.END)
        self.combobox_id.set('')
        self.combo_cargo.set('')
        self.text_descripcion.delete("1.0", tk.END)
        self.combo_sucursal.set('')
        self.listbox_empleado.selection_clear(0, tk.END)
