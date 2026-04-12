tareas = []
completadas = []

def mostrar_menu():
    print("========================================")
    print("           GESTOR DE TAREAS            ")
    print("========================================")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("========================================")

def ver_tareas():
    if len(tareas) == 0:
        print("📭 No hay tareas pendientes")
    else:
        print("\n📋 TAREAS PENDIENTES:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")
    tareas.append(tarea)
    print(f'✅ "{tarea}" agregada')

def completar_tarea():
    ver_tareas()
    if len(tareas) == 0:
        return
    
    try:
        num = int(input("¿Cuál tarea completaste? (número): "))
        tarea = tareas.pop(num - 1)
        completadas.append(tarea)
        print(f'✅ "{tarea}" marcada como completada')
    except:
        print("❌ Número inválido")

def eliminar_tarea():
    ver_tareas()
    if len(tareas) == 0:
        return
    
    try:
        num = int(input("¿Cuál tarea deseas eliminar? (número): "))
        tarea = tareas.pop(num - 1)
        print(f'🗑️ "{tarea}" eliminada')
    except:
        print("❌ Número inválido")

# 🔁 Loop principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida")