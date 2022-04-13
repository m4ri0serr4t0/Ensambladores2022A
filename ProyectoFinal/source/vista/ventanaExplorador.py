from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfile


def open_file():
    # file = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo",
    # filetypes=(("Ensamblador", "*.asm*"), ("Todos los archivos", "*.*")))
    file = askopenfile(mode='r', filetypes=[('Archivos Ensamblador', '*.asm')])
    # label.config(text='Se ha abierto el archivo con la ubicación: '+file)

    if file is not None:
        content = file.read()
        messagebox.showinfo("Codigo", content)


    # if file is not None:
    # content = file.read()
    # print(content)


ventana = Tk()
ventana.geometry('600x200')
ventana.title('Explorador de Archivos')
ventana.iconbitmap("icon/asm.ico")

etiqueta = Label(ventana, text="Explorador de Archivos", width=100, height=4, fg="black")
etiqueta.pack()

btn = Button(ventana, text='Abrir Archivo', background="green", command=lambda: open_file())
btn.pack()

btn2 = Button(ventana, text='   Salir    ', background="red", command=lambda: exit())
btn2.pack()

etiqueta2 = Label(ventana, text="Equipo 1 2022-A", width=100, height=4, fg="black")
etiqueta2.pack()
mainloop()
