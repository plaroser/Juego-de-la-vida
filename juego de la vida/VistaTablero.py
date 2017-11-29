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
                        self.tablero[x][y] = Checkbutton(master, text="")
                        self.tablero[x][y].grid(row=x,column=y)
            b = Button(master, text="OKkkkkkkk")
            b.grid(row=x+1,column=0, columnspan = 5)
            b2 = Button(master, text="Hola a todos esto es una prueba")
            b2.grid(row=x+2,column=0, columnspan = 5)

    '''def imprimirTablero(self, matriz):
        for x in range(filas):
            for y in range(columnas):
                self.tablero[x][y]=matriz[x][y]'''
   
    def __init__(self, filas, columnas):
        '''
        Constructor
        '''
        self.crearTablero(columnas,filas)
        #Seleccionar una casilla
        self.tablero[1][1].select()
        
        mainloop()
   
