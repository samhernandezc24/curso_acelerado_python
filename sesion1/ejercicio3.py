'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio3.py
Author: Sam Hernandez
Action: Pago de Trabajador
'''

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
horas_extra = float(input("Introduce las horas extra: "))

coste_extra = coste * horas_extra
paga = (horas * coste) + coste_extra * 2

print("Tu paga es:", paga)
