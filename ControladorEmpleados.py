from ModeloEmpleados import ModeloEmpleados
import mysql.connector


class ControladorEmpleados:
    def __init__(self):
        self.Id = None
        self.NombresApellidos = None
        self.NoCelular = None
        self.CargoActual = None

    def Insertar(self, NombresApellidos, NoCelular, CargoActual):
        # Código de errores:
        # 0: Todo está bien.
        # 1: Hay campos vacíos.
        # 2: Un valor que se requiere como número no lo es.

        if len(NombresApellidos) <= 1 or NoCelular == "" or CargoActual == "":
            return 1

        try:
            # Convertir el valor a un número entero
            int(NoCelular)
        except ValueError:
            return 2

        return 0

    def Actualizar(self, Id, NombresApellidos, NoCelular, CargoActual):

        if len(NombresApellidos) <= 1 or NoCelular == "" or CargoActual == "":
            return 1

        conexion = None

        cursor = None

        try:
            # Convertir el valor a un número entero
            int(NoCelular)
        except ValueError:
            return 2

        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Sentencia SQL para actualizar el registro
            sentencia = "UPDATE empleados SET NombresApellidos = %s, NoCelular = %s, CargoActual = %s WHERE Id = %s"
            cursor.execute(sentencia, (NombresApellidos,
                           NoCelular, CargoActual, Id))
            conexion.commit()  # Confirmar los cambios

            print(f'Empleado con Id {Id} ha sido actualizado.')
            return 0

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return 3  # Error en la base de datos

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def Consultar(self, Id=None):
        conexion = None
        cursor = None
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Sentencia SQL para consultar por Id o todos los registros
            if Id is not None:
                sentencia = "SELECT * FROM empleados WHERE Id = %s"
                cursor.execute(sentencia, (Id,))
            else:
                sentencia = "SELECT * FROM empleados"
                cursor.execute(sentencia)

            resultados = cursor.fetchall()

            for fila in resultados:
                print(fila)

            return resultados

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return None

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def Borrar(self, Id):
        conexion = None
        cursor = None

        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Sentencia SQL para eliminar un registro
            sentencia = "DELETE FROM empleados WHERE Id = %s"
            cursor.execute(sentencia, (Id,))
            conexion.commit()  # Confirmar los cambios

            print(f'Empleado con Id {Id} ha sido borrado.')
            return 0

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return 1  # Error en la base de datos

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
