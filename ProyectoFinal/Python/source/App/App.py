from ProyectoFinal.source.vista.Vista import Vista
from tkinter import *

from ProyectoFinal.source.vista.Vista import Vista

_rutaIcono = 'icon/asm.ico'
if __name__ == '__main__':
    root = Tk()
    vista = Vista(root, 'Analizador Lexicográfico', '600x200', _rutaIcono)
