import tkinter as tk
from tkinter import ttk

from Views.Cargo_View import CargosFrame
from Views.Empleado_View import VentanaEmpleado
from Views.Profesion_View import ProfesionesFrame
from Views.Municipio_View import MunicipiosFrame
from Views.Departamento_View import DepartamentosFrame
from Views.Sucursal_View import SucursalFrame
from Views.AcercaDe_View import PopupAcercaDe
from Views.Contrato_View import ContratoFrame
from Views.Usuario_View import UsuarioFrame

class BancoUQApp:
    def __init__(self, master, nivel_usuario):
        self.master = master
        self.nivel_usuario = nivel_usuario
        master.title("BancoUQ")
        self.current_frame = None

        self.menu = tk.Menu()
        self.menu_Entidades = tk.Menu(self.menu, tearoff=0)
        self.menu_Transacciones = tk.Menu(self.menu, tearoff=0)
        self.menu_Reportes = tk.Menu(self.menu, tearoff=0)
        self.menu_Utilidades = tk.Menu(self.menu, tearoff=0)
        self.menu_Ayudas = tk.Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="Entidades", menu=self.menu_Entidades)
        self.menu.add_cascade(label="Transacciones", menu=self.menu_Transacciones)
        self.menu.add_cascade(label="Resportes/Consultas", menu=self.menu_Reportes)
        self.menu.add_cascade(label="Utilidades", menu=self.menu_Utilidades)
        self.menu.add_cascade(label="Ayudas", menu=self.menu_Ayudas)

        self.menu_Entidades.add_command(label="Departamentos", command=self.abrir_panel_departamento)
        self.menu_Entidades.add_command(label="Tipo Municipios")
        self.menu_Entidades.add_command(label="Municipios", command=self.abrir_panel_municipio)
        self.menu_Entidades.add_command(label="Sucursales", command=self.abrir_panel_sucursal)
        self.menu_Entidades.add_command(label="Cargos", command=self.abrir_panel_cargo)
        self.menu_Entidades.add_command(label="Profesiones", command=self.abrir_panel_profesion)
        self.menu_Entidades.add_command(label="Empleados", command=self.abrir_panel_empleado)
        self.menu_Entidades.add_separator()
        self.menu_Entidades.add_command(label="Salir", command=master.quit)

        self.menu_Transacciones.add_command(label="Contratos", command=self.abrir_panel_contrato)

        self.menu_Reportes.add_command(label="Listar Sucursales")
        self.menu_Reportes.add_command(label="Informe Empelados")

        self.menu_Utilidades.add_command(label="Usuarios", command=self.abrir_panel_usuario)
        self.menu_Utilidades.add_command(label="Bitacora De Usuarios")

        self.menu_Ayudas.add_command(label="Ayudas De Aplicación")
        self.menu_Ayudas.add_command(label="Acerca De ...", command=self.abrir_PopUp_AcercaDe)

        opciones_deshabilitadas_Entidades = ["Profesiones", "Municipios", "Departamentos"]
        opciones_deshabilitadas_Transacciones = ["Contratos"]

        for opcion in opciones_deshabilitadas_Entidades:
            if self.nivel_usuario == "Principal":
                self.menu_Entidades.entryconfig(opcion, state="disabled")
            elif self.nivel_usuario == "esporadico":
                self.menu_Entidades.entryconfig(opcion, state="normal")

        for opcion1 in opciones_deshabilitadas_Transacciones:
            if self.nivel_usuario == 1:
                self.menu_Transacciones.entryconfig(opcion1, state="disabled")
            elif self.nivel_usuario == 2:
                self.menu_Transacciones.entryconfig(opcion1, state="normal")

        master.config(menu=self.menu)
        master.geometry("1000x600")

    def abrir_panel_empleado(self):
        self.switch_frame(VentanaEmpleado)

    def abrir_panel_profesion(self):
        self.switch_frame(ProfesionesFrame)

    def abrir_panel_municipio(self):
        self.switch_frame(MunicipiosFrame)

    def abrir_panel_departamento(self):
        self.switch_frame(DepartamentosFrame)

    def abrir_panel_cargo(self):
        self.switch_frame(CargosFrame)

    def abrir_panel_sucursal(self):
        self.switch_frame(SucursalFrame)

    def abrir_PopUp_AcercaDe(self):
        PopupAcercaDe(self.master)

    def abrir_panel_contrato(self):
        self.switch_frame(ContratoFrame)

    def abrir_panel_usuario(self):
        self.switch_frame(UsuarioFrame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

