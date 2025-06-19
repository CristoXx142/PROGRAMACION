# 1. Crear una función que imprima un mensaje
def saludo():
    print('¡Hola, mundo!')

# ----------------------------------------

# 2. Función con un argumento
def saludar(nombre):
    print('Hola, ' + nombre)

# ----------------------------------------

# 3. Suma de dos números
def sumar(a, b):
    return a + b

# ----------------------------------------

# 4. Calcular el salario
def computepay(horas, tarifa):
    if horas > 40:
        extra = horas - 40
        pago = 40 * tarifa + extra * tarifa * 1.5
    else:
        pago = horas * tarifa
    return pago

# ----------------------------------------

# 5. Función para determinar el mayor carácter
def mayor_caracter(cadena):
    if cadena:
        return max(cadena)
    else:
        return None

# ----------------------------------------

# 6. Conversión de tipo
def convertir_a_flotante(valor):
    try:
        return float(valor)
    except:
        return None

# ----------------------------------------

# 7. Función que retorna un saludo en diferentes idiomas
def saludo_idioma(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

# ----------------------------------------

# 8. Comprobar si un número es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# ----------------------------------------

# 9. Concatenar cadenas
def concatenar(cad1, cad2):
    return cad1 + cad2

# ----------------------------------------

# 10. Calcular promedio
def promedio(lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma / len(lista)

# ----------------------------------------

# 11. Contar vocales
def contar_vocales(cadena):
    contador = 0
    for c in cadena.lower():
        if c in 'aeiou':
            contador = contador + 1
    return contador

# ----------------------------------------

# 12. Revertir cadena
def invertir(cadena):
    return cadena[::-1]

# ----------------------------------------

# 13. Tabla de multiplicar
def tabla(numero):
    for i in range(1, 11):
        print(str(numero) + " x " + str(i) + " = " + str(numero * i))

# ----------------------------------------

# 14. Función sin parámetros
def mensaje():
    print("Primera línea de mensaje.")
    print("Segunda línea de mensaje.")
    print("Tercera línea de mensaje.")

# ----------------------------------------

# 15. Función que retorne el número más pequeño
def menor_valor(lista):
    if len(lista) == 0:
        return None
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

# ----------------------------------------

# 16. Calcular factorial
def factorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

# ----------------------------------------

# 17. Determinar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# ----------------------------------------

# 18. Repetir una cadena n veces
def repetir(cadena, n):
    return cadena * n

# ----------------------------------------

# 19. Función con múltiples parámetros
def descripcion(nombre, edad, ciudad):
    print(nombre + " tiene " + str(edad) + " años y vive en " + ciudad + ".")

# ----------------------------------------

# 20. Verificar palíndromo
def es_palindromo(cadena):
    cadena_limpia = ""
    for c in cadena:
        if c.isalnum():
            cadena_limpia = cadena_limpia + c.lower()
    if cadena_limpia == cadena_limpia[::-1]:
        return True
    else:
        return False