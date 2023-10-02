from tkinter import *
import os
from pathlib import Path
from os import system
from shutil import *
from tkinter import ttk

#crear ventana principal
ventana = Tk()
ventana.title("Recetario")
ventana.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\libro-de-recetas.ico")
ventana.geometry("480x220")
ventana.configure(bg="#90ADC6")

#panel principal
panel_principal = Frame(ventana, bg="#90ADC6", width=500)
panel_principal.pack()

# crear la carpeta para guardar las recetas
carpeta =  "C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\Recetas"

existe = os.path.exists(carpeta)

if not existe:
    os.makedirs(carpeta)

#funciones para cada opcion
lista_funciones_abiertas = []

def leer_receta():
    #crear ventana leer
    global ventana_leer
    ventana_leer = Tk()
    ventana_leer.title("Leer receta")
    ventana_leer.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\libro-de-recetas.ico")
    lista_funciones_abiertas.append(ventana_leer)

    #panel principal
    panel_nuevo = Frame(ventana_leer)
    panel_nuevo.pack()

    #ruta de categorias
    ruta_cat = Path("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\Recetas")

    #funcion para controlar el cuadro para elegir la receta
    def elegir_receta(event):
        contenido = cuadro_categoria.get()
        global ruta_receta
        ruta_receta = Path(ruta_cat, contenido)
        lista_recetas = []
        cont = 0
        for r in Path(ruta_receta).glob("*txt"):
            lista_recetas.append(Path(r).stem)  
            cont +=1
        
        if cont == 0:
            lista_recetas.append("No hay recetas")

        cuadro_receta["values"] = lista_recetas

    #abrir archivo y mostrar
    def abrir_archivo():
        contenido = cuadro_receta.get() + ".txt"
        ruta_abrir = Path(ruta_receta, contenido)
        etiqueta_contenido.config(text= open(ruta_abrir).read())
        open(ruta_abrir).close()

    #panel para eleccion de categoria
    panel_categoria = Frame(panel_nuevo)
    panel_categoria.pack(side=LEFT)

    #etiqueta categoria
    etiqueta_categoria = Label(panel_categoria, font=("arial", 12), text="Elige tu categoria: ")
    etiqueta_categoria.grid(row=0, column=0)

    #cuadro para categoria
    lista_carpetas_cat = []
    categoria_var = StringVar()
    cuadro_categoria = ttk.Combobox(panel_categoria, textvariable=categoria_var, font=("arial", 12))
    cont = 0
    for c in os.listdir(ruta_cat):
        lista_carpetas_cat.append(c)
        cont +=1
    if cont == 0:
        lista_carpetas_cat.append("No hay categorias dispnibles")

    cuadro_categoria["values"]= lista_carpetas_cat
    cuadro_categoria.bind("<<ComboboxSelected>>", elegir_receta)
    cuadro_categoria.grid(row=0, column=1)


    #panel para la receta
    panel_receta = Frame(panel_nuevo)
    panel_receta.pack(side=LEFT)

    #etiqueta receta
    etiqueta_receta = Label(panel_receta, font=("arial", 12), text="Elige tu receta: ")
    etiqueta_receta.grid(row=0, column=0)

    #cuadro para receta
    receta_var = StringVar()
    cuadro_receta = ttk.Combobox(panel_receta, font=("arial", 12), textvariable=receta_var)
    cuadro_receta.bind("<<ComboBoxSelected>>", abrir_archivo)
    cuadro_receta.grid(row=0, column=1)

    #boton
    boton = Button(panel_receta, text="Leer", command=abrir_archivo)
    boton.grid(row=0, column=2, padx=2)

    #panel para ver el contenido
    panel_contenido = Frame(ventana_leer, background="#90ADC6")
    panel_contenido.pack(side=BOTTOM, expand=True, fill="both")

    #etiqueta para contenido
    etiqueta_contenido = Label(panel_contenido, font=("arial", 12), height=20, background="#90ADC6", anchor="nw")
    etiqueta_contenido.grid(row=0, column=0)

    #cerrar la ventana
    def sacar_de_lista():
        indice = lista_funciones_abiertas.index(ventana_leer)
        lista_funciones_abiertas.remove(lista_funciones_abiertas[indice])
        ventana_leer.destroy()

    ventana_leer.protocol("WM_DELETE_WINDOW", sacar_de_lista)

    #loop de ventana leer
    ventana_leer.mainloop()

