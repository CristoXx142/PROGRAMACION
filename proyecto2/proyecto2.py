#Proyecto 2: Contador de Vocales
#Objetivo: Usar bucles for y condicionales con cadenas (str).
#Instrucciones para los estudiantes:
#1.	Pide al usuario que escriba una frase o palabra.
#2.	Recorre la cadena con un for y cuenta cuántas vocales tiene.
#3.	Muestra cuántas veces aparece cada vocal (a, e, i, o, u).

palabra = input("Escribe una frase o palabra: ")
contador = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for letra in palabra:
    if letra in contador:
        contador[letra] += 1
print("Cantidad de cada vocal:")
for vocal, cantidad in contador.items():
    print(f"{vocal}: {cantidad}")
