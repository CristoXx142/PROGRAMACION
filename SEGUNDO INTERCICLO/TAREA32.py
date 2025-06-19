total_general = 0    

with open("compras.txt", "r") as archivo:
    for linea in archivo:
        producto, cantidad, precio = linea.strip().split(',')
        subtotal = int(cantidad) * float(precio)
        total_general += subtotal
        print(f"{producto}: {cantidad} x ${precio} = ${subtotal:.2f}")

print(f"\nTotal a pagar: ${total_general:.2f}")
        