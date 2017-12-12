'''
Created on 2 de nov. de 2017

@author: SergioPla
'''

from tkinter import *
#import tkinter
import Tablero
import ControladorTablero

master = Tk()
master.title("Juego de la vida By SergioPla")

class VistaTablero(object):

    def leerTablero(self):
        return self.tablero

    def crearTablero(self,filas,columnas):
        self.filas=filas
        self.casillas =  [[0 for x in range(filas)] for y in range(columnas)] 
        self.tablero =  [[False for x in range(filas)] for y in range(columnas)] 
        for x in range(filas):
            for y in range(columnas):
                self.tablero[x][y]=BooleanVar()
                self.casillas[x][y] = Checkbutton(master, text="", variable=self.tablero[x][y])
                #print(str(Tablero.Tablero.tablero[x][y].get()))
                self.casillas[x][y].grid(row=x,column=y)

        lVivos = Label(master,text="Total vivos:")
        lVivos.grid(row=x+4,column=0, columnspan = 4)
        self.lbVivos = Label(master, text="0")
        self.lbVivos.grid(row=x+4,column=4, columnspan = 4)
    
    def imprimirTablero(self,tablero):
        for x in range(self.filas):
            for y in range(self.columnas):
                if tablero[x][y]==True:
                    self.casillas[x][y].select()
                else:
                    self.casillas[x][y].deselect()
                #    print(tablero[x][y])
                #self.casillas[x][y].select()
                self.setVivos()
    
    def modoVista(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                self.casillas[x][y].config(state=DISABLED)

    def modoEdicion(self):
        for x in range(self.filas):
            for y in range(self.columnas):
                self.casillas[x][y].config(state="normal")
    
    def setVivos(self):
        contador = 0
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.tablero[x][y].get()==True:
                    contador=contador+1
        self.lbVivos.config(text=str(contador))

    def __init__(self, filas, columnas, tablero):
        '''
        Constructor
        '''
        self.tablero = tablero
        self.filas=filas
        self.columnas = columnas
        self.crearTablero(columnas,filas)
        #Seleccionar una casilla
        self.casillas[0][0].select()
        #mainloop()

    def getMaster(self):
       return master
 