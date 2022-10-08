'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio26.py
Author: Sam Hernandez
Action: Diccionario de Divisa.
'''

diccionario = {'Euro':'€', 'Dollar':'$', 'Peso':'$'}
divisa = input("Introduce una divisa: ")

if divisa in diccionario:
  print("El simbolo de la divisa", divisa, "es", diccionario[divisa])
else:
  print("La divisa introducida no está disponible.")