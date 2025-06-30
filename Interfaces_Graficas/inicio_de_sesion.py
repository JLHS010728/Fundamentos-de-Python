from tkinter import *
from tkinter import ttk




raiz = Tk()
raiz.title("Inicio de sesión")

marcoPrincipal = ttk.Frame(raiz, padding="5 5 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

Usuario = StringVar()
Contraseña = StringVar()

txtUsuario = ttk.Entry(marcoPrincipal, width=7, textvariable=Usuario)
txtUsuario.grid(column=2, row=3, sticky=(W, E))
txtContraseña = ttk.Entry(marcoPrincipal, width=7, textvariable=Contraseña)
txtContraseña.grid(column=2, row=4, sticky=(W, E))

ttk.Label(marcoPrincipal, textvariable=Usuario).grid(column=1, row=3, sticky=(W, E))
ttk.Label(marcoPrincipal, textvariable=Contraseña).grid(column=1, row=4, sticky=(W, E))
ttk.Button(marcoPrincipal, text="Ingresar").grid(column=2, row=5, sticky=W)

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=1, row=3, sticky=E)
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=1, row=4, sticky=E)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

txtUsuario.focus()
raiz.bind('<Return>', print("Sesión iniciada"))

raiz.mainloop()