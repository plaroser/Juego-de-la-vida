import Tablero
from tkinter import *
master = Tk() 
if __name__ == '__main__':
    t = Tablero.Tablero(50,20)
   
    #mainloop()
    '''
    t.activar(1,1)
    t.activar(2,1)
    t.activar(3,1)
    
    t.evolucion()
    '''
    print(str(t))
