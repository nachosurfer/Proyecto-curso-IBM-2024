import tkinter as tk

def on_nuevo():
    print("Nuevo archivo")

def on_guardar():
    print("Guardar archivo")

def on_cerrar():
    print("Cerrar aplicación")
    root.quit()

root = tk.Tk()

# Configurar la ventana
root.title("Mi aplicación")
root.geometry("300x300")

# Crear y configurar la barra de menú
barraMenu = tk.Menu(root)
root.config(menu=barraMenu)

# Crear el submenú "Archivo"
archivoMenu = tk.Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", command=on_nuevo)
archivoMenu.add_command(label="Guardar", command=on_guardar)
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=on_cerrar)
archivoMenu.add_command(label="Salir", command=on_cerrar)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

# Crear el submenú "Edición"
archivoEdicion = tk.Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

# Crear el submenú "Herramientas"
archivoHerramientas = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

# Añadir un label de prueba en la ventana
label = tk.Label(root, text="Esta es una prueba")
label.pack(pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()
