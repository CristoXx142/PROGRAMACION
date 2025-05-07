#PROYECTO 5:
# 1.Pide el nombre del usuario
nombredelestudiante = input("Escribe todo tu nombre por favor: ")

# 2. Pide las 4 calificaciones
nota1 = int(input("Ingresa la calificación 1: "))
nota2 = int(input("Ingresa la calificación 2: "))
nota3 = int(input("Ingresa la calificación 3: "))
nota4 = int(input("Ingresa la calificación 4: "))

# 3. Calcula el promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# 4 y 5. Muestra el resultado
if promedio >= 14:
    print(nombredelestudiante + ", tu promedio es", promedio, ". Felicitaciones, aprobaste sigue asi eres grande.")
else:
    print("Lo siento " + nombredelestudiante + ", tu promedio es", promedio, ". Estás reprobado.")
