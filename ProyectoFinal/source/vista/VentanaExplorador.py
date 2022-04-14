from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfile

from self import self

from ProyectoFinal.source.vista.Ventana import Ventana


def open_file():
    file = askopenfile(mode='r', filetypes=[('Archivos Ensamblador', '*.asm')])
    if file is not None:
        content = file.read()
        messagebox.showinfo("Codigo", content)


class VentanaExplorador(Ventana):

    def __init__(self, root, title, geometry, icon):
        super().__init__(root, title, geometry, icon)

        label = Label(self.root, text="Explorador de Archivos", width=100, height=4, fg="black")
        label.pack()
        btn = Button(self.root, text='Abrir Archivo', background="green", command=lambda: open_file())
        btn.pack()
        btn2 = Button(self.root, text='   Salir    ', background="red", command=lambda: exit())
        btn2.pack()
        Ventana.mainloop()