def crear_receta():
    #crear ventana crear receta
    global ventana_crear_rec
    ventana_crear_rec = Tk()
    ventana_crear_rec.title("Crear receta")
    ventana_crear_rec.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\libro-de-recetas.ico")
    lista_funciones_abiertas.append(ventana_crear_rec)
    #panel principal
    panel_nuevo = Frame(ventana_crear_rec)
    panel_nuevo.pack()

    #ruta de categorias
    ruta_cat = Path("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\Recetas")

    
    
    def listar():
        cont = 0
        lista.delete(0, "end")
        for r in ruta_receta.glob("*txt"):
            lista.insert(END, Path(r).stem)
            cont +=1

        if cont == 0:
            lista.insert(END, "No hay recetas")


    #funcion para controlar el cuadro para elegir la receta
    def elegir_receta(event):
        global contenido1
        contenido1 = cuadro_categoria.get()
        global ruta_receta
        ruta_receta = Path(ruta_cat, contenido1)
        lista_recetas = []
        cont = 0
        for r in Path(ruta_receta).glob("*txt"):
            lista_recetas.append(Path(r).stem)  
            cont +=1
        
        if cont == 0:
            lista_recetas.append("No hay recetas")
        listar()

       

    #abrir archivo y mostrar
    def crear_archivo():
        contenido = cuadro_receta.get() + ".txt"
        contenido2 = cuadro_cont_rec.get("1.0", "end")

        ruta_crear = Path(ruta_receta, contenido)
        escribir = open(ruta_crear, "w")
       
        escribir.write(contenido2)

        cuadro_cont_rec.delete("1.0", "end")

        cuadro_receta.delete(0, "end")
        cuadro_receta.focus()

        etiqueta_contenido.config(text="***************SU RECETA SE CREO EXITOSAMENTE*************")
        listar()
    
     #panel para la receta
    panel_receta = Frame(panel_nuevo)
    panel_receta.pack(side=TOP)

    #etiqueta categoria
    etiqueta_categoria = Label(panel_receta, font=("arial", 12), text="Elige tu categoria: ")
    etiqueta_categoria.grid(row=0, column=0)

    #cuadro para categoria
    lista_carpetas_cat = []
    categoria_var = StringVar()
    cuadro_categoria = ttk.Combobox(panel_receta, textvariable=categoria_var, font=("arial", 12))
    cont = 0
    for c in os.listdir(ruta_cat):
        lista_carpetas_cat.append(c)
        cont +=1
    if cont == 0:
        lista_carpetas_cat.append("No hay categorias dispnibles")

    cuadro_categoria["values"]= lista_carpetas_cat
    cuadro_categoria.bind("<<ComboboxSelected>>", elegir_receta)
    cuadro_categoria.grid(row=0, column=1)

    #etiqueta receta
    etiqueta_receta = Label(panel_receta, font=("arial", 12), text="Nombre de receta: ")
    etiqueta_receta.grid(row=0, column=2)

    #cuadro para receta
    receta_var = StringVar()
    cuadro_receta = Entry(panel_receta, textvariable=receta_var)
    cuadro_receta.grid(row=0, column=3)

    #etiqueta para contenido de la receta
    etiqueta_cont_rec = Label(panel_receta, font=("arial", 12), text="Escribe la receta: ")
    etiqueta_cont_rec.grid(row=0, column=4)

    #cuadro para receta
    cuadro_cont_rec = Text(panel_receta, width=20, height=10)
    cuadro_cont_rec.grid(row=0, column=5)

    #boton
    boton = Button(panel_receta, text="Crear", command=crear_archivo)
    boton.grid(row=0, column=6, padx=2)

    #panel para la lista
    panel_lista = Frame(panel_nuevo, background="#333652")
    panel_lista.pack(side=BOTTOM, fill="both")

    #cuadro y etiqueta para lista
    etiqueta_lista = Label(panel_lista, font=("arial", 12), text="Recetas: ", anchor="e")
    etiqueta_lista.grid(row=0, column=0, padx=420, pady=2)
    lista = Listbox(panel_lista, font=("arial", 12), height=5)
    lista.grid(row=1, column=0)

    #panel para ver el contenido
    panel_contenido = Frame(ventana_crear_rec, background="#90ADC6")
    panel_contenido.pack(side=BOTTOM, expand=True, fill="both")

    #etiqueta para contenido
    etiqueta_contenido = Label(panel_contenido, font=("arial", 12), height=20, background="#90ADC6", anchor="nw")
    etiqueta_contenido.grid(row=0, column=0, padx=200)

        #cerrar la ventana
    def sacar_de_lista():
        indice = lista_funciones_abiertas.index(ventana_crear_rec)
        lista_funciones_abiertas.remove(lista_funciones_abiertas[indice])
        ventana_crear_rec.destroy()

    ventana_crear_rec.protocol("WM_DELETE_WINDOW", sacar_de_lista)

    #loop de ventana crear receta
    ventana_crear_rec.mainloop()

