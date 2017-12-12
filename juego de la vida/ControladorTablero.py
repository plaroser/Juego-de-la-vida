'''
Created on 21 de nov. de 2017

@author: SergioPla
'''
import VistaTablero
import Tablero
from tkinter import *
import threading
import time

class ControladorTablero():
    t = 0
    v=0


    def __init__(self, filas, columnas):
        """Constructor

        Crea un tablero con el número de filas y columnas indicado

        Args:
            self: Instancia actual
            filas: Filas totales a crear
            columnas: Columnas totales a 
        """
        self.tablero = Tablero.Tablero(filas, columnas);
        self.vista = VistaTablero.VistaTablero(filas, columnas,self.tablero);
        self.bIniciar = Button(master=self.vista.getMaster(), text="Continuar",command=self.iniciar)
        self.bIniciar.grid(row=filas+6,column=0, columnspan = 4)
        self.bParar = Button(master=self.vista.getMaster(), text="Parar", command=self.parar,state=DISABLED)
        self.bParar.grid(row=filas+7,column=0, columnspan = 4)
        self.lbGeneraciones = Label(master=self.vista.getMaster(),text="Generaciones = 0")
        self.lbGeneraciones.grid(row=filas+5,column=0, columnspan = 5)
        self.counter=0
        self.continuar = False
        self.t = threading.Thread(target=self.vivir)

    def iniciar(self):
        """Inicia el juego

        Inicia el ciclo del juego

        Args:
            self: Instancia actual
            
        """
        if not self.t.isAlive():
            self.t.start()
        self.bIniciar.config(state=DISABLED)
        self.bParar.config(state="normal")
        self.continuar=True
        self.vista.modoVista()

    def vivir(self):
        """Ciclo de vida

        Se va ejecutando segun lo que se ha calculado

        Args:
            self: Instancia actual
           
        """
        while True:
            if self.continuar:
                self.siguienteEstado()
                time.sleep(1)

    def parar(self):
        """Para el ciclo

        Para el ciclo de vida del juego

        Args:
            self: Instancia actual

        """
        self.continuar=False
        self.bIniciar.config(state="normal")
        self.bParar.config(state=DISABLED)
        self.vista.modoEdicion()

       

    def leerTablero(self):
        """Lee el tablero

        Lee el estado actual del la vista del tablerop y lo plasma en el modelo del tablero
        Args:
            self: Instancia acual.

        """
        #salida = ""
        for x in range(self.vista.filas):
            #salida=salida+"\n"
            for y in range(self.vista.columnas):
                    self.tablero.tablero[x][y]=self.vista.tablero[x][y].get()
                    #salida=salida+" "+str(self.tablero.getValue(x,y))
        #print(self.tablero)

    def imprimirTablero(self):
        """Imprime el tablero

        Lee el estado actual del la vista del tablero y lo plasma en el modelo del tablero
        Args:
            self: Instancia acual.

        """
        for x in range(self.vista.filas):
            for y in range(self.vista.columnas):
                self.vista.tablero[x][y].set(self.tablero.tablero[x][y])

    def siguienteEstado(self):
        """Calcula el siguiente estado del tablero

        Ejecuta todos los metodos necesarios para calcular el siguiente estado del tablero

        Args:
            self: Instancia acual.

        """
        self.leerTablero()
        self.tablero.evolucion()
        self.imprimirTablero()
        self.vista.imprimirTablero(self.tablero.tablero)
        self.counter=self.counter+1
        self.lbGeneraciones.config(text="Generaciones = "+str(self.counter))
