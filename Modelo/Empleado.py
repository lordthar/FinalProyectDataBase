from Conexion import *

class Empleado:
    def __init__(self, codigo, cedula, nombre, direccion, telefono, cargo, profesion):
        self.codigo = codigo
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.profesion = profesion