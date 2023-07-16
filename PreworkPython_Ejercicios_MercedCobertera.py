'''
VARIABLES Y OPERADORES
'''
# 1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor. Luego, imprime la variable.
print('VARIABLES Y OPERADORES: Ejercicio 1')
nombre = 'Merced'
print(nombre)

# 2. Ejercicio: Crea dos variables, a y b , y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b .
print('VARIABLES Y OPERADORES: Ejercicio 2')
a = 5
b = 10
print ("La suma de", a, " + ", b, " es igual a", a+b)

# 3. Ejercicio: Calcula el área de un triángulo con base 10 y altura 5.
print('VAIABLES Y OPERADORES: Ejercicio 3')
area_triangulo = (a*b)/2
print("El área del triangulo es igual a", area_triangulo)

# 4. Ejercicio: Calcula el resto de dividir 17 entre 3.
print('VARIABLES Y OPERADORES: Ejercicio 4')
resto = 17 % 3
print("El resto de la división es", resto)


'''
CONDICIONALES
'''

# 1. Ejercicio: Dado un número, imprime si es positivo o negativo.
print('CONDICIONALES: Ejercicio 1')
x = 46
if x < 0:
    print('x es negativo')
else:
    print('x es positivo')

# 2. Ejercicio: Dado un número, imprime si es par o impar.
print('CONDICIONALES: Ejercicio 2')
if x % 2 == 0:
    print('x es par')
else:
    print( 'x es impar')

# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
print('CONDICIONALES: Ejercicio 3')
a = 7
b = 5
c = 4

if a > b:
    Num_mayor = a
elif b > c:
    Num_mayor = b
else:
    Num_mayor = c
print("El mayor de los números dados es:", Num_mayor)

'''
BUCLES
'''

# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
print('BUCLES: Ejercicio 1')
for num in range(11):
    print(num)

# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
print('BUCLES: Ejercicio 2')
num = 0
while num < 20:
    num = num + 2
    print(num)

# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
print('BUCLES: Ejercicio 3')
num = 1
suma = 1
while num < 100:
    num = num + 1
    suma = suma + num
print("La suma de los números del 1 al 100 es igual a", suma)

'''
FUNCIONES
'''
# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
print('FUNCIONES: Ejercicio 1')
a = 16
b = 5
def suma(a, b):
    return a + b
resultado = suma(a,b)
print(resultado)

# 2. Ejercicio: Define una función que tome un número y retorne su factorial.
print('FUNCIONES: Ejercicio 2')
a = 5
def factorial(a):
    resultado = 1
    i = 1
    while i <= a:
        resultado = resultado * i
        i = i + 1
    print("!",a,"=", resultado)
    return resultado
fact_a = factorial (a)

# 3. Ejercicio: Define una función que tome un número y determine si es primo.
print('FUNCIONES: Ejercicio 3')
a =11
def es_primo (a):
    for b in range(2, a):
      if a % b == 0:
          return False
    return True
print(es_primo(a))

# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
print('FUNCIONES: Ejercicio 4')
lista = [1, 2, 3, 4]
def suma_lista(lista):
    suma = 0
    for n in lista:
      suma = suma + n
    return suma
print(suma_lista(lista))

# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
print('FUNCIONES: Ejercicio 5')
texto = 'Prueba inversion'
def invertir_cadena(texto):
    texto_invertido = texto[::-1]
    print(texto_invertido)
    return texto_invertido
invertir_cadena(texto)

'''
BUCLES Y FUNCIONES
'''
# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
print('BUCLES Y FUNCIONES: Ejercicio 1')
n = 9
def serie_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
      c = b + a
      a = b
      b = c
      print(a)
serie_fibonacci(n)

# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
print('BUCLES Y FUNCIONES: Ejercicio 2')
n = 21
def obtener_divisores(n):
    divisores = [1]
    for i in range(2, n+1):
      if n % i == 0:
          divisores.append(i)
    print("Los divisores de ", n, "son",divisores)
    return divisores
