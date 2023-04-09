import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('assets/icono.ico')

#etiqueta(label)
etiqueta1= tk.Label(ventana, text='contenido')
etiqueta1.grid(row=1, column=0, columnspan=2)
#Definimos una variable para modificar usando set y leer el get
#entrada_var1 = tk.StringVar(value='Valor por defecto')
entrada1 = ttk.Entry(ventana, width=30)#, textvariable=entrada_var1)#tk.RIGHT, tk.LEFT
entrada1.grid(row=0,column=0)
#insert agrega un texto
#entrada1.insert(0, 'Introduce una cadena de texto')
#entrada1.insert(tk.END, '.')
#entrada1.config(state='readonly')

def enviar():
    #Recuperar informacion a partir de variable asociada con caja de texto
    #boton1.config(text=entrada_var1.get())
    #Modificar con set
    #entrada_var1.set('Cambio...')
    #recuperar informacion
    #print(entrada_var1.get())
    
    #Modificar label
    etiqueta1.config(text=entrada1.get())
    #Messagebox(cajas de mensaje)
    mensaje1= entrada1.get()
    if mensaje1:
        messagebox.showinfo('Info', mensaje1 + ' Informativo')
        messagebox.showerror('Error', mensaje1 + ' Error' )
        messagebox.showwarning('Alerta', mensaje1 + ' alerta')
#Creamos un boton
boton1= ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
ventana.mainloop()