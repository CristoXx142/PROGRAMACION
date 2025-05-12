

#Sumar números ingresados por el usuario hasta que ingrese 0.

contador = 0
while contador <=5:
    print("Numero: ", contador)
    contador += 1

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").

numero_aleatorio = 50
numero_ingresado = int(input("Adivina el número entre 1 y 100: "))
while numero_ingresado != numero_aleatorio:
    if numero_ingresado < numero_aleatorio:
        print("El número es mayor.")
    elif numero_ingresado > numero_aleatorio:
        print("El número es menor.")
    numero_ingresado = int(input("Intenta nuevamente: ")) 
else:
         print("Adivinaste")
    
#Validar contraseña (repetir hasta que coincida con una guardada).

contraguardada = "123"
contraingresada = ""
while contraingresada != contraguardada:
    contraingresada = input("Ingrese la contraseña: ")
    if contraingresada != contraguardada:
        print("Incorrecta")
print("correcta")

#Simular un cajero automático (menú: retirar, depositar, salir).
saldo = 1000
opcion = 0
while opcion != 3:
    print("Menú Cajero Automático")
    print("1. Retirar")
    print("2. Depositar")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cantidad = int(input("Digite la cantidad: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiraste {cantidad}. Tu saldo es: {saldo}")
        else:
            print("Saldo insuficiente")
    elif opcion == 2:
        cantidad = int(input("Digite la cantidad a depositar: "))
        saldo += cantidad
        print(f"Depositaste {cantidad}. Saldo actual: {saldo}")
    elif opcion == 3:
        print("Gracias por utilizar nuestro servicio")
    else:
        print("Intente nuevamente")
    

#Calcular la raíz cuadrada por aproximación (método babilónico).

numero = float(input("Ingrese un número : "))
babilonico = 1e-10
aprox = numero / 2.0
maprox = (aprox + numero / aprox) / 2.0

while (maprox - aprox) ** 2 >= babilonico ** 2:
    aprox = maprox
    maprox = (aprox + numero / aprox) / 2.0

print(f"La raíz cuadrada aproximada de {numero} es {maprox}")

#Contar dígitos de un número entero (ej: 456 → 3).

n = int(input("Ingrese un número entero: "))
cont = 0
if n == 0:
    cont = 1
else:
    while n != 0:
        n //= 10
        cont += 1
print(f"El número {n} tiene {cont} dígitos.")

#Generar la secuencia de Fibonacci hasta un límite.

limite = int(input("Ingrese el límite para la secuencia de Fibonacci: "))
a, b = 0, 1
print("Secuencia de Fibonacci:")
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
print()

# Encontrar números primos en un rango dado.

inicio = int(input("inicio del rango: "))
fin = int(input("fin del rango: "))

print(f"Primos entre {inicio} y {fin}:")
for numero in range(inicio, fin + 1):
    if numero > 1:
        for divisor in range(2, numero):
            if numero % divisor == 0:
                break
        else:
            print(numero)

#Simular un temporizador (contar regresivamente desde N).

import time
n = int(input("Ingrese el número para la alarma: "))
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("se acabó el tiempo")

#Leer archivos línea por línea hasta fin de archivo.

arch = input("Ingrese el archivo: ")
archivo = open(arch, 'r')
linea = archivo.readline()
while linea:
    print(linea, end='')
    linea = archivo.readline()
archivo.close()




