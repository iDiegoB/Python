#GUI - Graphical User Interface

#TKinter - TK interface

#Importamos el módulo de tkinter 
import tkinter as tk

#Importar paquete ttk, componentes de tkinter
from tkinter import ttk

#Creamos un objeto usando la clase TK
ventana = tk.Tk()

#Modificamos el tamaño de la ventana(pixeles)
ventana.geometry('600x400')


#Cambiamos el nombre de la ventana(pixeles)
ventana.title('Nueva ventana')

#Configuracion del icono de la aplicacion
ventana.iconbitmap('assets/icono.ico')

#Definir el evento click
def evento_click():
    #Reescribe el boton
    boton1.config(text="Boton presionado")
    print('Evento click')
    #Creamos un nuevo boton y lo mostramos
    boton2= ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()

#Creamos un Boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)

#Utilizar el pack layout manager, para mostrar el boton de la ventana
boton1.pack()
#Iniciamos la ventana (Esta linea la ejecutamos al final)
#Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()
