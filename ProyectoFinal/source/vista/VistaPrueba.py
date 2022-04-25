from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import re
import ply.lex as lex

#lex.py se utiliza para dividir una cadena de entrada.
tokens = [
    'PSEUDOINSTRUCCIONES',
    'INSTRUCCIONES',
    'SIMBOLO',
    'REGISTRO',
    'CONSTANTE_NUMERICA_DECIMAL',
    'CONSTANTE_NUMERICA_HEXADECIMAL',
    'CONSTANTE_NUMERICA_BINARIA']

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

segmentos = ['.data segment', '.stack segment', '.code segment']

def open_file():
    file = askopenfile(mode='r',
                       filetypes=[('Archivos Ensamblador', '*.asm')])  # Abirendo el archivo desde un file explorer
    if file is None:  # Si el usuario no selecciona algún archivo
        mostrarAdvertencia()  # Muestra advertencia
    else:
        content = file.read()  # Lee el contenido del archivo
        mostrarCodigo(content)
        segments=[]
        lineas = content.split('\n')
        for i in lineas:
            for j in segmentos:
                if re.search(j, i):
                    segments.append(j)
        print(segments)






def t_REGISTRO(t):
    r'[a-zA-Z]{2}'
    if t.value or t.value.upper() in registers:
        # .type = t.value
        return t


def t_INSTRUCCIONES(t):
    r'[a-zA-Z]*'
    if t.value or t.value.upper() in instrucciones:
        t.type = t.value
        return t


def t_COMENTARIO(t):
    r'\;.*'
    return t


def t_SIMBOLO(t):
    pass


def t_CONSTANTE_NUMERICA_DECIMAL(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CONSTANTE_NUMERICA_HEXADECIMAL(t):
    r'[0-9A-Fa-f][0-9A-Fa-f]*'
    return t


def mostrarAdvertencia():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")


def mostrarCodigo(content):
    ventanaCodigo = Tk()
    ventanaCodigo.geometry()
    ventanaCodigo.title('Código')
    ventanaCodigo.iconbitmap('icon/asm.ico')
    labelTituloCodigo = Label(ventanaCodigo, text='El código tiene el siguiente contenido: ', font='terminal',
                              fg="blue")
    labelTituloCodigo.grid(row=0, column=1)

    textCodigo = Text(ventanaCodigo, font='terminal', height=100, width=100)
    # scrollbarCodigo = Scrollbar(ventanaCodigo, command=textCodigo.yview())
    # scrollbarCodigo.grid(row=1, column=3)

    textCodigo.insert(END, content)
    textCodigo.configure(state='disabled')  # SOLO LECTURA
    textCodigo.grid(row=1, column=1)

    btn = Button(ventanaCodigo, text='Mostrar Elementos', font='Terminal', background="green", command=lambda: None)
    btn.grid(row=1, column=2)

    btn2 = Button(ventanaCodigo, text='Identificar Elementos', font='Terminal', background="red", command=lambda: None)
    btn2.grid(row=1, column=3)


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
