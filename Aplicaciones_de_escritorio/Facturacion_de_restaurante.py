from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#iniciar txinter
aplicacion = Tk()

#tamano ventana
aplicacion.geometry("1145x630+0+0")

#evitar maximizar
aplicacion.resizable(0,0)

#titulo ventana
aplicacion.title("Gestor de restaurante - sistema de facturacion")

#color fondo
aplicacion.config(bg="burlywood")

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief= FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de facturacion", fg="black", font=("Dosis", 58), bg="burlywood", width=22)
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=60)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo,text="Comida", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="black")
panel_comidas.pack(side= LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text="Bebidas", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="black")
panel_bebidas.pack(side= LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo,text="Postres", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="black")
panel_postres.pack(side= LEFT)

#panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadore
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()

#lista de productos
lista_comidas = ["Pescado", "Sushi", "Pizza", "Pollo", "Res", "Cerdo", "Hamburqueza", "Arroz"]
lista_bebidas = ["Refresco1", "Refresco2", "Refresco3", "Jugo", "Jugo2", "Cerveza", "Agua", "Vino"]
lista_postres = ["Helado", "Frutas", "Brownies", "Flan", "Pastel1", "Pastel2", "Pastel3", "Pastel4"]

#revisar checks
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variable_lista_comidas[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        elif variable_lista_comidas[x].get() == 0:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
            cuadros_comida[x].config(textvariable=texto_comida[x])
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variable_lista_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        elif variable_lista_bebidas[x].get() == 0:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
            cuadros_bebida[x].config(textvariable=texto_bebida[x])
        x += 1

    x = 0
    for c in cuadros_postre:
        if variable_lista_postres[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == "0":
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        elif variable_lista_postres[x].get() == 0:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
            cuadros_postre[x].config(textvariable=texto_postre[x])
        x += 1


#checks buttons
variable_lista_comidas = []
cuadros_comida = []
texto_comida = []
cont = 0
for comida in lista_comidas:

    #crear check buttons
    variable_lista_comidas.append('')
    variable_lista_comidas[cont] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=("Dosis", 19, "bold"),
                         onvalue=1, offvalue=0, variable=variable_lista_comidas[cont], command=revisar_check)
    comida.grid(row=cont, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[cont] = StringVar()
    texto_comida[cont].set('0')
    cuadros_comida[cont] = Entry(panel_comidas,font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable=texto_comida[cont])
    cuadros_comida[cont].grid(row=cont, column=1)


    cont += 1

variable_lista_bebidas = []
cuadros_bebida = []
texto_bebida = []
cont = 0
for bebidas in lista_bebidas:

    # crear check buttons
    variable_lista_bebidas.append('')
    variable_lista_bebidas[cont] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=bebidas.title(), font=("Dosis", 19, "bold"),
                          onvalue=1, offvalue=0, variable=variable_lista_bebidas[cont], command=revisar_check)
    bebidas.grid(row=cont, column=0, sticky=W)

    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[cont] = StringVar()
    texto_bebida[cont].set('0')
    cuadros_bebida[cont] = Entry(panel_bebidas, font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable=texto_bebida[cont])
    cuadros_bebida[cont].grid(row=cont, column=1)

    cont += 1

variable_lista_postres = []
cuadros_postre = []
texto_postre = []
cont = 0
for postres in lista_postres:

    # crear check buttons
    variable_lista_postres.append('')
    variable_lista_postres[cont] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=("Dosis", 19, "bold"),
                          onvalue=1, offvalue=0, variable=variable_lista_postres[cont], command=revisar_check)
    postres.grid(row=cont, column=0, sticky=W)

    # crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[cont] = StringVar()
    texto_postre[cont].set('0')
    cuadros_postre[cont] = Entry(panel_postres, font=("Dosis", 18, "bold"), bd=1, width=6, state=DISABLED, textvariable=texto_postre[cont])
    cuadros_postre[cont].grid(row=cont, column=1)

    cont += 1

#variables

var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_sub_total = StringVar()
var_total = StringVar()
var_impuesto = StringVar()

#etiquetass de costos y campos de entrada

#comida
etiqueta_costo_comida = Label(panel_costos, text="Costo Comida", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1)

#bebida
etiqueta_costo_bebida = Label(panel_costos, text="Costo Bebida", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx= 40)

#postre
etiqueta_costo_postre = Label(panel_costos, text="Costo Postre", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx= 40)

