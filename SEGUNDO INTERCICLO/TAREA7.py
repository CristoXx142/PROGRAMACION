def computepay(horas, tarifa):
    if horas > 40:
        hora = horas - 40
        salario = (40 * tarifas) + (hora * tarifas * 1.5)
    else:
        salario = horas * tarifas
    return salario

hora = float(input("Ingrese las horas: "))
tarifas = float(input("Ingrese la tarifa: "))
salario = computepay(hora, tarifas)
print("Salario:", salario)