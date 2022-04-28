from tkinter.filedialog import askopenfile

from ProyectoFinal.Python.source.modelo.Archivo import Archivo
from ProyectoFinal.Python.source.vista.vistaNew import Vista


def _abrirArchivo():
    file = askopenfile(mode='r',
                       filetypes=[('Archivos Ensamblador', '*.asm')])  # Abirendo el archivo desde un file explorer
    return file


def _leerArchivo(file):
    content = file.read()
    return content



if __name__ == '__main__':
    #archivo = Archivo()

    ventanaPrincipal = Vista() #Ventana Principal del explorador


    ventanaPrincipal.elementosVentanaPrincipal(_abrirArchivo())

    ventanaPrincipal.mainloop()
   #