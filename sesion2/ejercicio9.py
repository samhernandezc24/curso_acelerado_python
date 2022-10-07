'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio8.py
Author: Sam Hernandez
Action: Programa que pregunta una contraseña al usuario y la compara con un valor registrado en una constante.
'''

VALOR_REGISTRADO = 'password123'

entrada = input("Introduce la contraseña: ")

if (entrada == VALOR_REGISTRADO):
  print("¡Autenticado exitosamente!")
  
else:
  print("La contraseña introducida no es correcta.")

