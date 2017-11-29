'''
Created on 21 de nov. de 2017

@author: SergioPla
'''
import VistaTablero
import Tablero

class ControladorTablero(object):
    counter=0
    def counter_label(label):
        counter = 0
        def count():
            global counter
            counter += 1
            label.config(text=str(counter))
            label.after(1000, count)
        count()

    @staticmethod
    def crearTablero(filas,columnas):
        Tablero.Tablero(filas,columnas)
        VistaTablero.VistaTablero(filas,columnas)
        

    @staticmethod
    def leerTablero():
         for x in range(VistaTablero.VistaTablero.filas):
                for y in range(VistaTablero.VistaTablero.columnas):
                        Tablero.Tablero.tablero[x][y]=((VistaTablero.VistaTablero.casillas[x][y].value))
                        print(Tablero.Tablero.tablero[x][y].get())
