#1.	Crear una función multiplicar(x, y) que retorne el producto de dos números.
def multiplicar(x, y):
    agregado = x*y
    return agregado

x= int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
print("la multiplicacion es: ", multiplicar(x, y))

#-------------------------------------------------------

#2.	Crear una función es_par(numero) que retorne True si el número es par.
def es_par(numero):
    return numero % 2 == 0
     
numero = int(input("Ingrese un número: "))
print(es_par(numero))

#-------------------------------------------------------

#3.	Crear una función presentarse(nombre, edad) que imprima un mensaje con tus datos.
def presentarse(nombre, edad):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
presentarse(nombre,edad )