#sub-total
etiqueta_sub_total = Label(panel_costos, text="Sub-total", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_sub_total.grid(row=0, column=2, padx= 40)

texto_sub_total = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_sub_total)

texto_sub_total.grid(row=0, column=3, padx= 40)

#impuesto
etiqueta_impuesto = Label(panel_costos, text="Impuestos", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_impuesto)

texto_impuesto.grid(row=1, column=3, padx=40)

#precios de los productos
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]



#funciiones para los botones
def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida += (float(cantidad.get()) * precios_comida[p])
        p += 1
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida += (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre += (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_postre + sub_total_bebida
    impuesto = sub_total * 0.07
    total = sub_total + impuesto

    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postre.set(f"$ {round(sub_total_postre, 2)}")
    var_sub_total.set(f"$ {round(sub_total, 2)}")
    var_impuesto.set(f"$ {round(impuesto, 2)}")
    var_total.set(f"$ {round(total, 2)}")

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 1999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, F"*"*60+"\n")
    texto_recibo.insert(END, "ITEMS\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"-"*72+"\n")

    x=0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n")
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END,f"{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n")
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != "0":
            texto_recibo.insert(END,f"{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n")
        x += 1

    texto_recibo.insert(END, f"-" * 72 + "\n")
    texto_recibo.insert(END, f"Costo de la comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo del postre: \t\t\t{var_costo_postre.get()}\n")
    texto_recibo.insert(END, f"-" * 72 + "\n")
    texto_recibo.insert(END, f"Sub-total: \t\t\t{var_sub_total.get()}\n")
    texto_recibo.insert(END, f"Impuesto: \t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, F"*" * 60 + "\n")
    texto_recibo.insert(END, f"Le espramos pronto")

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension="txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion", "Guarado exitosamente")

def resetear():
    texto_recibo.delete(1.0, END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postre:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variable_lista_comidas:
        v.set(0)
    for v in variable_lista_bebidas:
        v.set(0)
    for v in variable_lista_postres:
        v.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_sub_total.set("")
    var_impuesto.set("")
    var_total.set("")


#total

etiqueta_total = Label(panel_costos, text="Total", font=("Dosis", 12, "bold"), bg="azure4", fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, font=("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_total)

texto_total.grid(row=2, column=3, padx= 40)

#botones
botones = ["total", "recibo", "guardar", "resetear"]
botones_creaddos = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("Dosis", 14, "bold"), fg="white", bg="azure4", bd=1)
    botones_creaddos.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creaddos[0].config(command=total)
botones_creaddos[1].config(command=recibo)
botones_creaddos[2].config(command=guardar)
botones_creaddos[3].config(command=resetear)


#area de recibo
texto_recibo = Text(panel_recibo, font=("Dosis", 12, "bold"), bd=1, width=40, height=10)
texto_recibo.grid(row=0, column=0)

# funcionalidad de la calculadore
operador = ''
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar ():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultaddo():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

#calculadora
visor_calculadora = Entry(panel_calculadora, font=("Dosis", 16, "bold"), bd=1, width=28)
visor_calculadora.grid(row=0, column=0, columnspan=4)


botones_calculadora = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "CE", "Borrar", "0", "/"]
botones_guardados =[]

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=("Dosis", 16, "bold"), fg="white", bg="azure4", bd=1, width=6)
    boton.grid(row=fila, column=columna)


    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

    botones_guardados.append(boton)

botones_guardados[0].config(command=lambda: click_boton("7"))
botones_guardados[1].config(command=lambda: click_boton("8"))
botones_guardados[2].config(command=lambda: click_boton("9"))
botones_guardados[3].config(command=lambda: click_boton("+"))
botones_guardados[4].config(command=lambda: click_boton("4"))
botones_guardados[5].config(command=lambda: click_boton("5"))
botones_guardados[6].config(command=lambda: click_boton("6"))
botones_guardados[7].config(command=lambda: click_boton("-"))
botones_guardados[8].config(command=lambda: click_boton("1"))
botones_guardados[9].config(command=lambda: click_boton("2"))
botones_guardados[10].config(command=lambda: click_boton("3"))
botones_guardados[11].config(command=lambda: click_boton("*"))
botones_guardados[14].config(command=lambda: click_boton("0"))
botones_guardados[15].config(command=lambda: click_boton("/"))

botones_guardados[13].config(command=lambda: borrar())

botones_guardados[12].config(command=lambda: obtener_resultaddo())

#evitar cierre
aplicacion.mainloop()