obtener_divisores(n)

# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
print('BUCLES Y FUNCIONES: Ejercicio 3')
lista = [1, 2, 2, 3, 4, 4]
def contar_elementos_unicos(lista):
    primer_valor = lista[0]
    a = len(lista)
    b = 1
    lista_unicos = []
    for b in range(1, a):
        if primer_valor == b:
            lista_unicos.append(b)
            primer_valor = lista[b+1]
    print(lista_unicos)
    return lista_unicos
contar_elementos_unicos(lista)

# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
print('BUCLES Y FUNCIONES: Ejercicio 4')
num = 5891
def suma_digitos(num):
    suma = 0
    b = num
    while b != 0:
        a = b % 10
        suma = suma + a
        b = b // 10
    print(suma)
    return suma
suma_digitos(num)

# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
print('BUCLES Y FUNCIONES: Ejercicio 5')
cadena = 'Contar numero de vocales en una cadena'
def contar_vocales(cadena):
    veces_a = 0
    veces_e = 0
    veces_i = 0
    veces_o = 0
    veces_u = 0
    for letra in cadena:
        if letra == 'a' or letra == 'A':
            veces_a = veces_a + 1
        elif letra == 'e' or letra == 'E':
            veces_e = veces_e + 1
        elif letra == 'i' or letra == 'I':
            veces_i = veces_i + 1
        elif letra == 'o' or letra == 'O':
            veces_o = veces_o + 1
        elif letra == 'u' or letra == 'U':
            veces_u = veces_u + 1
    print("La vocal A aparece", veces_a, "veces")
    print("La vocal E aparece", veces_e, "veces")
    print("La vocal I aparece", veces_i, "veces")
    print("La vocal O aparece", veces_o, "veces")
    print("La vocal U aparece", veces_u, "veces")
    return veces_a, veces_e, veces_i, veces_o, veces_u
contar_vocales(cadena)

# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
print('BUCLES Y FUNCIONES: Ejercicio 6')
lista = [1, 2, 3, 'x', 9, 20, 115, 'a']
elementos_a_mostrar = 5
def mostrar_elementos_lista(lista):
    lista_elementos_mostrados = []
    elemento = 1
    for elemento in range(0, elementos_a_mostrar):
        lista_elementos_mostrados.append(lista[elemento])
    print(lista_elementos_mostrados)
    return lista_elementos_mostrados
mostrar_elementos_lista(lista)

# 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
print('BUCLES Y FUNCIONES: Ejercicio 7')
cadena = 'Ejemplo para CONTAR mayusculas y MINUSCULAS en una FRase'
def contar_may_min(cadena):
    posicion = 0
    mayusculas = 0
    minusculas = 0
    while posicion < len(cadena):
        caracter = cadena[posicion]
        if caracter.isupper() == True:
            mayusculas = mayusculas + 1
        else:
            minusculas = minusculas + 1
        posicion += 1
    print("Total mayusculas:", mayusculas)
    print("Total minusculas:", minusculas)
    return mayusculas, minusculas
contar_may_min(cadena)

# 8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
print('BUCLES Y FUNCIONES: Ejercicio 8')
n = 6
def num_perfecto(n):
    divisores = obtener_divisores(n)
    suma = 0
    a = len(divisores) - 1
    for divisor in range(0, a):
        suma = suma + divisores[divisor]
    print("La suma de los divisores perfectos de ", n, "es igual a",suma)
    if suma == n:
        num_perfect = True
    else:
        num_perfect = False
    print(num_perfect)
    return num_perfect
num_perfecto(n)

# 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
print('BUCLES Y FUNCIONES: Ejercicio 9')
num_decimal = 233
def conversion_binario(num_decimal):
    decimal = num_decimal
    modulos = []
    while num_decimal > 0:
        resto = num_decimal % 2
        cociente = num_decimal // 2
        modulos.insert(0, resto)
        num_decimal = cociente
    print(modulos)
    multiplicador = 1
    num_binario = 0
    for digito in range(0, len(modulos))[::-1]:
        num_binario = num_binario + (modulos[digito] * multiplicador)
        multiplicador = multiplicador * 10
    print(decimal, "en binario es", num_binario)
    return num_binario
