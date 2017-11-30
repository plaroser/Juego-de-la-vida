'''
Created on 21 de nov. de 2017

@author: SergioPla
'''
import VistaTablero
import Tablero
from tkinter import *

class ControladorTablero():
    counter=0
    t = 0
    v=0

    def __init__(self, filas, columnas):
        self.tablero = Tablero.Tablero(filas, columnas);
        self.vista = VistaTablero.VistaTablero(filas, columnas,self.tablero);
        #==========Boton provisional==========
        bIniciar = Button(master=self.vista.getMaster(), text="Continuar",command=self.siguienteEstado)
        bIniciar.grid(row=filas+5,column=0, columnspan = 2)
        #mainloop()

    def counter_label(label):
        counter = 0
        def count():
            global counter
            counter += 1
            label.config(text=str(counter))
            label.after(1000, count)
        count()

    def leerTablero(self):
        #print(str(self.vista.columnas))
        #print(str(False))
        salida = ""
        for x in range(self.vista.filas):
            salida=salida+"\n"
            #print(str(self.vista.columnas))
            for y in range(self.vista.columnas):
                    self.tablero.tablero[x][y]=self.vista.tablero[x][y].get()
                    #print("blabla")
                    salida=salida+" "+str(self.tablero.getValue(x,y))
        #print(salida)
        #self.tablero.evolucion()
        print(self.tablero)

    def asignarTableroAVista(self):
        for x in range(self.vista.filas):
            for y in range(self.vista.columnas):
                self.vista.tablero[x][y].set(self.tablero.tablero[x][y])

    def siguienteEstado(self):
         self.leerTablero()
         self.tablero.evolucion()
         self.asignarTableroAVista()
         self.vista.imprimirTablero(self.tablero.tablero)
         #print("++++")