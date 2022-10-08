# Sesion 2

Listado de ejercicios

* ejercicio8.py

Descripción: Detecta un numero negativo, positivo y cero.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio8.py
Author: Sam Hernandez
Action: Detecta un numero negativo, positivo y cero.
'''
numero = int(input("Escriba un número entero: "))

# Programa que detecta numero negativo, positivo y cero.
if (numero < 0):
  print("El número introducido es negativo.")
elif (numero > 0):
  print("El número introducido es positivo.")
else:
  print("El número introducido es cero.")
```

* ejercicio9.py

Descripcion: Pregunta contraseña y la compara con un valor registrado.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio8.py
Author: Sam Hernandez
Action: Programa que pregunta una contraseña al usuario y la compara con un valor registrado en una constante.
'''
VALOR_REGISTRADO = 'password123'

entrada = input("Introduce la contraseña: ")

if (entrada == VALOR_REGISTRADO):
  print("¡Autenticado exitosamente!")
else:
  print("La contraseña introducida no es correcta.")
```

* ejercicio10.py

Descripcion: Numero par o impar.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio10.py
Author: Sam Hernandez
Action: Numero par o impar.
'''
n = int(input("Introduce un número entero: "))

# Un número es par si la división entre 2 da un resto de 0, el número no puede ser multiplicado, se utiliza el operador modulo (%)
if (n % 2) == 0:
  print("El número " + str(n) + " es par.")
else:
  print("El número " + str(n) + " es impar.")
```

* ejercicio11.py

Descripcion: Estructura condicional anidada.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio11.py
Author: Sam Hernandez
Action: Estructura condicional anidada.
'''
mes = int(input("Introduzca el mes del año: "))

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
  print("El mes tiene 31 días.")
elif mes == 2:
  print("El mes tiene 28 o 29 días.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  print("El mes tiene 30 días.")
else:
  print("Mes no válido.")
```

* ejercicio12.py

Descripcion: Estructura condicional anidada.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio12.py
Author: Sam Hernandez
Action: Estructura condicional anidada.
'''
mes = int(input("Introduzca el mes del año: "))

if (1 <= mes <= 12):
  print("Se ha introducido un mes válido.")
else: 
  print("El mes es incorrecto. Por defecto se elige Enero.")
  mes = 1

print("Se utilizará mes", mes)
```

* ejercicio13.py

Descripcion: Suma de 10 primeros numeros.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio13.py
Author: Sam Hernandez
Action: Suma de 10 primeros numeros.
'''
num = 1
suma = 0

while (num <= 10):
  suma += num
  print(suma)
  num += 1
```

* ejercicio14.py

Descripcion: Mostrar 10 veces una palabra por pantalla.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio13.py
Author: Sam Hernandez
Action: Mostrar por pantalla 10 veces una palabra introducida por el usuario.
'''
palabra = input("Ingresa una palabra: ")
valor = 0

while (valor < 10):
  print(palabra)
  valor += 1
```

* ejercicio15.py

Descripcion: Suma valores ingresados por teclado.

``` python
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
```

* ejercicio16.py

Descripcion: Imprime un triangulo.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio16.py
Author: Sam Hernandez
Action: Imprime un triangulo.
'''
n = int(input("Introduce la altura del triangulo (entero positivo): "))

for i in range(n):
  for j in range(i + 1):
    print("*", end="")

  print("")
```

* ejercicio17.py

Descripcion: Imprime una tabla de multiplicar.

``` python
'''
********** Curso de programacion acelerado de Python **********
Date 10-07-2022
File: sesion2/ejercicio17.py
Author: Sam Hernandez
Action: Tabla de multiplicar con entrada de usuario.
'''
n = int(input("Introduce el valor de la tabla de multiplicar: "))

for i in range(1, 13):
  resultado = n * i
  print(f'{n} x {i} = {resultado}')
```
