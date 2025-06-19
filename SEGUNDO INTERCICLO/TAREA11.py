#	Conversor de temperatura (Celsius a Fahrenheit y viceversa)
def convertir(valor, temp):
    if temp == 'C':
        return str((valor * 9/5) + 32) + " Fahrenheit"
    elif temp == 'F':
        return str((valor - 32) * 5/9) + " Celsius"
valor = float(input("Ingrese el valor de la temperatura: "))
temp = input("Ingrese: C para cambiar de C a F, F para cambiar de F a C: ").upper()
print("El valor convertido es: ", convertir(valor, temp))

