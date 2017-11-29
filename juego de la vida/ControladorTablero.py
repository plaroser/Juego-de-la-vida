'''
Created on 21 de nov. de 2017

@author: SergioPla
'''
import VistaTablero
import Tablero

class ControladorTablero():
    counter=0
    t = 0
    v=0
    def counter_label(label):
        counter = 0
        def count():
            global counter
            counter += 1
            label.config(text=str(counter))
            label.after(1000, count)
        count()

    def crearTablero(filas,columnas):
        Tablero.Tablero(filas,columnas)
        VistaTablero.VistaTablero(filas,columnas)
        VistaTablero.VistaTablero.filas=filas
        VistaTablero.VistaTablero.columnas=columnas
        

    def leerTablero():
        print(str(VistaTablero.VistaTablero.columnas))
        salida = ""
        for x in range(VistaTablero.VistaTablero.filas):
            salida=salida+"\n"
            for y in range(VistaTablero.VistaTablero.columnas):
                    salida=salida+" "+str(Tablero.Tablero.tablero[x][y].get())
        print(salida)

    def siguienteEstado():
         Tablero.Tablero.evolucion(Tablero.Tablero.tablero)