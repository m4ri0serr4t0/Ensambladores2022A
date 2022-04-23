from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import re

# Definiendo el conjunto de registros que tiene un 8086
registers = ['AX', 'AH', 'AL',
             'BX', 'BH', 'BL',
             'CX', 'CH', 'CL',
             'DX', 'DH', 'DL',
             'CS', 'DS', 'ES',
             'BP', 'SP', 'SI', 'DI']

# Definiendo las instrucciones asignadas

instrucciones = ['AAA', 'MOVSB', 'CLD', 'PUSHF', 'DAA',
                 'STOSB', 'DEC', 'INT', 'DIV', 'POP',
                 'ADC', 'LES', 'SHL', 'ADD', 'JA',
                 'JNC', 'LOOPNE', 'JNAE', 'JZ', 'JLE']




def open_file():
    file = askopenfile(mode='r',
                       filetypes=[('Archivos Ensamblador', '*.asm')])  # Abirendo el archivo desde un file explorer
    if file is None:  # Si el usuario no selecciona algún archivo
        mostrarAdvertencia()  # Muestra advertencia
    else:
        dataFlag = False

        content = file.read()  # Lee el contenido del archivo
        lineas = re.split(r'[\n]+', content)
        contador = 0
        elementos=[]

        for line in lineas:
            contador += 1
            print("linea#", contador, "\n", line)
            tokens = line.split(" ")
            print("Tokens are ", tokens)
            print("Line#", contador, "properties \n")
            for token in tokens:
                if token in registers or token.upper() in registers:
                    print("Registro son  ", token)

        dataFlag = False
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")


def validarComentario(string):
    r'\;.*'
    return string


def mostrarAdvertencia():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")


class Vista:

    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # sizexsize
        # self.root.iconbitmap(icon)

        label = Label(self.root, text="Analizador Lexicográfico", font='Fixedsys', width=100, height=4, fg="black")
        label.pack()

        btn = Button(self.root, text='Abrir Archivo', font='Fixedsys', background="green", command=lambda: open_file())
        btn.pack()

        btn2 = Button(self.root, text='   Salir    ', font='Fixedsys', background="red", command=lambda: exit())
        btn2.pack()

        label3 = Label(self.root, text="Equipo 1 2022-A", font='Fixedsys', width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.root.mainloop()


# _rutaIcono = 'asm.ico'
if __name__ == '__main__':
    root = Tk()
    vista = Vista(root, 'Analizador Lexicografico', '600x200')
