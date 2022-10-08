'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio20.py
Author: Sam Hernandez
Action: Almacen de precios y comparacion de cantidades.
'''

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
sum = 0

for price in prices:
  sum += price
  if (price < min):
    min = price
  elif (price > max):
    max = price

print("El minimo es " + str(min))
print("El maximo es " + str(max))
print("La suma total es "  + str(sum))
    