def crear_categoria():
    #crear ventana crear categoria
    global ventana_crear_cat
    ventana_crear_cat = Tk()
    ventana_crear_cat.title("Crear categoria")
    ventana_crear_cat.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\libro-de-recetas.ico")


    lista_funciones_abiertas.append(ventana_crear_cat)


    #panel principal
    panel_nuevo = Frame(ventana_crear_cat)
    panel_nuevo.pack()

    #ruta de categorias
    ruta_cat = Path("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\Recetas")

    def listar():

        etiqueta_lista = Label(panel_lista, font=("arial", 12), text="Categorias: ", anchor="e")
        etiqueta_lista.grid(row=0, column=0, padx=150, pady=2)
        lista = Listbox(panel_lista, font=("arial", 12), height=5)
        for c in os.listdir(ruta_cat):
            lista.insert(END, c)

        lista.grid(row=1, column=0)
        

    #crear categoria
    def crear_categoria():
        contenido = cuadro_categoria.get()
        ruta_crear = Path(ruta_cat, contenido)
        

        for car in os.listdir(ruta_cat):
            if car == contenido:
                etiqueta_contenido.config(text="********* ESTA CATEGORIA YA ESTA CREADA *********")
                cuadro_categoria.delete(0,"end")
                cuadro_categoria.focus()

        if contenido == "":
            etiqueta_contenido.config(text="************* DEBES LLENAR EL CAMPO *************")

        elif os.listdir(ruta_cat) == [] or car != contenido:
            os.mkdir(ruta_crear)
            etiqueta_contenido.config(text="***** SU CATEGORIA SE HA CREADO EXITOSAMENTE *****")
            cuadro_categoria.delete(0,"end")
            cuadro_categoria.focus()
        
        listar()

        

    #panel para eleccion de categoria
    panel_categoria = Frame(panel_nuevo, bg="#74BDCB")
    panel_categoria.pack(side=TOP)

    #etiqueta categoria
    etiqueta_categoria = Label(panel_categoria, font=("arial", 12), text="Nombre de categoria: ")
    etiqueta_categoria.grid(row=0, column=0, pady=10)

    #cuadro para categoria
    lista_carpetas_cat = []
    categoria_var = StringVar()
    cuadro_categoria = Entry(panel_categoria, textvariable=categoria_var, font=("arial", 12))
    cuadro_categoria.focus()
    cuadro_categoria.grid(row=0, column=1)

    #boton
    boton = Button(panel_categoria, text="Crear", command=crear_categoria)
    boton.grid(row=0, column=2, padx=2)

    #panel para la lista
    panel_lista = Frame(panel_nuevo, background="#333652")
    panel_lista.pack(side=TOP, fill="both")

    #panel para ver el contenido
    panel_contenido = Frame(ventana_crear_cat, background="#90ADC6")
    panel_contenido.pack(side=BOTTOM, expand=True, fill="both")

    #etiqueta para contenido
    etiqueta_contenido = Label(panel_contenido, font=("arial", 12), height=20, background="#90ADC6", anchor="nw")
    etiqueta_contenido.grid(row=0, column=0)
    listar()

    #cerrar la ventana
    def sacar_de_lista():
        indice = lista_funciones_abiertas.index(ventana_crear_cat)
        lista_funciones_abiertas.remove(lista_funciones_abiertas[indice])
        ventana_crear_cat.destroy()

    ventana_crear_cat.protocol("WM_DELETE_WINDOW", sacar_de_lista)

    #loop de ventana crear categoria
    ventana_crear_cat.mainloop()

