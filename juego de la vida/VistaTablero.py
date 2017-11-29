'''
Created on 2 de nov. de 2017

@author: SergioPla
'''

from tkinter import *
#import tkinter

master = Tk()
master.title("Juego de la vida By SergioPla")
class VistaTablero(object):
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
            for x in range(filas):
                for y in range(columnas):
                        self.casillas[x][y] = Checkbutton(master, text="")
                        self.casillas[x][y].grid(row=x,column=y)
            b = Button(master, text="OKkkkkkkk")
            b.grid(row=x+1,column=0, columnspan = 5)
            b2 = Button(master, text="Hola a todos esto es una prueba")
            b2.grid(row=x+2,column=0, columnspan = 5)


    def __init__(self, filas, columnas):
        '''
        Constructor
        '''
        self.casillas =  [[0 for x in range(filas)] for y in range(columnas)] 
        self.crearTablero(columnas,filas)
        #Seleccionar una casilla
        self.casillas[1][1].select()
        
        mainloop()
   
