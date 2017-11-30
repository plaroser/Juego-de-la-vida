'''
Created on 21 de nov. de 2017

@author: SergioPla
'''
import VistaTablero
import Tablero
from tkinter import *
import time
time.sleep(5) 

class ControladorTablero():
    t = 0
    v=0

    def __init__(self, filas, columnas):
        self.tablero = Tablero.Tablero(filas, columnas);
        self.vista = VistaTablero.VistaTablero(filas, columnas,self.tablero);
        #==========Boton provisional==========
        bIniciar = Button(master=self.vista.getMaster(), text="Continuar",command=self.siguienteEstado)
        bIniciar.grid(row=filas+6,column=0, columnspan = 2)
        self.lbGeneraciones = Label(master=self.vista.getMaster(),text="Generaciones = 0")
        self.lbGeneraciones.grid(row=filas+5,column=0, columnspan = 4)
        self.counter=0
        #mainloop()
        #self.bucle()

    def bucle(self):
        while True:
            self.siguienteEstado()
            time.sleep(1) 
    
    

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