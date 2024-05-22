from lista_de_tareas import ListaDeTareas

def mostrar_menu():
    print("\nLista de Tareas")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    lista_de_tareas = ListaDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                indice = int(input("Índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_tarea_completada(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "3":
            lista_de_tareas.listar_tareas()
        elif opcion == "4":
            try:
                indice = int(input("Índice de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "5":
            print("Saliendo del programa...\n")
            
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()

