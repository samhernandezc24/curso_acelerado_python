'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio10.py
Author: Sam Hernandez
Action: Numero par o impar.
'''

n = int(input("Introduce un número entero: "))

# Un número es par si la división entre 2 da un resto de 0, el número no puede ser multiplicado, se utiliza el operador modulo (%)
if (n % 2) == 0:
  print("El número " + str(n) + " es par.")
else:
  print("El número " + str(n) + " es impar.")