conversion_binario(num_decimal)

# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
print('BUCLES Y FUNCIONES: Ejercicio 10')
lista1 = [1, 5, 25, 3, 2]
lista2 = [1, 25, 56, 115, 0]
def interseccion_listas(lista1, lista2):
    list1 = set(lista1)
    list2 = set(lista2)
    interseccion = list1 & list2
    lista_comunes = list(interseccion)
    print("Los elementos comunes en ambas listas son:", lista_comunes)
    return lista_comunes
interseccion_listas(lista1, lista2)

# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
print('BUCLES Y FUNCIONES: Ejercicio 11')
cadena = 'ana'
def es_palindromo(cadena):
    if invertir_cadena(cadena) == cadena:
        print(cadena, "es un palíndromo")
        return True
    print(cadena, "no es un palíndromo")
    return False
es_palindromo(cadena)

# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
print('BUCLES Y FUNCIONES: Ejercicio 12')
def es_multiplo_n(num, multiplo):
    if num % multiplo == 0:
        multiplo_n = True
    else:
        multiplo_n = False
    return multiplo_n

for num in range(51):
    if es_multiplo_n(num, 3) == True and es_multiplo_n(num, 5) == True:
        print('FizzBuzz')
    elif es_multiplo_n(num, 3) == True:
        print('Fizz')
    elif es_multiplo_n(num, 5) == True:
        print('Buzz')
    else:
        print(num)
    num = num + 1

# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
print('BUCLES Y FUNCIONES: Ejercicio 13')
lista = [1, 69, 3, 552, 600]
def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print(lista_ordenada)
    return lista_ordenada
ordenar_lista(lista)

# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
print('BUCLES Y FUNCIONES: Ejercicio 14')
lista = ['hola', 'pruebas', 'paralelogramo', 'cancion', 'longitud']
longitud = 5
def longitud_palabras(lista, longitud):
    lista_longitud = []
    for elemento in lista:
        if len(elemento) >= longitud:
            lista_longitud.append(elemento)
    print(lista_longitud)
    return lista_longitud
longitud_palabras(lista, longitud)

# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.

'''¿qué diferencia hay entre este ejercicio y el número 1 de este bloque?'''

# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
print('BUCLES Y FUNCIONES: Ejercicio 16')
lista_num = [1, 5, 25, 3, 14]
def elemento_mayor(lista):
    mayor = lista_num[0]
    for numero in lista_num:
        if numero > mayor:
            mayor = numero
    print(mayor)
    return mayor
elemento_mayor(lista)

# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
print('BUCLES Y FUNCIONES: Ejercicio 17')
num = 123
def suma_digitos_al_cubo(num):
    suma_cubo = suma_digitos(num)
    cubo = suma_digitos(num)
    for i in range(2):
        suma_cubo = suma_cubo * cubo
    print("La suma de los dígitos de", num, "al cubo es igual a", suma_cubo)
    return suma_cubo
suma_digitos_al_cubo(num)

# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
print('BUCLES Y FUNCIONES: Ejercicio 18')
lista = [1, 56, 8, 125]
def segundo_mayor(lista):
    lista_ordenada = ordenar_lista(lista)
    penultimo = lista_ordenada[-2]
    print("El segundo número más grande de la lista es:",penultimo)
    return penultimo
segundo_mayor(lista)

# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
print('BUCLES Y FUNCIONES: Ejercicio 19')
lista1 = [1, 5, 25, 3, 2]
lista2 = [1, 25, 56, 115, 0]
def tienen_elementos_comunes(lista1, lista2):
    lista_comunes = interseccion_listas(lista1, lista2)
    len(lista_comunes)
    if len(lista_comunes) == 0:
        print('Ambas listas no tienen elementos comunes')
        return False
    print('Ambas listas tienen al menos un elemento en cumún')
    return True
