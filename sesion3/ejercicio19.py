'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio19.py
Author: Sam Hernandez
Action: Palindromo
'''

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()

if (word == reversed_word):
  print("Es un palindromo")
else:
  print("No es un palindromo")

