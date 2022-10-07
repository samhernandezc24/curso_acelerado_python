'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio17.py
Author: Sam Hernandez
Action: Tabla de multiplicar con entrada de usuario.
'''

n = int(input("Introduce el valor de la tabla de multiplicar: "))

for i in range(1, 13):
  resultado = n * i
  print(f'{n} x {i} = {resultado}')
  
