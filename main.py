from lista_de_tareas import ListaDeTareas.  # importa la clase ListaDeTareas del módulo lista de tareas

def mostrar_menu():     #imprime el menu de opciones para que el usuario pueda interactuar
    print("\nLista de Tareas")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():    #punto de entrada principal del programa. Aquí se crea una instancia ListaDeTareas la cuál gestiona las tareas.
    lista_de_tareas = ListaDeTareas()

    while True:   #iniamos bucle infinito hasta que el usuario decida salir del programa
        mostrar_menu()   #llamamos a la función. mostrar_menu para que nos muestre las opciones que tenemos
        opcion = input("Selecciona una opción: ") #mediante el input recogemos la opción seleccionada

        if opcion == "1":   #si elijo la opción 1 me pide que ingrese la descripción de la tarea y llama al método agregar_tarea de lisita_de_tarea
            descripcion = input("Descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":  #si es la opción 2 me pide la opción que quiero marcar, convertimos la entrada a entero y llamamos a marcar_tarea_completada
            try:
                indice = int(input("Índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_tarea_completada(indice)
            except ValueError: #si la conversión falla se atrapa la excepción en ValueError y nos muestra un mensaje de error
                print("Por favor, introduce un número válido.")
        elif opcion == "3": #si elegimos la opción 3 llamamos al método listar_tareas
            lista_de_tareas.listar_tareas()
        elif opcion == "4": #si elegimos la 4 se le pide que ingrese el indice de la opción a eliminar. Se convierte a entero y se llama al método eliminar_tarea
            try:
                indice = int(input("Índice de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:   #si la conversión falla se atrapa la excepción en ValueError y nos muestra un mensaje de error
                print("Por favor, introduce un número válido.")
        elif opcion == "5": #si elegimos la opción 5 salimos del progrma mediente un break.
            print("Saliendo del programa...\n")
            
            break
        else:  #si elegimos una opción diferente a las opciones anteriores nos dará un mensaje de "opción no válida"
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__": #Con este bloque nos aseguramos de que el script se ejecuta directamente (que no es importado) y llama a la función main().
    main()

