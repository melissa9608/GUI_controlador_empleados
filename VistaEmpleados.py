import tkinter as tk
from tkinter import messagebox
from ModeloEmpleados import ModeloEmpleados
from ControladorEmpleados import ControladorEmpleados


# Función para obtener el texto de las cajas de texto
def insertar_empleado():
    nombres_apellidos = caja_texto1.get()
    no_celular = caja_texto2.get()
    cargo_actual = caja_texto3.get()

    controlador_empleados = ControladorEmpleados()
    controlador_empleados.NombresApellidos = nombres_apellidos
    controlador_empleados.NoCelular = no_celular
    controlador_empleados.CargoActual = cargo_actual

    resultado_validacion = controlador_empleados.Insertar(
        nombres_apellidos, no_celular, cargo_actual)

    if resultado_validacion == 1:
        messagebox.showerror("Error", "Hay campos vacíos")
    elif resultado_validacion == 2:
        messagebox.showerror("Error", "El número de celular debe ser numérico")
    elif resultado_validacion == 0:
        datos = [nombres_apellidos, no_celular, cargo_actual]
        modelo_empleados = ModeloEmpleados()
        resultado_ejecucion = modelo_empleados.Insertar(datos)
        if resultado_ejecucion == 0:
            messagebox.showinfo(
                "Información", "Registro insertado exitosamente")


def actualizar_empleado():
    id_empleado = caja_texto_id.get()
    nombres_apellidos = caja_texto1.get()
    no_celular = caja_texto2.get()
    cargo_actual = caja_texto3.get()

    controlador_empleados = ControladorEmpleados()
    resultado_validacion = controlador_empleados.Actualizar(
        id_empleado, nombres_apellidos, no_celular, cargo_actual)

    if resultado_validacion == 1:
        messagebox.showerror("Error", "Hay campos vacíos")
    elif resultado_validacion == 2:
        messagebox.showerror("Error", "El número de celular debe ser numérico")
    elif resultado_validacion == 0:
        messagebox.showinfo("Información", "Registro actualizado exitosamente")

# Función para consultar empleados


def consultar_empleado():
    id_empleado = caja_texto_id.get()
    controlador_empleados = ControladorEmpleados()
    resultados = controlador_empleados.Consultar(id_empleado)

    if resultados is not None:
        for empleado in resultados:
            messagebox.showinfo("Empleado", f"ID: {empleado[0]}, Nombres: {
                                empleado[1]}, Celular: {empleado[2]}, Cargo: {empleado[3]}")
    else:
        messagebox.showerror("Error", "No se encontró el empleado")


# Función para borrar un empleado
def borrar_empleado():
    id_empleado = caja_texto_id.get()
    controlador_empleados = ControladorEmpleados()
    resultado_validacion = controlador_empleados.Borrar(id_empleado)

    if resultado_validacion == 0:
        messagebox.showinfo("Información", "Registro borrado exitosamente")
    else:
        messagebox.showerror("Error", "Error al borrar el registro")


# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("350x300")
ventana.title("Gestión de Empleados")

# Crear las etiquetas
etiqueta_id = tk.Label(ventana, text="ID del Empleado:")
etiqueta1 = tk.Label(ventana, text="Nombres y Apellidos:")
etiqueta2 = tk.Label(ventana, text="Número de Celular:")
etiqueta3 = tk.Label(ventana, text="Cargo Actual:")

# Crear las cajas de texto
caja_texto_id = tk.Entry(ventana)
caja_texto1 = tk.Entry(ventana)
caja_texto2 = tk.Entry(ventana)
caja_texto3 = tk.Entry(ventana)

# Posicionar las etiquetas y cajas de texto
etiqueta_id.place(x=30, y=20)
caja_texto_id.place(x=185, y=20)
etiqueta1.place(x=30, y=50)
caja_texto1.place(x=185, y=50)
etiqueta2.place(x=30, y=80)
caja_texto2.place(x=185, y=80)
etiqueta3.place(x=30, y=110)
caja_texto3.place(x=185, y=110)

# Crear los botones
boton_insertar = tk.Button(
    ventana, text="Insertar Registro", command=insertar_empleado)
boton_actualizar = tk.Button(
    ventana, text="Actualizar Registro", command=actualizar_empleado)
boton_consultar = tk.Button(
    ventana, text="Consultar Registro", command=consultar_empleado)
boton_borrar = tk.Button(
    ventana, text="Borrar Registro", command=borrar_empleado)
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)

# Posicionar los botones
boton_insertar.place(x=30, y=160)
boton_actualizar.place(x=30, y=200)
boton_consultar.place(x=200, y=160)
boton_borrar.place(x=200, y=200)
boton_salir.place(x=165, y=250)

# Iniciar el bucle principal
ventana.mainloop()
