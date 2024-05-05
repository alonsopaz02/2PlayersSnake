import random
from cabeza import Cabeza

class IAJugador:
    def __init__(self,dificultad,cabezaX,cabezaY):
        self.dificultad = dificultad
        self.color = "A"
        self.cabezaX = cabezaX
        self.cabezaY = cabezaY
        
        
    def set_cabezaX(self,x):
        self.cabezaX = x
        
    def set_cabezaY(self,y):
        self.cabezaY = y
        
    def get_cabezaX(self):
        return self.cabezaX
        
    def get_cabezaY(self):
        return self.cabezaY
    
    
    def elegir_posicion_facil(self,cabezaX,cabezaY):
        vecinos = []
        a = cabezaX
        b = cabezaY
        puntos_vecinos = [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]

        # Procesar cada punto vecino
        for punto in puntos_vecinos:
            x, y = punto  # Coordenadas del punto vecino

            # Verificar si el valor es 8 o 0 y aplicar las modificaciones
            if x == 8:
                x = 1
            elif x == 0:
                x = 7

            if y == 8:
                y = 1
            elif y == 0:
                y = 7

            # Agregar el punto modificado al arreglo de vecinos
            vecinos.append((x, y))
            
        numero_random = random.randint(0, 3)
        return vecinos[numero_random]