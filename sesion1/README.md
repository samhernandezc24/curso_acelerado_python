# Sesion 1

Listado de ejercicios

* ejercicio1.py

Descripción: Asignacion de Variables.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio1.py
Author: Sam Hernandez
Action: Asignacion de Variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 24030000000
promedio_temperatura = 31.3
estados_cercanos = ['chiapas', 'campeche', 'veracruz']
productos_locales = ['cacao', 'coco', 'caña']

print(nombre_estado, "es un estado que ", )
print("con", estados_cercanos[0], "colinda al sur,")
print("tiene una superficie de", superficie, "y")
print("además se consume mucho el", productos_locales)
```

* ejercicio2.py

Descripcion: Superficie de un Cuadrado.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio2.py
Author: Sam Hernandez
Action: Superficie de un Cuadrado
'''
lado = input("Ingrese la medida del lado del cuadrado: ")
# lado = int(lado)
lado = float(lado)
superficie = lado * lado

print("La superficie del cuadrado es: ")
print(superficie)
```

* ejercicio3.py

Descripcion: Pago de Trabajador.

``` python
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
```

* ejercicio4.py

Descripcion: Indice de masa corporal en kg/ estatura mtrs cuadrados

``` python
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
```

* ejercicio5.py

Descripcion: Convertir grados celsius a fahrenheit.

``` python
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
```

* ejercicio6.py

Descripcion: Imprimir capital obtenido de una inversion.

``` python
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
```


* ejercicio7.py

Descripcion: Suma de los primeros numeros enteros.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion1/ejercicio7.py
Author: Sam Hernandez
Action: Suma de los primeros números enteros
'''

n = int(input("Introduce un numero entero: "))
suma = (n * (n + 1) / 2)

print("La suma de los primeros numeros enteros desde 1 hasta", n, "es", suma)
```
