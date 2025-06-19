# Calculadora de propinas

cuenta = float(input("Ingrese el valor de la cuenta: "))

print("Elija el porcentaje de propina:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
opcion = input("Que opcion desea: ")

if opcion == "1":
    porcentaje = 0.10
elif opcion == "2":
    porcentaje = 0.15
elif opcion == "3":
    porcentaje = 0.20   
else:
    print("Opción no válida. Se usará 15% como propina.")
    porcentaje = 0.15

propina = cuenta * porcentaje
total = cuenta + propina
print(f"Cuenta: ${cuenta:.2f}, Propina: ${propina:.2f}, Total: ${total:.2f}")
