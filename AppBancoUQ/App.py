import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import datetime

from Conexion import CConexion
from Modelo.Usuario_Bitacora import Usuario_Bitacora
from Views.Cargo_View import CargosFrame
from Views.Empleado_View import VentanaEmpleado
from Views.Profesion_View import ProfesionesFrame
from Views.Municipio_View import MunicipiosFrame
from Views.Departamento_View import DepartamentosFrame
from Views.Sucursal_View import SucursalFrame
from Views.AcercaDe_View import PopupAcercaDe
from Views.Contrato_View import ContratoFrame
from Views.Usuario_View import UsuarioFrame
from Views.Tipo_Municipio_View import TipoMunicipio_Frame
from Views.Usuarios_Bitacora_View import usuarios_bitacora_view
from Views.Listar_Sucursales_View import ListarSucursalesView
from Views.Informe_Deptos_View import InformeDeptosView
from Views.Informe_Municipios_View import InformeMunicipiosView
from Views.Informe_Cargos_View import InformeCargosView
from Views.Informe_Empleados_View import InformeEmpleadosView
from Views.Listar_Contratos_View import ListarContratosView
from Views.Ayuda_Aplicación_View import PopupAyudaAplicacion
class BancoUQApp:
    def __init__(self, master, nivel_usuario, usuario_actual = None):
        self.master = master
        self.nivel_usuario = nivel_usuario
        self.usuario_actual = usuario_actual
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
        self.menu_Entidades.add_command(label="Tipo Municipios", command= self.abrir_panel_tipo_municipio)
        self.menu_Entidades.add_command(label="Municipios", command=self.abrir_panel_municipio)
        self.menu_Entidades.add_command(label="Sucursales", command=self.abrir_panel_sucursal)
        self.menu_Entidades.add_command(label="Cargos", command=self.abrir_panel_cargo)
        self.menu_Entidades.add_command(label="Profesiones", command=self.abrir_panel_profesion)
        self.menu_Entidades.add_command(label="Empleados", command=self.abrir_panel_empleado)
        self.menu_Entidades.add_separator()
        self.menu_Entidades.add_command(label="Cerrar Sesión", command=self.salir_sesion)

        self.menu_Transacciones.add_command(label="Contratos", command=self.abrir_panel_contrato)

        self.menu_Reportes.add_command(label="Listar Sucursales", command= self.abrir_panel_listar_sucursales)
        self.menu_Reportes.add_command(label="Informe Empelados", command= self.abrir_panel_Informe_Empleados)
        self.menu_Reportes.add_command(label="Listar Contratos", command= self.abrir_panel_listar_Contratos)
        self.menu_Reportes.add_command(label="Informe Departamentos", command= self.abrir_panel_Informe_Deptos)
        self.menu_Reportes.add_command(label="Informe Municipios", command= self.abrir_panel_Informe_Municipios)
        self.menu_Reportes.add_command(label="Informe Cargos", command= self.abrir_panel_Informe_Cargos)

        self.menu_Utilidades.add_command(label="Usuarios", command=self.abrir_panel_usuario)
        self.menu_Utilidades.add_command(label="Bitacora De Usuarios", command=self.abrir_panel_bitacora_usuario)

        self.menu_Ayudas.add_cascade(label="Ayudas De Aplicación", command= self.abrir_popUp_Ayuda_Aplicacion)
        self.menu_Ayudas.add_command(label="Acerca De ...", command=self.abrir_PopUp_AcercaDe)

        self.menu_Utilidades.add_command(label="Abrir Calculadora", command=self.abrir_calculadora)
        self.menu_Utilidades.add_command(label="Mostrar Fecha y Hora", command=self.mostrar_fecha_hora)

        opciones_deshabilitadas_Entidades = ["Profesiones", "Municipios", "Departamentos", "Tipo Municipios", "Sucursales", "Cargos", "empleados"]
        opciones_deshabilitadas_Transacciones = ["Contratos"]
        opciones_deshabilitadas_Usuarios = ["Usuarios", "Bitacora De Usuarios"]

        for opcion in opciones_deshabilitadas_Entidades:
            if self.nivel_usuario == "Esporadico":
                self.menu_Entidades.entryconfig(opcion, state="disabled")

        for opcion1 in opciones_deshabilitadas_Transacciones:
            if self.nivel_usuario == "Esporadico":
                self.menu_Transacciones.entryconfig(opcion1, state="disabled")

        for opcion2 in opciones_deshabilitadas_Usuarios:
            if self.nivel_usuario == "Esporadico":
                self.menu_Utilidades.entryconfig(opcion2, state="disabled")
            elif self.nivel_usuario == "Paramétrico":
                self.menu_Utilidades.entryconfig(opcion2, state="disabled")

        master.config(menu=self.menu)
        master.geometry("1000x600")


    def abrir_panel_listar_sucursales(self):
        self.switch_frame(ListarSucursalesView)
    def abrir_panel_listar_Contratos(self):
        self.switch_frame(ListarContratosView)
    def abrir_panel_Informe_Empleados(self):
        self.switch_frame(InformeEmpleadosView)
    def abrir_panel_Informe_Municipios(self):
        self.switch_frame(InformeMunicipiosView)
    def abrir_panel_Informe_Deptos(self):
        self.switch_frame(InformeDeptosView)
    def abrir_panel_Informe_Cargos(self):
        self.switch_frame(InformeCargosView)
    def abrir_panel_empleado(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(VentanaEmpleado, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_bitacora_usuario(self):
        self.switch_frame(usuarios_bitacora_view)
    def abrir_panel_profesion(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(ProfesionesFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_municipio(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(MunicipiosFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_departamento(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(DepartamentosFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_cargo(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(CargosFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_sucursal(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(SucursalFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_PopUp_AcercaDe(self):
        PopupAcercaDe(self.master)

    def abrir_popUp_Ayuda_Aplicacion(self):
        PopupAyudaAplicacion(self.master)

    def abrir_panel_contrato(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(ContratoFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_usuario(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(UsuarioFrame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")

    def abrir_panel_tipo_municipio(self):
        conexion = CConexion.ConexionBasedeDatos()
        if conexion:
            self.switch_frame(TipoMunicipio_Frame, conexion)
        else:
            messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos")
    def switch_frame(self, frame_class, conexion=None):
        if conexion:
            new_frame = frame_class(self.master, conection=conexion)
        else:
            new_frame = frame_class(self.master)

        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def salir_sesion(self):
        if self.usuario_actual:
            Usuario_Bitacora.registrar_cierre_sesion(self.usuario_actual)

        if messagebox.askokcancel("Cerrar sesión", "¿Estás seguro de que quieres cerrar sesión?"):
            self.master.destroy()

    def abrir_calculadora(self):
        try:
            subprocess.Popen("calc.exe")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se pudo abrir la calculadora")

    def mostrar_fecha_hora(self):
        now = datetime.datetime.now()
        dia_semana_en = now.strftime("%A")
        dias_semana = {
            "Monday": "Lunes",
            "Tuesday": "Martes",
            "Wednesday": "Miércoles",
            "Thursday": "Jueves",
            "Friday": "Viernes",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        dia_semana_es = dias_semana[dia_semana_en]
        fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
        messagebox.showinfo("Fecha, Hora y Día", f"Fecha y Hora: {fecha_hora}\nDía: {dia_semana_es}")

