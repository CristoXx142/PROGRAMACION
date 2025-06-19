from datetime import datetime       

entrada = input("¿Qué quieres registrar hoy?: ") 
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("diario.txt", "a") as archivo:
    archivo.write(f"[{fecha}] {entrada}\n")

print("Entrada guardada.")