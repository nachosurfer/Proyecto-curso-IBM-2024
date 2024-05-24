from colorama import init, Fore, Style  #importo las funciones necesaria de colorama

init(autoreset=True)  # Inicializa colorama para que los colores se reseteen después de cada impresión

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion  #inicializa la descripción de la tarea
        self.completada = False  #por defecto inicializo la tarea como no completada

    def marcar_completada(self):  # marca la tarea como completada
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente" #define el estado de la tarea según si está completada o no
        return f"{self.descripcion} - {estado}"  # nos devuelve una cadena que describe la tarea y su estado

class ListaDeTareas:    # defino la clase ListaDeTareas, con su constructor y sus módulos.
    def __init__(self):
        self.tareas = []  # inicializa la lista de tareas vacía.

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)  # crea una nueva tarea con la descripción proporcionada
        self.tareas.append(nueva_tarea)  # aquí agregamos con append la tarea a nuestra lista de tareas
        print(f"Tarea agregada: {nueva_tarea}")  # Aquí nos aseguramos que se está añadiendo ya que tuve un problema donde no se añadia a la tabla y así nos aseguramos.

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas): # Verificamos si el índice está dentro del rango de la lista de tareas.
            tarea_a_eliminar = self.tareas[indice - 1]  # aquí pasamos la opción elegido al índice
            confirmacion = input(f"¿Estás seguro de eliminar la tarea '{tarea_a_eliminar.descripcion}'? (s/n): ").lower() # Pido confirmación para no eliminar por error.
            if confirmacion == "s":
                self.tareas.pop(indice - 1) # elimino la tarea en caso afirmativo
                print("Tarea eliminada.")
            else:
                print("No se ha eliminado ninguna tarea.")
        else:
            print("El índice introducido está fuera de rango, por favor intentalo de nuevo.")

    def marcar_tarea_completada(self, indice):
        if 1 <= indice <= len(self.tareas):  # verifica si el índice proporcionado está dentro de rango
            self.tareas[indice - 1].marcar_completada()  # marca la tarea como completada
            print("Tarea marcada como completada.")
        else:
            print("El índice introducido está fuera de rango, por favor intentalo de nuevo.")

    def listar_tareas(self):
        if not self.tareas:  # verifica la lista de tareas está vacía
            print("No hay tareas para mostrar.")
        else:
            print(f"Total de tareas: {len(self.tareas)}")
        for indice, tarea in enumerate(self.tareas, start=1):  #itero sobre la lista para enumerarlas
            if tarea.completada:
                print(f"{indice}. {Fore.GREEN}{tarea}{Style.RESET_ALL}")  # si está completada la pongo verde
            else:
                # print(f"{indice}. {tarea}")
                print(f"{indice}. {Fore.CYAN}{tarea}{Style.RESET_ALL}") # si está sin completar la pinto de cian


def mostrar_menu():
    print()
    menu_width = 40  # Ancho del menú
    title = "Lista de tareas"
    title_length = len(title)
    left_padding = (menu_width - title_length) // 2  # Espaciado izquierdo
    right_padding = menu_width - title_length - left_padding - 2 # Espaciado derecho

    # Imprime el marco superior
    print("╔" + "═" * (menu_width - 2) + "╗")
    # Imprime el título centrado
    print("║" + " " * left_padding + Fore.MAGENTA + title + Style.RESET_ALL + " " * right_padding + "║")
    #print("║" + " " * left_padding + title + " " * right_padding + "║")
    # Imprime el separador
    print("╠" + "═" * (menu_width - 2) + "╣")
    # Imprime las opciones del menú
    print("║" + " " * (menu_width - 2) + "║")
    print("║" + Fore.BLUE + "1. Agregar tarea" + " " * 22 + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "2. Mostrar todas las tareas" + " " * 11 + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "3. Marcar tarea como completada" + " " * 7 + Style.RESET_ALL + "║")
    print("║" + Fore.RED + "4. Eliminar tarea" + " " * 21 + Style.RESET_ALL + "║")
    print("║" + Fore.BLUE + "5. Salir" + " " * 30 + Style.RESET_ALL + "║")
    # Imprime el marco inferior
    print("╚" + "═" * (menu_width - 2) + "╝")


"""                    ****************************IMPRIMIMOS EL MENU PRINCIPAL***********************************

def mostrar_menu():    
    print(Fore.MAGENTA + Style.BRIGHT + "\n                      ------- Lista de Tareas -------")
    print()
    print(Fore.BLUE + "1. Agregar tarea")
    print(Fore.BLUE + "2. Mostrar todas las tareas")
    print(Fore.BLUE + "3. Marcar tarea como completada")
    print(Fore.RED + "4. Eliminar tarea")
    print(Fore.BLUE + "5. Salir")
"""

#                    *****************************PARTE PRINCIPAL DEL PROGRMA*********************************
def main():
    lista_de_tareas = ListaDeTareas() # creamos una instancia de la clase ListaDeTareas()

    while True:
        mostrar_menu()   # aquí mostramos el menu de opciones
        opcion = input("Selecciona una opción: ")  # mediante el input introducimos la opción elegida

        if opcion == "1":   # mediante el condicional if vamos comparando todas las opciones propuestas en el menu para hacer la elección correspondiente
            descripcion = input("Descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)  # llamamos al módulo correspondiente
        elif opcion == "2":
            lista_de_tareas.listar_tareas()
        elif opcion == "3":  # aquí tratamos las excepciones mediante try/except
            try:
                indice = int(input("Índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_tarea_completada(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "4":
            try:
                indice = int(input(Fore.RED + "Índice de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "5":
            print("Saliendo del programa...\n")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":  #verifica si el script se está ejecutando como programa principal
    main()  # llama a la función principal del programa
