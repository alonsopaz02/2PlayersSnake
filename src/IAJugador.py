import random
from cabeza import Cabeza

class IAJugador:
    def __init__(self,dificultad,cabezaX,cabezaY):
        self.dificultad = dificultad
        self.color = "A"
    
    
    def elegir_posicion_facil(self,cabezaX,cabezaY,T):
        vecinos = []
        vecinos_vacios = []
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
        
        for punto in vecinos:
            if(T[punto[0]][punto[1]]==0):
                vecinos_vacios.append((punto[0],punto[1]))
        
        punto_aleatorio = random.choice(vecinos_vacios)
        return punto_aleatorio
    
    def decidir_posicion_facil(self,cabezaX,cabezaY,T):
        punto = []
        while(True):
            punto = self.elegir_posicion_facil(cabezaX,cabezaY)
            if(T[punto[0]][punto[1]]==0):
                return punto
    
