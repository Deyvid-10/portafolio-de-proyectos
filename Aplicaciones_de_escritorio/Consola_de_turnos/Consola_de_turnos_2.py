from Consola_de_turnos_1 import *
from tkinter import *

def menu():
    #colores
    blanco = "#EFEBE0"
    verde = "#BCECE0"

    #crar ventana
    ventana = Tk()
    ventana.title("Consoola de turnos")
    ventana.config(bg=verde)

    
    #turno
    panel_turno = Frame(ventana, bg=verde)
    
    etiqueta_turno = Label(panel_turno, font=("arial", 14), bg=blanco)
    etiqueta_turno.pack()
   
    etiqueta_espacio = Label(panel_turno, font=("arial", 12), bg=verde)
    etiqueta_espacio.pack()

    etiqueta_re = Label(panel_turno, text="Deseas tomar otro turno?", font=("arial", 12), bg=verde)
    etiqueta_re.pack()

    def ok():
        panel_turno.pack_forget()
        panel_botones.pack()

    boton_re = Button(panel_turno, text="OK", command=ok)
    boton_re.pack()


    #asignacion atributos
    per = decoreador_turnos(eleccion_perfumeria(), etiqueta_turno)
    cos = decoreador_turnos(eleccion_cosmetica(), etiqueta_turno)
    far = decoreador_turnos(eleccion_farmacia(), etiqueta_turno)
    
    
    #funsiones para los botones
    def cambiar_pantalla():
        panel_turno.pack(fill="both")
        panel_botones.pack_forget()
        

    def perfumeria():
        per()
        cambiar_pantalla()

    def cosmetica():
        cos()
        cambiar_pantalla()

    def farmacia():
        far()
        cambiar_pantalla()

  
    #botones
    panel_botones = Frame(ventana, bg=verde)
    panel_botones.pack()

    etiqueta_eleccion = Label(panel_botones, text="Por favor eliga su turno", font=("arial", 12), bg=verde)
    etiqueta_eleccion.grid(row=0, column=0)

    boton_per = Button(panel_botones, text="Perfumeria", width=22, height=2, font=("arial", 10), command=perfumeria)
    boton_per.grid(row=1, column=0, padx=5)

    boton_cos = Button(panel_botones, text="Cosmetica", width=22, height=2, font=("arial", 10), command=cosmetica)
    boton_cos.grid(row=2, column=0, padx=5)

    boton_far = Button(panel_botones, text="Farmacia", width=22, height=2, font=("arial", 10), command=farmacia)
    boton_far.grid(row=3, column=0, padx=5)

    

    #loop de ventana
    ventana.mainloop()


menu()