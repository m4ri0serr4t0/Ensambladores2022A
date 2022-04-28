from tkinter import *
import tkinter as tk
from tkinter import ttk


class Vista(tk.Tk):

    def __init__(self) -> None:
        super().__init__()


    def elementosVentanaPrincipal(self, comandoAbrir):
        self.geometry()
        self.title('Código')
        label = Label(self, text="Analizador Lexicográfico", font='Fixedsys', width=100, height=4, fg="black")
        label.pack()

        btn = Button(self, text='Abrir Archivo', font='Fixedsys', background="green", command=lambda: comandoAbrir)
        btn.pack()

        btn2 = Button(self, text='   Salir    ', font='Fixedsys', background="red",
                      command=lambda: self.destroy())  # lo hizo juan
        btn2.pack()

        label3 = Label(self, text="Equipo 1 2022-A", font='Fixedsys', width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.mainloop()

    def desplegarTexto(self, texto):
        scroll = tk.Scrollbar(self)
        textField = Text(self, font='terminal', height=50, width=40)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        textField.pack(side=tk.LEFT, fill=tk.Y)
        scroll.config(command=textField.yview)
        textField.config(yscrollcommand=scroll.set)

        textField.insert(END, texto)
        textField.configure(state='disabled')  # SOLO LECTURA
        textField.pack(side=LEFT)
