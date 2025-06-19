# Guardar 5 nombres en un archivo
with open('nombres.txt', 'w') as archivo:  # Abrir el archivo en modo escritura
    for i in range(5):  # Repetir 5 veces
        nombre = input(f"Ingrese el nombre {i+1}: ") # Solicitar un nombre al usuario, con un mensaje que indica el número del nombre 
        archivo.write(nombre + '\n')  # Escribir el nombre en el archivo, seguido de un salto de línea

