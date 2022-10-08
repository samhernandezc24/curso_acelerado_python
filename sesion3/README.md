# Sesion 3

Listado de ejercicios

* ejercicio18.py

Descripción: Verifica lista de datos y muestra un mensaje.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio18.py
Author: Sam Hernandez
Action: Verifica lista de datos y muestra un mensaje.
'''

personas_autorizadas = ["Alberto", "Carmen", "Sam", "Florencia", "Ixchel"]
nombre = input("Digame su nombre: ")

if (nombre in personas_autorizadas):
  print("Está autorizado")
else:
  print("No está autorizado")
```

* ejercicio19.py

Descripcion: Palindromo.

``` python
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
```

* ejercicio20.py

Descripcion: Almacen de precios y comparacion de cantidades.

``` python
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
```

* ejercicio21.py

Descripcion: Almacen de asignaturas de un curso.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio21.py
Author: Sam Hernandez
Action: Almacen de asignaturas de un curso.
'''

topics = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']

for topic in topics:
  print(topic)
  print("Mes no válido.")
```

* ejercicio22.py

Descripcion: Ganadores de loteria.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio22.py
Author: Sam Hernandez
Action: Ganadores de loteria.
'''

numeros_ganadores = list()

for num in range(5):
  numero = input("Ingrese el numero ganador: ")
  numeros_ganadores.append(numero)

print("Numeros de la loteria ordenados: ")
numeros_ganadores.sort()

for numero in numeros_ganadores:
  print(numero)
```

* ejercicio23.py

Descripcion: Almacen de tuplas.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio23.py
Author: Sam Hernandez
Action: Almacen de tuplas.
'''
a = (1, 2, 3)
b = (-1, 0, 2)
c = (2, -1, 4)
product = 0

for i in range(len(a)):
  product += a[i] * b[i] * c[i]

print("El producto de los vectores" + str(a) + " y " + str(b) + " y " + str(c) + " es " + str(product))
```

* ejercicio24.py

Descripcion: Diccionario vacio, con informacion de una persona.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio24.py
Author: Sam Hernandez
Action: Crear diccionario vacio y llenarlo con informacion de una persona.
'''
persona = {}
continuar = True

while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
```

* ejercicio25.py

Descripcion: Diccionario de traduccion español-ingles.

``` python
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
```

* ejercicio26.py

Descripcion: Diccionario de divisa.

``` python
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
  print("")
```

* ejercicio27.py

Descripcion: Diccionario de datos de usuario.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion3/ejercicio27.py
Author: Sam Hernandez
Action: Diccionario de datos de usuario.
'''

datos_usuario = {}
datos_usuario["nombre"] = input("Introduzca su nombre: ")
datos_usuario["edad"] = input("Introduzca su edad: ")
datos_usuario["direccion"] = input("Introduzca su direccion actual: ")
datos_usuario["telefono"] = input("Introduzca su numero de telefono: ")

print(datos_usuario["nombre"] + " tiene " + datos_usuario["edad"] + " años, vive en " + datos_usuario["direccion"] + " y su numero de telefono es " + datos_usuario["telefono"] + ".")
```
