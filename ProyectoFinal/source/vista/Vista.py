from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

from ProyectoFinal.source.modelo.Registro import Registro

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
        ventanaCodigo.iconbitmap('icon/asm.ico')
        labelTituloCodigo = Label(ventanaCodigo, text='El código tiene el siguiente contenido: ', font='terminal',fg="blue")
        labelTituloCodigo.pack(side=TOP)

        textCodigo = Text(ventanaCodigo, font='terminal', height=100, width=100)
        scrollbarCodigo = Scrollbar(ventanaCodigo, command=textCodigo.yview())
        scrollbarCodigo.pack(side=RIGHT)

        textCodigo.insert(END, content)
        textCodigo.configure(state='disabled')  # SOLO LECTURA
        textCodigo.pack(side=LEFT)

        listaElementos = separarElementos(content)
        stringElementos = ''
        for i in listaElementos:
            stringElementos += i + '\n'

        textoElementos = ''
        textoTotal = ''
        for i in listaElementos:  # recorrido analizador de cada una de las palabras
            palabra = str(i)
            palabra2 = listaElementos[listaElementos.index(palabra) + 1]
            newtextRegistros = palabra[0:2]
            if (newtextRegistros in registers) or (newtextRegistros in (i.lower() for i in
                                                                        registers)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
                textoTotal += (newtextRegistros + '  ------> Es Registro' + '\n')

            if (palabra in instrucciones) or (palabra in (i.lower() for i in
                                                          instrucciones)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
                textoTotal += (palabra + '------> Es Instrucción' + '\n')
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
        botonCodigo.pack(side=RIGHT)
        windowIdentificacion(textoTotal)



def windowElementosIdentificacion(contenido, contenido2):
    ventanaElementos = Tk()
    ventanaElementos.geometry()
    ventanaElementos.title('Elementos')
    ventanaElementos.iconbitmap('icon/asm.ico')

    labelTitulo = Label(ventanaElementos, text='El programa tiene los siguientes elementos:', font='terminal',fg="blue")
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

    textIdentificación = Text(ventanaIdentificacion, font='terminal', height=50, width=30, foreground='blue')
    scrollbarIdentificacion = Scrollbar(ventanaIdentificacion, command=textIdentificación.yview())
    scrollbarIdentificacion.pack(side=RIGHT)

    textIdentificación.insert(END, contenido2)
    textIdentificación.configure(state='disabled')  # SOLO LECTURA
    textIdentificación.pack(side=LEFT)


def windowIdentificacion(contenido):
    # Ventana que se desplegará para mostrar la identificación de los elementos
    pass


def validarSegmento(string1, string2):
    if string1.startswith('.') and string2.startswith('segment'):
        return True


def validarRegistro(listaRegistros, string):
    if string.startswith('AX'):
        listaRegistros.append(string)
    if string.startswith('BX'):
        listaRegistros.append(string)


def validarComentario(string):
    if not string.startswith(';'):
        return True


def validarSimbolo(string):  # Solo etiquetas
    if string.endswith(':'):
        return True


def validarRegistros(string):
    r = Registro()
    registers = r.registros()


def separarElementos(lista):
    new_list = lista.split()
    return new_list


def mostrarAdvertencia():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")


class Vista:

    def __init__(self, root, title, geometry, icon):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # sizexsize
        self.root.iconbitmap(icon)

        label = Label(self.root, text="Analizador Lexicográfico", font='Fixedsys', width=100, height=4, fg="black")
        label.pack()

        btn = Button(self.root, text='Abrir Archivo', font='Fixedsys', background="green", command=lambda: open_file())
        btn.pack()

        btn2 = Button(self.root, text='   Salir    ', font='Fixedsys', background="red", command=lambda: exit())
        btn2.pack()

        label3 = Label(self.root, text="Equipo 1 2022-A", font='Fixedsys', width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.root.mainloop()
