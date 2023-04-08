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
entrada1.config(state='readonly')
ventana.mainloop()