tienen_elementos_comunes(lista1, lista2)

# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
print('BUCLES Y FUNCIONES: Ejercicio 20')
lista = [1, 25, 54, 2, 0, 89]

def invertir_lista(lista):
    lista_inversa = lista[::-1]
    print(lista_inversa)
    return lista_inversa
invertir_lista(lista)

# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
print('BUCLES Y FUNCIONES: Ejercicio 21')
cadena = '125 euros y 4 productos'
def contar_numeros_letras(cadena):
    digitos = 0
    letras = 0
    for elemento in cadena:
        if elemento.isnumeric():
            digitos = digitos + 1
        letras = letras + 1
    print("Numeros = ", digitos, "/ Letras =", letras)
    return digitos, letras
contar_numeros_letras(cadena)

# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
print('BUCLES Y FUNCIONES: Ejercicio 22')
lista = [2, 2, 3, 4, 5]
def sumar_numeros_lista(lista):
    suma = lista[0]
    a = len(lista)
    for numero in range(1, a):
        suma = suma + lista[numero]
    print("La suma de los números de la lista es igual a", suma)
    return suma
sumar_numeros_lista(lista)

# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
print('BUCLES Y FUNCIONES: Ejercicio 23')
lista = [1, 1, 1, 2, 3, 4]
def contar_repeticiones(lista):
    recuento = {}
    for dato in lista:
        if dato not in recuento:
            recuento[dato] = 0
        recuento[dato] = recuento[dato] + 1
    print(recuento)
    return(recuento)

def mayor(recuento):
    mayor = 0
    claves = list(recuento.keys())
    valores = list(recuento.values())
    for dato in recuento:
        if recuento[dato] > mayor:
            mayor = recuento[dato]
            dato_mayor = claves[valores.index(mayor)]
    print("El elemento más común en la lista es:", dato_mayor)
    return dato_mayor

def elemento_mas_comun(lista):
    recuento = (contar_repeticiones(lista))
    mayor(recuento)

elemento_mas_comun(lista)

# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
print('BUCLES Y FUNCIONES: Ejercicio 24')
num = 2
def tabla_multiplicar_10 (num):
    tabla_multiplicar = {}
    i = 1
    for i in range(11):
        producto = i * num
        tabla_multiplicar[i] = producto
    print(tabla_multiplicar)
tabla_multiplicar_10(num)

# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
print('BUCLES Y FUNCIONES: Ejercicio 25')
cadena = 'prueba'
def apariciones_cadena(cadena):
    caracteres = {}
    for caracter in cadena:
        if caracter not in caracteres:
            caracteres[caracter] = 0
        caracteres[caracter] = caracteres[caracter] + 1
    print(caracteres)
    return caracteres
apariciones_cadena(cadena)

# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
print('BUCLES Y FUNCIONES: Ejercicio 26')
lista1 = [1, 3, 5, 7, 10]
lista2 = [1, 4, 5, 20]
def no_comunes(lista1, lista2):
    lista_comunes = []
    for elemento in lista1:
        if elemento not in lista2:
            lista_comunes.append(elemento)
    for elemento in lista2:
        if elemento not in lista1:
            lista_comunes.append(elemento)
    print("Los elementos no comunes en ambas listas son:",lista_comunes)
    return lista_comunes
no_comunes(lista1, lista2)

# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.

''' ¿qué diferencia hay entre este ejercicio y el ejercicio 3 del bloque BUCLES Y FUNCIONES? '''

# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
print('BUCLES Y FUNCIONES: Ejercicio 28')
num = 10
def obtener_pares_menores(num):
    pares=[]
    par = 0
    while par < num:
        par = par + 2
        pares.append(par)
    print("Los números pares menores o iguales a ", num, "son ", pares)
    return pares
