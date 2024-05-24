class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea agregada: {nueva_tarea}")  # Línea de depuración

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas.pop(indice - 1)
            print("Tarea eliminada.")
        else:
            print("Índice fuera de rango.")

    def marcar_tarea_completada(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()
            print("Tarea marcada como completada.")
        else:
            print("Índice fuera de rango.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            print(f"Total de tareas: {len(self.tareas)}")  # Línea de depuración
        for indice, tarea in enumerate(self.tareas, start=1):
            print(f"{indice}. {tarea}")

def mostrar_menu():
    print("\nLista de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
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
            print()
            lista_de_tareas.listar_tareas()
        elif opcion == "3":
            try:
                indice = int(input("Índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_tarea_completada(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")
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
