#Proyecto 4: Juego de Adivinar el Número
#Objetivo: Usar int, if y for con lógica básica de juegos.
#Instrucciones para los estudiantes:
#1.	El programa debe tener un número fijo secreto entre 1 y 10 (por ahora, tú decides el número como profesor, por ejemplo, 7).
#2.	El usuario tiene 3 intentos para adivinarlo.
#.	En cada intento debe ingresar un número.
#4.	Si acierta, muestra: "¡Correcto! Adivinaste el número."
#.	Si falla, muestra si el número es mayor o menor al secreto.

numero_secreto = 7
print("Bienvenido al juego de adivinar el número.")
print("Tienes 3 intentos para adivinar el número secreto entre 1 y 10.")

for intento in range(1,4):
    adivina = int(input("Ingresa tu número: "))
    
    if adivina == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
    elif adivina < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