def cuadrado(pares):
    cuadrados_pares = []
    for par in pares:
        cuadrado = par * par
        cuadrados_pares.append(cuadrado)
    print("Los cuadrados de los numeros pares menores o iguales a ", num, "son ", cuadrados_pares)
    return cuadrados_pares
sumar_numeros_lista(cuadrado(obtener_pares_menores(num)))

# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
print('BUCLES Y FUNCIONES: Ejercicio 29')
lista = [1, 2, 4, 4, 5, 4, 2]
def promedio(lista):
    print(len(lista))
    promedio = sumar_numeros_lista(lista) / len(lista)
    print(promedio)
    return promedio
promedio(lista)

# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
print('BUCLES Y FUNCIONES: Ejercicio 30')
lista = ['hola', 'palabras', 'rio', 'ordenador']
def contar_letras(cadena):
    letras = 0
    for letra in cadena:
        letras = letras + 1
    return(letras)
def diccionario_letras_cadena(lista):
    longitud = {}
    for cadena in lista:
        if cadena not in longitud:
            longitud[cadena] = 0
        longitud[cadena] = contar_letras(cadena)
    print(longitud)
    return longitud
def cadena_mas_larga(lista):
    longitud = diccionario_letras_cadena(lista)
    mayor = 0
    cadenas = list(longitud.keys())
    longitud_cadena = list(longitud.values())
    for cadena in longitud:
        if longitud[cadena] > mayor:
            mayor = longitud[cadena]
            cadena_mayor = cadenas[longitud_cadena.index(mayor)]
    print("La cadena más larga de la lista es:", cadena_mayor)
    return cadena_mayor
cadena_mas_larga(lista)

# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
print('BUCLES Y FUNCIONES: Ejercicio 31')
num = 10
def calcular_primos(num):
    contador = 2
    num_primos = 1
    lista_primos = []
    while num_primos <= num:
        if es_primo(contador):
            lista_primos.append(contador)
            num_primos = num_primos + 1
        contador = contador + 1
    print(lista_primos)
calcular_primos(num)

# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
print('BUCLES Y FUNCIONES: Ejecicio 32')
cadena = 'esta cadena es una prueba'
def identificar_palabras(cadena):
    palabras = []
    palabra = ''
    for elemento in cadena:
        if elemento != ' ':
            palabra += elemento
        else:
            palabras.append(palabra)
            palabra = ''
    palabras.append(palabra)
    return palabras
def frase_al_reves(cadena):
    palabras = identificar_palabras(cadena)
    palabras_invertidas = invertir_lista(palabras)
    frase_invertida = ''
    for palabra in palabras_invertidas:
        frase_invertida = frase_invertida + palabra + ' '
    print("La cadena con las palabras en orden inverso es:",frase_invertida)
frase_al_reves(cadena)


# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
print('BUCLES Y FUNCIONES: Ejercicio 33')
tupla = ('hola', 'camion', 'arbol', 'celeste')
def obtener_ultimo_elemento(tupla):
    diccionario = {}
    i = len(tupla)
    for cadena in tupla:
        ultima_letra = cadena[-1]
        diccionario[cadena] = ultima_letra
    return diccionario
def buscar_tuplas(tupla):
    diccionario = obtener_ultimo_elemento(tupla)
    lista_ultimos = list(diccionario.values())
    lista_ultimos_ordenada = ordenar_lista(lista_ultimos)
    tuplas_ordenadas = []
    for elemento in lista_ultimos_ordenada:
        valor = list(diccionario.keys())[list(diccionario.values()).index(elemento)]
        tuplas_ordenadas.append(valor)
    print("Las tuplas ordenadas según su último elemento son:", tuplas_ordenadas)
    return tuplas_ordenadas
buscar_tuplas(tupla)

# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.

''' ¿que diferencia hay entre este ejercicio y el ejercicio 5 de este bloque?'''

# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
''' ¿qué diferencia hay entre este ejercicio y el ejercicio 3 del bloque funciones?'''