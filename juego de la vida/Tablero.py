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
        """Activar

        activa una casilla espacifica

        Args:
            self: Instancia actual
            fila: Fila seleccionada
            columna: Columna seleccionada 
        """
        self.tablero[fila][columna] = Tablero.ACTIVA
    
    def desactivar(self,fila,columna):
        """Desactivar

        desactivar una casilla espacifica

        Args:
            self: Instancia actual
            fila: Fila seleccionada
            columna: Columna seleccionada 
        """
        self.tablero[fila][columna] = Tablero.INACTIVA
        
        
        
        
    def posicionValida(self,x,y):
        """Calcula si una posicion es valida

        Comprueba que una casilla es existente

        Args:
            self: Instancia actual
            x: Fila seleccionada
            y: Columna seleccionada 

        Returns: si la posicion es valida
        """
        return ((x>=0) and (x<self.filas))and ((y>=0) and (y<self.columnas))
        
        
    def calcularNumeroVecinosVivos(self,fila,columna):
        """Calcular el numero de vecinos vivos

        activa una casilla espacifica

        Args:
            self: Instancia actual
            fila: Fila seleccionada
            columna: Columna seleccionada

        Returns: Calculo del total de vecinos vivos
        """
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
        """Devuelve el valor de una casilla


        Args:
            self: Instancia actual
            fila: Fila seleccionada
            columna: Columna seleccionada

        Returns: Valor de la casilla seleccionada
        """
        return self.tablero[fila][columna]     
     
    def calcularProximoEstado(self,fila,columna):
        """Calcula el proximo estado de una casilla


        Args:
            self: Instancia actual
            fila: Fila seleccionada
            columna: Columna seleccionada

        Returns: Calcula el siguiente estado de una casilla
        """
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
        """Calcular el siguiente estado

        Calcula el siguiente estado del tablero

        Args:
            self: Instancia actual
            fila: Fila seleccionada
            columna: Columna seleccionada

        """
        copia = [[self.tablero[x][y] for x in range(self.filas)] for y in range(self.columnas)]
        
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                self.tablero[i][j] = self.calcularProximoEstado(i,j)
                 
        
    def __str__(self):
        """Crea un string del tablero


        Args:
            self: Instancia actual

        Returns: Calculo del tablero en String
        """
        res = ""
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                res = res + " " + str(self.getValue(i,j))
            res = res + "\n"    
        return res
    
