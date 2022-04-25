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
             'BP', 'SP', 'SI', 'DI'
             ]
# Definiendo las instrucciones asignadas

instrucciones = ['AAA', 'MOVSB', 'CLD', 'PUSHF', 'DAA',
                 'STOSB', 'DEC', 'INT', 'DIV', 'POP',
                 'ADC', 'LES', 'SHL', 'ADD', 'JA',
                 'JNC', 'LOOPNE', 'JNAE', 'JZ', 'JLE']

pseudoinstrucciones = ['.data segment', '.DATA SEGMENT', '.code segment'
    , '.CODE SEGMENT', '.stack segment''.STACK SEGMENT', 'ends', 'ENDS',
                       'byte ptr', 'BYTE PTR', 'world ptr', 'WORLD PTR', 'db', 'DB', 'equ',
                       'EQU', '.code', '.CODE', '.stack', '.STACK', '.data', '.DATA'
                       ]


# lo hizo juan

def open_file():
    """
    Esta función abre el archivo tipo asm y ejecuta las ventana para el analizador léxico""
    :return:
    """
    file = askopenfile(mode='r',
                       filetypes=[('Archivos Ensamblador', '*.asm')])  # Abirendo el archivo desde un file explorer
    if file is None:  # Si el usuario no selecciona algún archivo
        mostrarAdvertencia()  # Muestra advertencia
    else:
        content = file.read()  # Lee el contenido del archivo

        ventanaCodigo = Tk()
        ventanaCodigo.geometry()
        ventanaCodigo.title('Código')

        labelTituloCodigo = Label(ventanaCodigo, text='El código tiene el siguiente contenido: ', font='terminal',
                                  fg="blue")
        labelTituloCodigo.grid(row=0, column=1)

        textCodigo = Text(ventanaCodigo, font='terminal', height=100, width=100)
        # scrollbarCodigo = Scrollbar(ventanaCodigo, command=textCodigo.yview())
        # scrollbarCodigo.grid(row=1, column=3)

        textCodigo.insert(END, content)
        textCodigo.configure(state='disabled')  # SOLO LECTURA
        textCodigo.grid(row=1, column=1)

        listaElementos = separarPalabras(content)
        elements = []
        lineas = content.split('\n')
        lineasSinComentario = []
        for x in lineas:

            posicionComentario = x.find(';')
            if posicionComentario == -1:
                lineasSinComentario.append(x)

            else:
                linea = x[0:posicionComentario]
                lineasSinComentario.append(linea)

        stringElementos = ''
        stringLineas = ''

        for i in lineasSinComentario:
            stringLineas == i + '\n'
            print(i)


        for j in lineasSinComentario:
            lineaPalabras = j.split()

            for z in lineaPalabras:
                elements.append(z)



        for i in elements:
            stringElementos += i + '\n'

        textoElementos = ''
        textoTotal = ''

        constanteCaracter=[]

        for a in lineasSinComentario:
            constante = validadConstantesCaracter(a)
            constanteCaracter.append(constante)
            if constante != None:
                print(constante)


        for i in elements:

            i.replace(',', '')  # recorrido analizador de cada una de las palabras

            palabra = str(i)
            palabra2 = elements[elements.index(palabra) + 1]
            newtextRegistros = palabra[0:2]
            if (newtextRegistros in registers) or (newtextRegistros in (i.lower() for i in
                                                                        registers)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
                textoTotal += (newtextRegistros + '  ------> Es Registro' + '\n')

            if (palabra in instrucciones) or (palabra in (i.lower() for i in
                                                          instrucciones)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
                textoTotal += (palabra + '  ------> Es Instruccion' + '\n')
            if (palabra.isdigit()):
                textoTotal += (palabra+ '  ------> Es Constante Numerica Decimal'+ '\n')
            if (palabra.endswith('H') or palabra.endswith('h')):
                textoTotal += (palabra+ '  ------> Es Constante Numerica Hexadecimal' + '\n')
            if (validaBinario(palabra)):
                textoTotal += (palabra + '  ------> Es Constante Numerica Binaria' + '\n')

            if validarSimbolo(palabra):
                textoTotal += (palabra + '------> Es Simbolo' + '\n')
            if palabra2 == 'segment':
                textoElementos += (palabra + ' ' + palabra2 + '\n')


            else:

                if validarComentario(palabra) and palabra != 'segment':
                    textoElementos += (palabra + '\n')


                else:
                    pass

        # a = windowElementos(textoElementos)
        botonCodigo = Button(ventanaCodigo, text='Siguiente', font='terminal', background='green',
                             command=lambda: windowElementosIdentificacion(textoElementos, textoTotal))
        botonCodigo.grid(row=0, column=2)


# def mostrarCodigo(content):

# def agregarBotonIdentificarElementos(ventana, elementos, total):


def windowElementosIdentificacion(contenido, contenido2):
    ventanaElementos = Tk()
    ventanaElementos.geometry('700x700')
    ventanaElementos.title('Elementos')
    #ventanaElementos.iconbitmap('icon/asm.ico')

    labelTitulo = Label(ventanaElementos, text='El programa tiene los siguientes elementos:', font='terminal',
                        fg="blue")
    labelTitulo.pack(side=TOP)

    textElementos = Text(ventanaElementos, font='terminal', height=50, width=40)
    scrollbar = Scrollbar(ventanaElementos, command=textElementos.yview())
    scrollbar.pack(side=RIGHT)

    textElementos.insert(END, contenido)
    textElementos.configure(state='disabled')  # SOLO LECTURA
    textElementos.pack(side=LEFT)

    ventanaIdentificacion = Tk()
    ventanaIdentificacion.geometry()
    ventanaIdentificacion.title('Identificación de elementos')
    ventanaIdentificacion.iconbitmap('icon/asm.ico')

    labelTituloIdentificacion = Label(ventanaIdentificacion,
                                      text='Los elementos del programa tienen las siguiente clasificación: '
                                           '                                                               ',
                                      font='terminal',
                                      fg='black')
    labelTituloIdentificacion.pack(side=TOP)

    textIdentificación = Text(ventanaIdentificacion, font='terminal', height=100, width=80, foreground='blue')
    scrollbarIdentificacion = Scrollbar(ventanaIdentificacion, command=textIdentificación.yview())
    scrollbarIdentificacion.pack(side=RIGHT)

    textIdentificación.insert(END, contenido2)
    textIdentificación.configure(state='disabled')  # SOLO LECTURA
    textIdentificación.pack(side=LEFT)


def separarPalabras(lista):
    new_lista = lista.split()
    return new_lista


def validarSegmento(string1, string2):
    if string1.startswith('.') and string2.startswith('segment'):
        return True

def validadConstantesCaracter(linea):
    indexComilla = linea.find('"')
    if indexComilla == -1:
        pass
    else:
        constante = linea[indexComilla:]
        return constante


def validaBinario(string):
    # set function convert string
    # into set of characters .
    p = set(string)

    # declare set of '0', '1' .
    s = {'0', '1'}

    # check set p is same as set s
    # or set p contains only '0'
    # or set p contains only '1'
    # or not, if any one condition
    # is true then string is accepted
    # otherwise not .
    if len(string) >= 2 and (s == p or p == {'0'} or p == {'1'}) and (string.endswith('B') or string.endswith('b')):
        return True
    else:
        return False


def validarComentario(string):
    if not string.startswith(';'):
        return True


def validarSimbolo(string):  # Solo etiquetas
    if string.endswith(':'):
        return True


def validarRegistros(string):
    pass


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

        btn2 = Button(self.root, text='   Salir    ', font='Fixedsys', background="red",
                      command=lambda: self.root.destroy())  # lo hizo juan
        btn2.pack()

        label3 = Label(self.root, text="Equipo 1 2022-A", font='Fixedsys', width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.root.mainloop()


# _rutaIcono = 'asm.ico'
if __name__ == '__main__':
    root = Tk()
    vista = Vista(root, 'Analizador Lexicografico', '600x200')
