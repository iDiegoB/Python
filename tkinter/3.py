import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('assets/icono.ico')

#width cantidad de caracteres que ocupa la caja
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')#tk.RIGHT, tk.LEFT
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)#tk.RIGHT, tk.LEFT
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state= tk.NORMAL)#tk.RIGHT, tk.LEFT
entrada1.grid(row=0,column=0)
#insert agrega un texto
entrada1.insert(0, 'Introduce una cadena de texto')
entrada1.insert(tk.END, '.')
#entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())
    boton1.config(text= 'Enviado')
    #eliminar el contenido
    #entrada1.delete(0, tk.END)
    
    #Seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    #hacer efectiva la seleccion
    entrada1.focus()

#Creamos un boton
boton1= ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()