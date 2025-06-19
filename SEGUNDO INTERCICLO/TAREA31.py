with open("tareas.txt", "r") as archivo:  
    tareas = archivo.readlines()           
    for i, tarea in enumerate(tareas, 1):   
        print(f"{i}. {tarea.strip()}")       
print("Total de tareas:", len(tareas))  