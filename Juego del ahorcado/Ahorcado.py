from tkinter import *
from random import *
from PIL import Image, ImageTk

#PALABRAS QUE TIENE ALMACENADAS EL PROGRAMA

palabras = ["PerrO CALiente", "Cabeza", "Elefante", "Computadora", "Perro caliente", "Universidad", "Caballero","Queso", 
            "Aquiles", "Herrero", "Pan con queso", "Cafe","Casa blanca", "Kung lao", "jo jo", "Jose Martinez"]
palabras_incorrectas = []
palabras_correctas = []

#FUNCION PARA ELEGIR LA PALABRA
def elegir_palabra (lista_palabras):
    palabra_elegida = choice(lista_palabras).lower()
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in palabras_correctas:
            lista_oculta.append(l)
        elif l == " ":
            lista_oculta.append(" ")
            palabras_correctas.append(" ")
        else:
            lista_oculta.append("_ ")
    return lista_oculta


vidas = 6
intentos = 0
palabra_secreta_fija = (elegir_palabra(palabras)[0])



#crear ventana
ventana = Tk()
ventana.title("Ahorcado")
ventana.iconbitmap("C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Juegos\\Ahorcado\\horca.ico")

#panel principal
panel_principal = Frame(ventana, bg="#76A2EF")
panel_principal.pack(side=TOP)


#panel para titulo
panel_titulo = Frame(panel_principal, bg="gray", borderwidth=5, relief="ridge")
panel_titulo.pack(side=TOP, padx=10, pady=10)

#etiqueta titulo
etiqueta_titulo = Label(panel_titulo, text=f"Juego del ahorcado", bg="white", font=("arial", 40))
etiqueta_titulo.grid(row=0, column=0)

#panel para mostrar
panel_mostrar = Frame(panel_principal)
panel_mostrar.pack(side=LEFT, padx=10, pady=10)

#ETIQUETA vidas
etiqueta_vidas = Label(panel_mostrar, text=f"Vidas: {vidas}", font=("arial", 14))
etiqueta_vidas.grid(row=0, column=0, sticky="w")

#Etiqueta para mostrar imagenes
etiqueta_imagen = Label(panel_mostrar)
etiqueta_imagen.grid(row=1, column=0)

#panel para la palabra
panel_letra = Frame(panel_principal)
panel_letra.pack(side=BOTTOM, padx=10, pady=10)

#mostrar lineas y palabras de la letra
oculto = nuevo_tablero(palabra_secreta_fija)
etiqueta_letra = Label(panel_letra, text="".join(oculto), font=("arial", 25))
etiqueta_letra.grid(row=0, column=0)


#PANEL PARA INFORMACION
panel_informacion = Frame(panel_principal)
panel_informacion.pack(side=RIGHT, padx=10, pady=10)

#ETIQUETA CON LAS PALABRAS EQUIVOCADAS
palabras_no_acertadas = Label(panel_informacion, text=f"Palabras no acertadas", font=("arial", 12))
palabras_no_acertadas.grid(row=0, column=0)

#panel para motras las palabras no acertadas
panel_no_acertadas = Frame(panel_informacion)
panel_no_acertadas.grid(row=1, column=0)
etiqueta_no_acertadas = Label(panel_no_acertadas, font=("arial", 14), background="#C9C9CA", width=25, height=5)
etiqueta_no_acertadas.grid(row=0, column=0)

#MENSAJES DE ADVERTENCIA
etiqueta_advertencia = Label(panel_informacion, font=("arial", 12), width=35)
etiqueta_advertencia.grid(row=2, column=0)

#FUNCION PARA PRESIONAR EL BOTON

n = 0
def presionar_boton():
    global contenido
    global palabras_incorrectas
    global palabras_correctas
    global vidas
    global n
    global intentos
    global imagen_presentar
    global imagen_abierta
    global oculto

    
    
    contenido = campo_enviar.get().lower()
    etiqueta_advertencia.config(text="")

    if contenido not in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z" or contenido == "":
        etiqueta_advertencia.config(text="Debes elegir solo 1 la letra")
        

    elif contenido in palabras_correctas:
        etiqueta_advertencia.config(text="ESTA PALABRA YA LA ACERtASTE ELIGE OTRA")
        
    elif contenido in palabra_secreta_fija:
        palabras_correctas.append(contenido)
        etiqueta_letra.config(text="".join(nuevo_tablero(palabra_secreta_fija)))
        intentos +=1


    elif contenido not in palabras_incorrectas:
        
        palabras_incorrectas.append(contenido)
        etiqueta_no_acertadas.config(text=', '.join(palabras_incorrectas))
        vidas -= 1
        etiqueta_vidas.config(text=f"Vidas: {vidas}")
        intentos += 1
        n += 1

        imagen_abierta = Image.open(f"C:\\Users\\Deyvid\\OneDrive\\Documents\\Programas\\Juegos\\Ahorcado\\Ahorcado_{n}.png")  
        imagen_presentar = ImageTk.PhotoImage(imagen_abierta)
        etiqueta_imagen.config(image=imagen_presentar)
        
    else:
        etiqueta_advertencia.config(text="ESA LETRA YA FUE ELEGIDA")

    campo_enviar.delete(0, "end")
    campo_enviar.focus()

    if set(palabras_correctas) == set(palabra_secreta_fija):
        panel_informacion.pack_forget()
        panel_mostrar.pack_forget()
        etiqueta_letra.config(text=f"!!!!!ENHORABUENA!!!!!\nLograste adivinar la palabra secreta.\nPalabra secreta: {palabra_secreta_fija}\nVidas restantes: {vidas}\nIntentos: {intentos}\nPalabras incorrectas: {', '.join(palabras_incorrectas)}",
                              bg="#C9C9CA")
    
    elif vidas == 0:
        panel_informacion.pack_forget()
        panel_mostrar.pack_forget()
        etiqueta_letra.config(text=f"!!!!!AHORCADO!!!!!\nNo lograste adivinar la palabra secreta.\nPalabra secreta: {palabra_secreta_fija}\nVidas restantes: {vidas}\nIntentos: {intentos}\nPalabras incorrectas: {', '.join(palabras_incorrectas)}",
                                bg="#C9C9CA")
    
#INGRESAR LAS PALABRAS
def borrar(event):
    campo_enviar.delete(0, "end")


panel_enviar = Frame(panel_informacion)
panel_enviar.grid(row=3, column=0)

campo_var = StringVar()

campo_enviar = Entry(panel_enviar, textvariable=campo_var)
campo_enviar.grid(row=0, column=0)
campo_enviar.insert(0, "Adivina la palabra")
campo_enviar.bind("<FocusIn>", borrar)


boton_enviar = Button(panel_enviar, text=f"Enviar", command=presionar_boton)
boton_enviar.grid(row=0, column=1)




#LOOP DE LA VENTANA
ventana.mainloop()

