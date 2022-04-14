from ProyectoFinal.source.vista.Ventana import Ventana
from tkinter import *

from ProyectoFinal.source.vista.VentanaExplorador import VentanaExplorador

_rutaIcono = 'icon/asm.ico'
if __name__ == '__main__':
    root = Tk()
    ventana = VentanaExplorador(root, 'Explorador de Archivos', '600x200', _rutaIcono)
