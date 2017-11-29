'''
Created on 2 de nov. de 2017

@author: SergioPla
'''

from tkinter import *
#import tkinter

master = Tk()
master.title("Juego de la vida By SergioPla")
import Tablero
class VistaTablero(object):


    filas = 0
    columnas=0
    '''
        def counter_label(label):
            counter = 0
            def count():
                global counter
                counter += 1
                label.config(text=str(counter))
                label.after(1000, count)
            count()
    '''
    
    def crearTablero(self,filas,columnas):
        self.filas=filas
        self.casillas =  [[0 for x in range(filas)] for y in range(columnas)] 
        Tablero.Tablero.tablero =  [[False for x in range(filas)] for y in range(columnas)] 
        for x in range(filas):
            for y in range(columnas):
                Tablero.Tablero.tablero[x][y]=BooleanVar()
                self.casillas[x][y] = Checkbutton(master, text="", variable=Tablero.Tablero.tablero[x][y])
                #print(str(Tablero.Tablero.tablero[x][y].get()))
                self.casillas[x][y].grid(row=x,column=y)
        self.bParar = Button(master, text="Parar")
        self.bParar.grid(row=x+1,column=0, columnspan = 4)
        self.bIniciar = Button(master, text="Iniciar")
        self.bIniciar.grid(row=x+2,column=0, columnspan = 4)
        l = Label(master,text="Ciclos de vida:")
        l.grid(row=x+3,column=0, columnspan = 4)
        self.l2= Label(master,text="Ejemplo de ciclos")
        self.l2.grid(row=x+3,column=4, columnspan = 4)
        lMilisegundos = Label(master,text="Milisegundos:")
        lMilisegundos.grid(row=x+4,column=0, columnspan = 4)
        self.tbMilisegundos = Entry(master, text="1000")
        self.tbMilisegundos.grid(row=x+4,column=4, columnspan = 4)


    def __init__(self, filas, columnas):
        '''
        Constructor
        '''


        self.crearTablero(columnas,filas)
        #Seleccionar una casilla
        self.casillas[0][0].select()
        
        mainloop()
   
