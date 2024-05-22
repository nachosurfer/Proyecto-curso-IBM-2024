from tarea import Tarea

class ListaDeTareas:
    def __init__(self):     #creo el constructor
        self.tareas = []    #inicializo la variable de clase "tareas" a una lista vacía

    def agregar_tarea(self, descripcion):   #creo un método "agregar_tarea"
        nueva_tarea = Tarea(descripcion)    
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):   #creo un método eliminar_tarea
            self.tareas.pop(indice - 1)         #me posciono al final de la fina y elimino el último dato
        else:
            print("Índice fuera de rango.")

    def marcar_tarea_completada(self, indice):  #creo un método para marcar la tarea
        if 1 <= indice <= len(self.tareas):     #comparo el tamaño de mi lista
            self.tareas[indice - 1].marcar_completada()
        else:
            print("Índice fuera de rango.")

    def listar_tareas(self):            #creo un método para listar las tareas
        if not self.tareas:
            print("No hay tareas en la lista.")
        for indice, tarea in enumerate(self.tareas, start=1):   #itero mi lista
            print(f"{indice}. {tarea}")
