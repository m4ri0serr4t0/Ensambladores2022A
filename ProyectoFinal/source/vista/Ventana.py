from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile


def open_file():
    file = askopenfile(mode='r', filetypes=[('Archivos Ensamblador', '*.asm')])
    if file is not None:
        content = file.read()
        messagebox.showinfo("Codigo", content)


class Ventana:

    def __init__(self, root, title, geometry, icon):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # sizexsize
        self.root.iconbitmap(icon)

        Label(self.root, text="Explorador de Archivos", width=100, height=4, fg="black").pack()

        btn = Button(self.root, text='Abrir Archivo', background="green", command=lambda: open_file())
        btn.pack()
        btn2 = Button(self.root, text='   Salir    ', background="red", command=lambda: exit())
        btn2.pack()

        self.root.mainloop()

