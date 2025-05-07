#Proyecto 3: Tabla de Multiplicar Personalizada
#Objetivo: Reforzar el uso de for y int.
#Instrucciones para los estudiantes:
#1.	Pide al usuario un número entre 1 y 12.
#2.	Imprime la tabla de multiplicar de ese número, desde 1 hasta 12.

numero = int(input("Introduce un número entre 1 y 12: "))
if 1 <= numero <= 12:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Por favor, introduce un número entre 1 y 12.")