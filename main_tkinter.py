import tkinter as tk
from tkinter import messagebox

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

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas.pop(indice - 1)
        else:
            print("Índice fuera de rango.")

    def marcar_tarea_completada(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()
        else:
            print("Índice fuera de rango.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        for indice, tarea in enumerate(self.tareas, start=1):
            print(f"{indice}. {tarea}")

class Aplicacion:
    def __init__(self, root):
        self.lista_de_tareas = ListaDeTareas()

        self.root = root
        self.root.title("Lista de Tareas")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.descripcion_label = tk.Label(self.frame, text="Descripción de la tarea:")
        self.descripcion_label.grid(row=0, column=0, padx=5, pady=5)

        self.descripcion_entry = tk.Entry(self.frame, width=40)
        self.descripcion_entry.grid(row=0, column=1, padx=5, pady=5)

        self.agregar_button = tk.Button(self.frame, text="Agregar tarea", command=self.agregar_tarea)
        self.agregar_button.grid(row=0, column=2, padx=5, pady=5)

        self.tareas_listbox = tk.Listbox(self.frame, width=60, height=15)
        self.tareas_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.marcar_completada_button = tk.Button(self.frame, text="Marcar como completada", command=self.marcar_completada)
        self.marcar_completada_button.grid(row=2, column=0, padx=5, pady=5)

        self.eliminar_button = tk.Button(self.frame, text="Eliminar tarea", command=self.eliminar_tarea)
        self.eliminar_button.grid(row=2, column=1, padx=5, pady=5)

        self.salir_button = tk.Button(self.frame, text="Salir", command=root.quit)
        self.salir_button.grid(row=2, column=2, padx=5, pady=5)

    def agregar_tarea(self):
        descripcion = self.descripcion_entry.get()
        if descripcion:
            self.lista_de_tareas.agregar_tarea(descripcion)
            self.actualizar_lista()
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La descripción no puede estar vacía")

    def marcar_completada(self):
        try:
            indice = self.tareas_listbox.curselection()[0] + 1  # Ajustamos el índice para que sea 1 basado
            self.lista_de_tareas.marcar_tarea_completada(indice)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea")

    def eliminar_tarea(self):
        try:
            indice = self.tareas_listbox.curselection()[0] + 1  # Ajustamos el índice para que sea 1 basado
            self.lista_de_tareas.eliminar_tarea(indice)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea")

    def actualizar_lista(self):
        self.tareas_listbox.delete(0, tk.END)
        for i, tarea in enumerate(self.lista_de_tareas.tareas, start=1):
            estado = "Completada" if tarea.completada else "Pendiente"
            self.tareas_listbox.insert(tk.END, f"{i}. {tarea.descripcion} - {estado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
