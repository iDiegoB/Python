import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejor de Grid')
ventana.iconbitmap('assets/icono.ico')

#Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)

ventana.columnconfigure(0, weight=2)
ventana.columnconfigure(1, weight=5)

def evento1():
    boton1.config(text='Boton 1 presionado')
def evento2():
    boton2.config(text='Boton 2 presionado')
def evento4():
    boton4.config(text='Boton 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')

#Definimos dos botones
boton1 = ttk.Button(ventana, text='Boton 1', command= evento1)
boton1.grid(row = 0 , column=0, sticky='NSWE')

# sticky N(ARRIBA), E(DERECHA), S(ABAJO) ,W(IZQUIERDA)

boton2 = ttk.Button(ventana, text='Boton 2', command= evento2)
boton2.grid(row = 1, column=0, sticky= 'NSWE')

boton3 = ttk.Button(ventana, text='Boton 3')
boton3.grid(row = 0, column=1, sticky= 'NSWE')
#boton3.pack()
boton4 = tk.Button(ventana, text='Boton 4', command= evento4)
boton4.grid(row = 1, column=1, sticky= 'NSWE')

ventana.mainloop()