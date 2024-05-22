from tkinter import Tk, Label

root = Tk()
root.title("Verificación de Tkinter")
root.geometry("300*200")

label = Label(root, text="Tkinter está funcionando")
label.pack()

root.mainloop()
