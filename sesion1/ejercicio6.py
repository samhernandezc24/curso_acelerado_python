'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio6.py
Author: Sam Hernandez
Action: Imprime Capital obtenido de una inversion
'''

cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interes porcentual anual?: "))
años = int(input("¿Años?"))

print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))