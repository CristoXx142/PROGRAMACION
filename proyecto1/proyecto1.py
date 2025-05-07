#PROYECTO 1. CALCULADORA DE EDAD
AÑO = 2025
Nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿En que año naciste?"))

edad = AÑO - edad
print("Hola", Nombre, "tienes", edad, "años")

if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