def eliminar_receta():
    #crear ventana eliminar receta
    global ventana_eliminar_rec
    ventana_eliminar_rec = Tk()
    ventana_eliminar_rec.title("Eliminar receta")
    ventana_eliminar_rec.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\libro-de-recetas.ico")
    lista_funciones_abiertas.append(ventana_eliminar_rec)




    #panel principal
    panel_nuevo = Frame(ventana_eliminar_rec)
    panel_nuevo.pack()

    #ruta de categorias
    ruta_cat = Path("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\Recetas")

    #funcion para controlar el cuadro para elegir la receta
    def elegir_receta(event):
        contenido = cuadro_categoria.get()
        global ruta_receta
        ruta_receta = Path(ruta_cat, contenido)
        lista_recetas = []
        cont = 0
        for r in Path(ruta_receta).glob("*txt"):
            lista_recetas.append(Path(r).stem)  
            cont +=1
        
        if cont == 0:
            lista_recetas.append("No hay recetas")

        cuadro_receta["values"] = lista_recetas

    def actualizar_campo():
        contenido = cuadro_categoria.get()
        global ruta_receta
        ruta_receta = Path(ruta_cat, contenido)
        lista_recetas = []
        cont = 0
        for r in Path(ruta_receta).glob("*txt"):
            lista_recetas.append(Path(r).stem)  
            cont +=1
        
        if cont == 0:
            lista_recetas.append("No hay recetas")

        cuadro_receta["values"] = lista_recetas
        

    #eleminar archivo
    def eleminar_archivo():
        contenido = cuadro_receta.get() + ".txt"
        ruta_eliminar = Path(ruta_receta, contenido)
        os.remove(ruta_eliminar)
        etiqueta_contenido.config(text="***** SU RECETA SE HA ELIMINADO EXITOSAMENTE *****")

        actualizar_campo()
        cuadro_receta.delete(0, "end")

    #panel para eleccion de categoria
    panel_categoria = Frame(panel_nuevo)
    panel_categoria.pack(side=LEFT)

    #etiqueta categoria
    etiqueta_categoria = Label(panel_categoria, font=("arial", 12), text="Elige tu categoria: ")
    etiqueta_categoria.grid(row=0, column=0)

    #cuadro para categoria
    lista_carpetas_cat = []
    categoria_var = StringVar()
    cuadro_categoria = ttk.Combobox(panel_categoria, textvariable=categoria_var, font=("arial", 12))
    for c in os.listdir(ruta_cat):
        lista_carpetas_cat.append(c)

    cuadro_categoria["values"]= lista_carpetas_cat
    cuadro_categoria.bind("<<ComboboxSelected>>", elegir_receta)
    cuadro_categoria.grid(row=0, column=1)


    #panel para la receta
    panel_receta = Frame(panel_nuevo)
    panel_receta.pack(side=LEFT)

    #etiqueta receta
    etiqueta_receta = Label(panel_receta, font=("arial", 12), text="Elige tu receta: ")
    etiqueta_receta.grid(row=0, column=0)

    #cuadro para receta
    receta_var = StringVar()
    cuadro_receta = ttk.Combobox(panel_receta, font=("arial", 12), textvariable=receta_var)
    cuadro_receta.bind("<<ComboBoxSelected>>", eleminar_archivo)
    cuadro_receta.grid(row=0, column=1)

    #boton
    boton = Button(panel_receta, text="Eliminar", command=eleminar_archivo)
    boton.grid(row=0, column=2, padx=2)

    #panel para ver el contenido
    panel_contenido = Frame(ventana_eliminar_rec, background="#90ADC6")
    panel_contenido.pack(side=BOTTOM, expand=True, fill="both")

    #etiqueta para contenido
    etiqueta_contenido = Label(panel_contenido, font=("arial", 12), height=20, background="#90ADC6", anchor="nw")
    etiqueta_contenido.grid(row=0, column=0)

    #cerrar la ventana
    def sacar_de_lista():
        indice = lista_funciones_abiertas.index(ventana_eliminar_rec)
        lista_funciones_abiertas.remove(lista_funciones_abiertas[indice])
        ventana_eliminar_rec.destroy()

    ventana_eliminar_rec.protocol("WM_DELETE_WINDOW", sacar_de_lista)

    #loop de ventana eliminar receta
    ventana_eliminar_rec.mainloop()

