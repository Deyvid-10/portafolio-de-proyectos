from tkinter import *

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre

        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)

        self.numero_cuenta = numero_cuenta

        self.balance = balance

    def __str__(self):
        return "\n" + "*" * 5 + " CUENTA BANCARIA " + "*" * 5 + "\n" + f"Cliente: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}\n"

    def depositar(self, deposito):

        self.balance += deposito

    def retirar(self, retiro):

        self.balance -= retiro


def crear_cliente():

    #funcion para boton
    def guardar():
        global info_cuenta
        nom = campo_cliente_nom.get()
        ap = campo_cliente_ap.get()
        cuen = campo_cliente_cuen.get()
        bal = 0

        

        info_cuenta = Cliente(nom, ap, cuen, bal)
        menu(info_cuenta)

        panel_pedir_datos.pack_forget()
        panel_menu.pack(pady=5, padx=5)

        

    #creacion de las etiquetas
    lista_cliente = ["Nombres:", "Apellidos:", "Numero de cuenta:"]
    cont = 0

    for c in lista_cliente:
        etiqueta_cliente = Label(panel_pedir_datos, font=("arial", 12), text=c, background="#88B2CC")
        etiqueta_cliente.grid(row=cont, column=0, sticky="e")
        cont +=1

    
    #campos para datos

    nombre = StringVar()
    campo_cliente_nom = Entry(panel_pedir_datos, textvariable=nombre)
    campo_cliente_nom.focus()
    campo_cliente_nom.grid(row=0, column=1)

    apellido = StringVar()
    campo_cliente_ap = Entry(panel_pedir_datos, textvariable=apellido)
    campo_cliente_ap.grid(row=1, column=1, padx=5)

    cuenta = IntVar()
    campo_cliente_cuen = Entry(panel_pedir_datos, textvariable=cuenta)
    campo_cliente_cuen.delete(0, "end")
    campo_cliente_cuen.grid(row=2, column=1, padx=5)
        
    boton_cliente = Button(panel_pedir_datos, text="Guardar", command=guardar)
    boton_cliente.grid(row=3, column=1, padx=5)

    info_cuenta = ""

    return info_cuenta

def menu(info):



    #funsiones para botones
    def ingresar():
        contenido = dinero.get()
        dinero.delete(0, "end")
        dinero.focus()
        if contenido == "":
            etiqueta_info.config(text="** El campor esta vacio **") 
        else:    
            info.depositar(int(contenido))
            etiqueta_info.config(text="** Su deposito fue completado **")

        etiqueta_consulta.config(text=info)
    
    def sacar():
        contenido = dinero.get()
        dinero.delete(0, "end")
        dinero.focus()
        if contenido == "":
            etiqueta_info.config(text="** El campor esta vacio **") 
        elif info.balance < int(contenido):
            etiqueta_info.config(text="** Monto es menor al balance **") 
        else:    
            info.retirar(int(contenido))
            etiqueta_info.config(text="** Su retiro fue completado **")

        etiqueta_consulta.config(text=info)

    def apagar():
        ventana.destroy()

    #consulta
    panel_consulta = Frame(panel_menu, bg="#88B2CC")
    panel_consulta.pack(side=TOP, fill="both")

    etiqueta_consulta = Label(panel_consulta, font=("arial", 12), text=info, bg="#88B2CC")
    etiqueta_consulta.grid(column=0, row=0, sticky="nw")

    #mensaje informativo
    panel_info = Frame(panel_menu, bg="#88B2CC")
    panel_info.pack(side=TOP, fill="both")

    etiqueta_info = Label(panel_info, font=("arial", 12, ), bg="#88B2CC", fg="red")
    etiqueta_info.grid(row=0, column=0)

    #ingresar valores
    panel_valores = Frame(panel_menu, bg="#88B2CC")
    panel_valores.pack(side=TOP)

    efectivo = IntVar()
    dinero = Entry(panel_valores, textvariable=efectivo, width=25)
    dinero.delete(0, "end")
    dinero.focus()
    dinero.grid(row=0, column=0, pady=5, padx=5)

    #botones
    panel_botones = Frame(panel_menu, bg="#88B2CC")
    panel_botones.pack(side=TOP)

    depositar = Button(panel_botones, command=ingresar, text="Depositar")
    depositar.grid(row=1, column=0)

    retirar = Button(panel_botones, command=sacar, text="Retirar")
    retirar.grid(row=1, column=1, padx=5)

    salir = Button(panel_botones, command=apagar, text="Salir")
    salir.grid(row=1, column=2)


#crear ventana
ventana = Tk()
ventana.title("Cuenta bancaria")
ventana.config(background="#88B2CC")

#panel para pedir los datos
panel_pedir_datos = Frame(ventana, bg="#88B2CC")
panel_pedir_datos.pack(pady=5, padx=5)

cuenta_bancaria = crear_cliente()

#panel para el menu
panel_menu = Frame(ventana, bg="#88B2CC")



#loop de ventana
ventana.mainloop()
