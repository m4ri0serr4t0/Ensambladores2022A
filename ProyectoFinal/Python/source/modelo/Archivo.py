from tkinter import messagebox
from tkinter.filedialog import askopenfile


class Archivo:

    def __init__(self) -> None:
        super().__init__()

    def abrirArchivo(self):
        file = askopenfile(mode='r',
                           filetypes=[('Archivos Ensamblador', '*.asm')])  # Abirendo el archivo desde un file explorer
        return file

    def leerArchivo(self, file):
        content = file.read()
        return content


if __name__ == '__main__':
    archivo = Archivo()
    contenido = archivo.abrirArchivo()
    codigo = archivo.leerArchivo(contenido)
    print(contenido)


