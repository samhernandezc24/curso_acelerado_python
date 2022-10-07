'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio4.py
Author: Sam Hernandez
Action: Indice de masa corporal peso en kg/ estatura mtrs cuadrados
'''

peso = input("¿Cuál es tu peso en kg?: ")
estatura = input("¿Cuál es tu estatura en metros?: ")
imc = round(float(peso) / float(estatura) ** 2, 2)

print("Tu indice de masa corporal es " + str(imc))