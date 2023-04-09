import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x130')
        self.title('Login')
        self.resizable(0,0)#No hacer mas grande la      self

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()
        
    def _crear_componentes(self):
        usuario = tk.Label(self, text='Usuario:')
        usuario.grid(row=0, column=0, columnspan=1, sticky=tk.E, padx=5,pady=5)

        self.usuario_entry = ttk.Entry(self, width=35, justify=tk.CENTER)
        self.usuario_entry.grid(row=0, column = 1, sticky=tk.W,padx=5, pady=5)
        
        

        contra = tk.Label(self, text='Password:')
        contra.grid(row=1, column=0, columnspan=1, sticky=tk.E,padx=5,pady=5)

        self.contra_entry = ttk.Entry(self, width=35, show='*', justify=tk.CENTER)
        self.contra_entry.grid(row=1, column = 1, sticky=tk.W,padx=5, pady=5)
        
        boton_login = ttk.Button(self, text='Login', command=self._login_command)
        boton_login.grid(row=3, column=0, columnspan=2)
    def _login_command(self):
        messagebox.showinfo('Login', 'Usuario: ' + self.usuario_entry.get() + '\nContraseña: ' + self.contra_entry.get())

#Ejecutar la ventana
if __name__== '__main__':
    login_ventana = Login()
    login_ventana.mainloop()