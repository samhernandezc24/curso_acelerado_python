'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio12.py
Author: Sam Hernandez
Action: Estructura condicional anidada.
'''

mes = int(input("Introduzca el mes del año: "))

if (1 <= mes <= 12):
  print("Se ha introducido un mes válido.")
else: 
  print("El mes es incorrecto. Por defecto se elige Enero.")
  mes = 1

print("Se utilizará mes", mes)
