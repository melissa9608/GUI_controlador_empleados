import mysql.connector


class ModeloEmpleados:
    def __init__(self):
        self.Parametros = None

    def Insertar(self, Parametros):
        # Código de errores:
        # 0: Todo está bien.

        print(Parametros[0])
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Sentencia SQL para insertar un registro
            sentencia = "INSERT INTO empleados (NombresApellidos, NoCelular, CargoActual) VALUES (%s, %s, %s)"
            cursor.execute(sentencia, Parametros)
            conexion.commit()  # Confirmar los cambios
            return 0

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return 1  # Indicar que hubo un error

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def Actualizar(self, Parametros):
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Sentencia SQL para actualizar el registro
            sentencia = "UPDATE empleados SET NoCelular = %s, NombresApellidos = %s, CargoActual = %s WHERE Id = %s"
            cursor.execute(sentencia, Parametros)
            conexion.commit()  # Confirmar los cambios
            return 0

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return 1  # Error en la base de datos

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def Consultar(self, sentencia, parametros=None):
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Ejecutar la sentencia SQL con los parámetros si se proporcionan
            if parametros:
                cursor.execute(sentencia, parametros)
            else:
                cursor.execute(sentencia)

            resultados = cursor.fetchall()

            for fila in resultados:
                print(fila)

            return resultados

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return None  # Indicar que hubo un error

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def Borrar(self, Parametros):
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost', user='root', passwd='', db='empleados')

            cursor = conexion.cursor()

            # Sentencia SQL para eliminar un registro
            sentencia = "DELETE FROM empleados WHERE Id = %s"
            cursor.execute(sentencia, (Parametros[0],))
            conexion.commit()  # Confirmar los cambios
            print(f'Empleado con Id {Parametros[0]} ha sido borrado.')
            return 0

        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return 1  # Error en la base de datos

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
