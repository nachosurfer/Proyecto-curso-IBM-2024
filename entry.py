from tkinter import *  # Importo todos los módulos de creación de ventanas gráficas

# Crear la raíz de la ventana
raiz = Tk()
raiz.title("Mi Aplicación")
raiz.geometry("300x200")

# Crear una etiqueta para el cuadro de texto
etiqueta = Label(raiz, text="Ingrese su texto:")
etiqueta.pack()

# Crear un cuadro de texto
cuadroTexto = Entry(raiz)
cuadroTexto.pack()

# Función para mostrar el texto del cuadro de texto
def mostrar_texto():
    texto = cuadroTexto.get()
    print(texto)  # O realizar alguna otra acción

# Crear un botón que llama a la función mostrar_texto
boton = Button(raiz, text="Mostrar texto", command=mostrar_texto)
boton.pack()

# Iniciar el bucle principal de la ventana
raiz.mainloop()
