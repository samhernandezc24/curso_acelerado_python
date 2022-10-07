'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio5.py
Author: Sam Hernandez
Action: Programa que convierte grados Celsius a Fahrenheit.
'''

celsius = float(input("Introduce el grado celsius: "))

# calcular a fahrenheit
fahrenheit = (celsius * 1.8) + 32

print('%0.1f grados Celsius es igual a %0.1f grados Fahrenheit' %(celsius, fahrenheit))
