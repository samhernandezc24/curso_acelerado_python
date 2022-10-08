'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio25.py
Author: Sam Hernandez
Action: Diccionario de traduccion español-ingles.
'''

diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traduccion separadas por comas: ")

for i in palabras.split(','):
  clave, valor = i.split(':')
  diccionario[clave] = valor

frase = input('Introduce una frase en español: ')

for i in frase.split():
  if i in diccionario:
    print(diccionario[i], end=' ')
  else:
    print(i, end=' ')