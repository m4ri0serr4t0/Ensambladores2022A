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
    file = askopenfile(mode='r', filetypes=[('Archivos Ensamblador', '*.asm')])
    if file is None:
        mostrarAdvertencia()  # Muestra advertencia
    else:
        content = file.read()
        messagebox.showinfo("Código", content)
        listaElementos = separarElementos(content)
        stringElementos = ''
        for i in listaElementos:
            stringElementos += i + '\n'

        textoElementos = ''
        textoTotal = ''
        for i in listaElementos:
            palabra = str(i)
            palabra2 = listaElementos[listaElementos.index(palabra) + 1]
            newtextRegistros = palabra[0:2]
            if (newtextRegistros in registers) or (newtextRegistros in (i.lower() for i in
                                                                        registers)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
                textoTotal += (newtextRegistros + '  ------> Es Registro' + '\n')

            if (palabra in instrucciones) or (palabra in (i.lower() for i in
                                                          instrucciones)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
                textoTotal += (palabra + '------> Es Instrucción' + '\n')
            if palabra2 == 'segment':
                textoElementos += (palabra + ' ' + palabra2 + '\n')
            else:

                if validarComentario(palabra) and palabra != 'segment':
                    textoElementos += (palabra + '\n')

                else:
                    pass

        ventanaElementos = Tk()
        ventanaElementos.geometry()
        ventanaElementos.title('Elementos')
        ventanaElementos.iconbitmap('icon/asm.ico')

        labelTitulo = Label(ventanaElementos, text='El programa tiene los siguientes elementos:', fg="blue")
        labelTitulo.pack(side=TOP)

        textElementos = Text(ventanaElementos, height=50, width=30)
        scrollbar = Scrollbar(ventanaElementos, command=textElementos.yview())
        scrollbar.pack(side=RIGHT)

        textElementos.insert(END, textoElementos)
        textElementos.configure(state='disabled')  # SOLO LECTURA
        textElementos.pack(side=LEFT)

        ventanaIdentificacion = Tk()  # Ventana que se desplegará para mostrar la identificación de los elementos
        ventanaIdentificacion.geometry()
        ventanaIdentificacion.title('Identificación de elementos')
        ventanaIdentificacion.iconbitmap('icon/asm.ico')

        labelTituloIdentificacion = Label(ventanaIdentificacion,
                                          text='Los elementos del programa tienen las siguiente clasificación: '
                                               '                                                               ',
                                          fg='black')
        labelIdentificacion = Label(ventanaIdentificacion, text=textoTotal, fg="blue")
        labelTituloIdentificacion.pack(side=TOP)
        labelIdentificacion.pack(side=BOTTOM)




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

        label = Label(self.root, text="Explorador de Archivos", width=100, height=4, fg="black")
        label.pack()

        btn = Button(self.root, text='Abrir Archivo', background="green", command=lambda: open_file())
        btn.pack()

        btn2 = Button(self.root, text='   Salir    ', background="red", command=lambda: exit())
        btn2.pack()

        label3 = Label(self.root, text="Equipo 1 2022-A", width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.root.mainloop()
