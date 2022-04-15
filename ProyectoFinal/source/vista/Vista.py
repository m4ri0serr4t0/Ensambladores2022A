from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile


def open_file():
    file = askopenfile(mode='r', filetypes=[('Archivos Ensamblador', '*.asm')])
    if file is None:
        mostrarError()
    else:
        content = file.read()
        messagebox.showinfo("Código", content)
        e = separarElementos(content)
        newtext = ''
        for i in e:
            texto = str(i)
            newtext += (texto+'\n')
        ventana2 = Tk()
        ventana2.geometry('200x300')
        ventana2.title('Elementos')
        labelElementos = Label(ventana2, text=newtext)
        labelElementos.pack()


def separarElementos(lista):
    new_list = lista.split()
    return new_list


def mostrarError():
    messagebox.showwarning("Error", "Selecciona un archivo")


# def leerArchivo():
# file = 'C:programa/archivoensambaldor'
# contenido = file.read()
# def leerpossa


class Ventana:

    def __init__(self, root, title, geometry, icon):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # sizexsize
        self.root.iconbitmap(icon)

        label = Label(self.root, text="Explorador de Archivos", width=100, height=4, fg="black")
        label.pack()

        btn = Button(self.root, text='Abrir Archivo Para Lectura', background="green", command=lambda: open_file())
        btn.pack()



        btn2 = Button(self.root, text='   Salir    ', background="red", command=lambda: exit())
        btn2.pack()

        label3 = Label(self.root, text="Equipo 1 2022-A", width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.root.mainloop()


