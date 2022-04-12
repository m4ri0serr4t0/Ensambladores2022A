from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

ventana = Tk()
ventana.geometry('300x100')
ventana.title('Explorador de Archivos')
ventana.iconbitmap("icon/asm.ico")


# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfile(mode='r', filetypes=[('Archivos Ensamblador', '*.asm')])
    if file is not None:
        content = file.read()
        print(content)

#comentario
btn = Button(ventana, text='Abrir Archivo', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

btn2 = Button(ventana, text='Exit', command=lambda: exit())
btn2.pack(side=BOTTOM, pady=10)
mainloop()
