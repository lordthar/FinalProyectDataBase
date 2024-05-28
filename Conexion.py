import mysql.connector

class CConexion:

    def ConexionBasedeDatos(Self = None):
        try:
            conexion = mysql.connector.connect(user='root', password='Migue3182078123@', host='127.0.0.1', database='BancoDB', port='3306')
            print("Conexion Correcta")
            return conexion
        except mysql.connector.Error as error:
            print("Database connection error: ".format(error))
            return conexion