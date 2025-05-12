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

contraguardada = "segura123"
contraingresada = ""
while contraingresada != contraguardada:
    contraingresada = input("Ingrese la contraseña: ")
    if contraingresada != contraguardada:
        print("Incorrecta")
print("correcta")

#Simular un cajero automático (menú: retirar, depositar, salir).
saldo = 1000
1 = print("retirar")
2 = print("depositar")
3 = print("salir")
opcion = int(input("Seleccione una opción: "))
while opcion != 3:
    if opcion == 1:
        cantidad = int(input("Cantidad a retirar: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiraste {cantidad}. Saldo actual: {saldo}")
        else:
            print("Su saldo es insuficiente.")
   
    elif opcion == 2:
        cantidad = int(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
        print(f"Depositaste {cantidad}. Saldo actual: {saldo}")
    else:

        print("Gracias por utilizar nuesstro servicio.")
    

#Calcular la raíz cuadrada por aproximación (método babilónico).

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.





