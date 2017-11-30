'''
Created on 21 de nov. de 2017

@author: SergioPla
'''


class Tablero(object):
    '''
    classdocs
    '''
    ACTIVA = True
    INACTIVA = False
    NVECINOS_VOLVER_ACTIVA = 3
    MIN_CONTINUA_VIVA = 2
    MAX_CONTINUA_VIVA = 3
    tablero =  [[0 for x in range(100)] for y in range(100)]

    def __init__(self, filas, columnas):
        '''
        Constructor
        '''
        self.filas = filas
        self.columnas = columnas   
        self.tablero =  [[False for x in range(filas)] for y in range(columnas)] 
        
    def activar(self,fila,columna):
        self.tablero[fila][columna] = Tablero.ACTIVA
    
    def desactivar(self,fila,columna):
        self.tablero[fila][columna] = Tablero.INACTIVA
        
        
        
        
    def posicionValida(self,x,y):
        return ((x>=0) and (x<self.filas))and ((y>=0) and (y<self.columnas))
        
        
    def calcularNumeroVecinosVivos(self,fila,columna):
        contador = 0;
        for i in range(-1, 2):
            x = fila + i
            for j in range(-1, 2):
                y = columna + j
    
                if (self.posicionValida(x,y)):
                    if (self.tablero[x][y] == Tablero.ACTIVA and (i!=0 or j!=0)):
                        contador = contador + 1

        return contador
    
    def getValue(self, fila, columna): 
        return self.tablero[fila][columna]     
     
    def calcularProximoEstado(self,fila,columna):
        vecinosVivos = self.calcularNumeroVecinosVivos(fila, columna)
        res = False
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
                #print(str(self.calcularProximoEstado(i,j)))
        
        self.tablero = copia;   

    def evolucion2(self):
        print(self.columnas);
        
    def __str__(self):
        res = ""
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                res = res + " " + str(self.getValue(i,j))
            
            res = res + "\n"    

        return res
    
