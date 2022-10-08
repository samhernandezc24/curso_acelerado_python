'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio22.py
Author: Sam Hernandez
Action: Ganadores de loteria.
'''

numeros_ganadores = list()

for num in range(5):
  numero = input("Ingrese el numero ganador: ")
  numeros_ganadores.append(numero)

print("Numeros de la loteria ordenados: ")
numeros_ganadores.sort()

for numero in numeros_ganadores:
  print(numero)