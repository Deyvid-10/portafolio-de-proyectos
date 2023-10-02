from tkinter import * 

def decoreador_turnos(funcion, eti):
    def texto_adicional():
        
        eti.config(text="Su turno es:"+"\n" + next(funcion) + "\nAguarde y sera atendido")

    return texto_adicional

def eleccion_perfumeria():

    for p in range(1, 10000):
        perfumeria = f"P-{p}"
        yield perfumeria

def eleccion_farmacia():
    for f in range(1, 10000):
        farmacia = f"F-{f}"
        yield farmacia

def eleccion_cosmetica():
    for c in range(1, 10000):
        cosmetica = f"C-{c}"
        yield cosmetica

print("f")