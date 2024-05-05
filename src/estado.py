from tablero import Tablero
from cabeza import Cabeza

class Estado: 
    def __init__(self,turno):
        self.tablero = Tablero()
        self.turno = turno
        self.cabezaRoja = Cabeza()
        self.cabezaAzul = Cabeza()
        
    def get_tablero(self):
        return self.tablero
    
    def get_turno(self):
        return self.turno
    
    def get_x_cabezaRoja(self):
        return self.cabezaRoja.get_x_cabeza()
    
    def get_y_cabezaRoja(self):
        return self.cabezaRoja.get_y_cabeza()
    
    def get_x_cabezaAzul(self):
        return self.cabezaAzul.get_x_cabeza()
    
    def get_y_cabezaAzul(self):
        return self.cabezaAzul.get_y_cabeza()
    
    def set_tablero(self,T):
        self.tablero = T
    
    def set_turno(self,t):
        self.turno = t
    
    def set_x_cabezaRoja(self,x):
        self.cabezaRoja.set_x_cabza(x)
    
    def set_y_cabezaRoja(self,y):
        self.cabezaRoja.set_y_cabza(y)
    
    def set_x_cabezaAzul(self,x):
        self.cabezaAzul.set_x_cabza(x)
    
    def set_y_cabezaAzul(self,y):
        self.cabezaAzul.set_y_cabza(y)
    
    def set_estado(self, tablero,turno, cabezaRoja, cabezaAzul):
        self.tablero=tablero
        self.turno=turno
        self.cabezaRoja=cabezaRoja
        self.cabezaAzul=cabezaAzul
        
    def print_estado(self): # Muestra el estado actual del juego
        print('Tablero:', self.tablero.__str__())
        print('Turno:', self.turno)
        print('X de CabezaRoja: ',self.cabezaRoja.get_x_cabeza)
        print('Y de CabezaRoja:', self.cabezaRoja.get_y_cabeza)
        print('X de CabezaAzul: ',self.cabezaAzul.get_x_cabeza)
        print('Y de CabezaAzul:', self.cabezaAzul.get_y_cabeza)
        print('-------------------')