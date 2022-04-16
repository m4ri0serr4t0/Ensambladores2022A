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

            if validarComentario(texto):
                newtext += (texto + '\n')
            else:
                pass
        ventana2 = Tk()
        ventana2.geometry('400x400')
        ventana2.title('Elementos')
        labelTitulo = Label(ventana2, text='El programa tiene los siguientes elementos:', fg="blue")
        labelTitulo.grid(row=1, column=4)
        labelElementos = Label(ventana2, text=newtext)
        labelElementos.grid(row=2, column=5)
        btnpag = Button(ventana2, text='Siguiente Página', bg='green')
        btnpag.grid(row=3, column = 6)





def validarComentario(string):
    if not string.startswith(';'):
        return True

def separarElementos(lista):
    new_list = lista.split()
    return new_list


def mostrarError():
    messagebox.showwarning("Error", "Selecciona un archivo")


class Vista:

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
