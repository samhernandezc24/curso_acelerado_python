'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio8.py
Author: Sam Hernandez
Action: Detecta un numero negativo.
'''

# numero = int(input("Escriba un número positivo: "))
numero = int(input("Escriba un número entero: "))

# Condicion que detecta un numero negativo
"""
if (numero < 0):
  print("¡Le he dicho que escriba un número positivo!")
  print(f"Ha escrito el número {numero}")
"""

# Programa que detecta numero negativo, positivo y cero.
if (numero < 0):
  print("El número introducido es negativo.")

elif (numero > 0):
  print("El número introducido es positivo.")

else:
  print("El número introducido es cero.")

