'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio18.py
Author: Sam Hernandez
Action: Verifica lista de datos y muestra un mensaje.
'''

personas_autorizadas = ["Alberto", "Carmen", "Sam", "Florencia", "Ixchel"]
nombre = input("Digame su nombre: ")

if (nombre in personas_autorizadas):
  print("Está autorizado")
else:
  print("No está autorizado")
