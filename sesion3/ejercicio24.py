'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio24.py
Author: Sam Hernandez
Action: Crear diccionario vacio y llenarlo con informacion de una persona.
'''
persona = {}
continuar = True

while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"