#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk

class HelloWorld(ttk.Frame):
    '''Clase que define una ventana que muestra un "Hello World"'''
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        #Creamos un label
        saludo = ttk.Label(self, text='Hello World!!', anchor='center')
        #Lo agregamos a la ventana
        saludo.pack(fill='both', expand=True)
        #Agregamos este frame a la ventana principal (Top level window)
        self.pack(fill='both', expand=True)

        #Configuramos la ventan principal
        top = self.winfo_toplevel()
        top.title('Hello World')
        top.minsize(width=300, height=200)

if __name__ == '__main__':
    app = HelloWorld()
    app.mainloop()