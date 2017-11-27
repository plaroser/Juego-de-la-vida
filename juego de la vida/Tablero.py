from tkinter import *
#import tkinter

master = Tk()
#frame = Tk.frame(master)
master.title("Prueba")
#frame.pack()


class Tablero(object):
    '''
    classdocs
    '''
    ACTIVA = 1
    INACTIVA = 0
    NVECINOS_VOLVER_ACTIVA = 3
    MIN_CONTINUA_VIVA = 2
    MAX_CONTINUA_VIVA = 3
    
    def counter_label(label):
        counter = 0
        def count():
            global counter
            counter += 1
            label.config(text=str(counter))
            label.after(1000, count)
        count()

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
        self.filas = filas
        self.columnas = columnas   
        self.tablero = [[0 for x in range(filas)] for y in range(columnas)] 
        self.check= [[0 for x in range(filas)] for y in range(columnas)]
        self.crearTablero(columnas,filas)
        #Seleccionar una casilla
        self.tablero[1][1].select()
        
        mainloop()


    def activar(self,fila,columna):
        self.tablero[fila][columna] = Tablero.ACTIVA
    
    def desactivar(self,fila,columna):
        self.tablero[fila][columna] = Tablero.INACTIVA
        

        
        
    def posicionValida(self,x,y):
        return ((x >= 0) and (x < self.filas)) and ((y >= 0) and (y < self.columnas))
        
        
    def calcularNumeroVecinosVivos(self,fila,columna):
        contador = 0
        for i in range(-1, 2):
            x = fila + i
            for j in range(-1, 2):
                y = columna + j
    
                if (self.posicionValida(x,y)):
                    if (self.tablero[x][y] == Tablero.ACTIVA and (i != 0 or j != 0)):
                        contador = contador + 1
                    
                
        
        return contador
    
    def getValue(self, fila, columna): 
        return self.tablero[fila][columna]     
     
    def calcularProximoEstado(self,fila,columna):
        vecinosVivos = self.calcularNumeroVecinosVivos(fila, columna)
        res = 0
        if (self.getValue(fila, columna) == Tablero.INACTIVA):
            if (vecinosVivos == Tablero.NVECINOS_VOLVER_ACTIVA):
                res = Tablero.ACTIVA
            else:
                res = Tablero.INACTIVA
        else:
            if ((vecinosVivos >= Tablero.MIN_CONTINUA_VIVA) and (vecinosVivos <= Tablero.MAX_CONTINUA_VIVA)):
                res = Tablero.ACTIVA
            else:
                res = Tablero.INACTIVA
        
        return res
 
    def evolucion(self):
        copia = [[self.tablero[x][y] for x in range(self.filas)] for y in range(self.columnas)]
        
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                copia[i][j] = self.calcularProximoEstado(i,j)
                print(str(self.calcularProximoEstado(i,j)))
        
        self.tablero = copia  
        
    def __str__(self):
        res = ""
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                res = res + " " + str(self.getValue(i,j))
            
            res = res + "\n"    

        return res


