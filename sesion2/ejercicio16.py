'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio16.py
Author: Sam Hernandez
Action: Imprime un triangulo.
'''

n = int(input("Introduce la altura del triangulo (entero positivo): "))

for i in range(n):
  for j in range(i + 1):
    print("*", end="")

  print("")