def eliminar_categoria():
    #crear ventana eliminar categoria
    global ventana_eliminar_cat
    ventana_eliminar_cat = Tk()
    ventana_eliminar_cat.title("Eliminar categoria")
    ventana_eliminar_cat.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\libro-de-recetas.ico")
    lista_funciones_abiertas.append(ventana_eliminar_cat)


    #panel principal
    panel_nuevo = Frame(ventana_eliminar_cat)
    panel_nuevo.pack()

    #ruta de categorias
    ruta_cat = Path("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Aplicaciones_de_escritotio\\Recetario\\Recetas")
        
    def actualizar():
        global lista_carpetas_cat
        lista_carpetas_cat = []
        cont = 0
        for c in os.listdir(ruta_cat):
            lista_carpetas_cat.append(c)
            cont +=1
        if cont == 0:
            lista_carpetas_cat.append("No hay categorias dispnibles")

        cuadro_categoria["values"]= lista_carpetas_cat

    #eleminar archivo
    def eliminar_categoria():
        contenido = cuadro_categoria.get()
        ruta_eliminar = Path(ruta_cat, contenido)
        if contenido == "":
            etiqueta_contenido.config(text="**************** EL CAMPO ESTA VACIO ****************")
        else:
            rmtree(ruta_eliminar)
            actualizar()
            etiqueta_contenido.config(text="***** SU CATEGORIA SE HA ELIMINADO EXITOSAMENTE *****")
            cuadro_categoria.delete(0,"end")


    #panel para eleccion de categoria
    panel_categoria = Frame(panel_nuevo)
    panel_categoria.pack(side=LEFT)

    #etiqueta categoria
    etiqueta_categoria = Label(panel_categoria, font=("arial", 12), text="Elige tu categoria: ")
    etiqueta_categoria.grid(row=0, column=0)

    #cuadro para categoria
    lista_carpetas_cat = []
    categoria_var = StringVar()
    cuadro_categoria = ttk.Combobox(panel_categoria, textvariable=categoria_var, font=("arial", 12))

    for c in os.listdir(ruta_cat):
        lista_carpetas_cat.append(c)

    cuadro_categoria["values"]= lista_carpetas_cat
    cuadro_categoria.grid(row=0, column=1)

    #boton
    boton = Button(panel_categoria, text="Eliminar", command=eliminar_categoria)
    boton.grid(row=0, column=2, padx=2)

    #panel para ver el contenido
    panel_contenido = Frame(ventana_eliminar_cat, background="#90ADC6")
    panel_contenido.pack(side=BOTTOM, expand=True, fill="both")

    #etiqueta para contenido
    etiqueta_contenido = Label(panel_contenido, font=("arial", 12), height=20, background="#90ADC6", anchor="nw")
    etiqueta_contenido.grid(row=0, column=0)


    #cerrar la ventana
    def sacar_de_lista():
        indice = lista_funciones_abiertas.index(ventana_eliminar_cat)
        lista_funciones_abiertas.remove(lista_funciones_abiertas[indice])
        ventana_eliminar_cat.destroy()

    ventana_eliminar_cat.protocol("WM_DELETE_WINDOW", sacar_de_lista)

    #loop de ventana eliminar categoria
    ventana_eliminar_cat.mainloop()


def finalizar_programa():

    for ven in lista_funciones_abiertas:
        ven.destroy()
    ventana.destroy()

#accion para el boton de cierre
ventana.protocol("WM_DELETE_WINDOW", finalizar_programa)
    
#ventana para mostrar las opciones
lista_menu = ["Leer receta", "Crear receta", "Crear categoria", "Eliminar receta", "Eliminar categoria", "Finalizar programa"]
lista_funciones = [leer_receta, crear_receta, crear_categoria, eliminar_receta, eliminar_categoria, finalizar_programa]
cont = 0
columna = 0
fila = 0

for l in lista_menu:

    boton = Button(panel_principal, text=lista_menu[cont], width=20, height=2, font=("arial", 15), command=lista_funciones[cont])
   
    boton.grid(row=fila, column=columna, padx=2, pady=5)
    
    cont += 1
    fila += 1

    if cont == 3:
        fila = 0
        columna = 1
    


#loop de la ventana principal
ventana.mainloop()