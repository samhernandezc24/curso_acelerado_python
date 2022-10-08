'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio27.py
Author: Sam Hernandez
Action: Diccionario de datos de usuario.
'''

datos_usuario = {}
datos_usuario["nombre"] = input("Introduzca su nombre: ")
datos_usuario["edad"] = input("Introduzca su edad: ")
datos_usuario["direccion"] = input("Introduzca su direccion actual: ")
datos_usuario["telefono"] = input("Introduzca su numero de telefono: ")

print(datos_usuario["nombre"] + " tiene " + datos_usuario["edad"] + " años, vive en " + datos_usuario["direccion"] + " y su numero de telefono es " + datos_usuario["telefono"] + ".")