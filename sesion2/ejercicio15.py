'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio15.py
Author: Sam Hernandez
Action: Suma valores ingresados por teclado.
'''

suma = 0

for f in range(10):
  valor = int(input("Ingresa valor: "))
  suma += valor

print("La suma es: ")
print(suma)

promedio = suma / 10

print("El promedio es: ")
print(promedio)
