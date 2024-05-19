import random
from game.juego import Juego
import copy

class IAFacil:
    def __init__(self,dificultad,jugador):
        self.dificultad = dificultad
        self.color = jugador
    
    ########################################
    ########### funciones utiles ###########
    ########################################
    
    # Encontrar casilleros vacios vecinos
    def encontrar_vacios(self,cabezaX,cabezaY,T):
        vecinos = []
        vecinos_vacios = []
        a = cabezaX
        b = cabezaY
        puntos_vecinos = [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]
        for punto in puntos_vecinos:
            x, y = punto  # Coordenadas del punto vecino
            # Verificar si el valor es 8 o 0 y aplicar cambio
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
        return vecinos_vacios
    
    
    # Contar cuandos movimientos legales existen
    def contar_mov_posibles(self, cabeza, casillas):
        x, y = cabeza
        return len(self.encontrar_vacios(x, y, casillas))
    
    # decidir movimiento
    def decidir_movimiento(self,juego:Juego):
        if(self.dificultad == "Principiante"):
            mejor_juego = self.no_deterministico_aleatorio(juego)
            return mejor_juego
        elif(self.dificultad == "Normal"):
            mejor_juego = self.primero_el_mejor2(juego)
            return mejor_juego
        elif(self.dificultad == "Experto"):
            mejor_juego = self.informado_minimax(juego)
            return mejor_juego
        else:
            print("No se pudo decidir movimiento")
    
    
    
    ########################################
    ######### funcion evaluadora ###########
    ########################################
    
    ########################################
    ####### f(e) = Ma(e) - Mr(e) ###########
    ########################################
    
    
    def evaluar_estado(self, juego: Juego):
        movimientos_ia = self.contar_mov_posibles(
            (juego.estado.get_x_cabezaAzul(), juego.estado.get_y_cabezaAzul()),
            juego.estado.tablero.get_casillas()
        )
        movimientos_oponente = self.contar_mov_posibles(
            (juego.estado.get_x_cabezaRoja(), juego.estado.get_y_cabezaRoja()),
            juego.estado.tablero.get_casillas()
        )
        return movimientos_ia - movimientos_oponente
    
    ########################################
    ########## IA MODO FACIL ###############
    ########################################
    
    def no_deterministico_aleatorio(self, juego: Juego):
        movimientos_legales = self.encontrar_vacios(
            juego.estado.get_x_cabezaAzul(),
            juego.estado.get_y_cabezaAzul(),
            juego.estado.tablero.get_casillas()
        )
        
        movimiento_aleatorio = random.choice(movimientos_legales)
        juego_copia = copy.deepcopy(juego)
        juego_copia.establecerAzul(movimiento_aleatorio[0], movimiento_aleatorio[1])
        
        a = juego_copia.estado.get_x_cabezaAzul()
        b = juego_copia.estado.get_y_cabezaAzul()
        
        return a,b
        
    ########################################
    ########## IA MODO INTERMEDIO ##########
    ########################################
    
    ########## Primero el mejor ##########
    ################ BFS #################
        
    def primero_el_mejor2(self, juego: Juego):
        vecinos_vacios = self.encontrar_vacios(
            juego.estado.get_x_cabezaAzul(),
            juego.estado.get_y_cabezaAzul(),
            juego.estado.tablero.get_casillas()
        )
        mejor_juego = None
        mejor_valor = float('-inf')
        
        for vecino in vecinos_vacios:
            juego_copia = copy.deepcopy(juego)
            juego_copia.establecerAzul(vecino[0], vecino[1])
            valor = self.evaluar_estado(juego_copia)
            
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_juego = juego_copia
        
        a = mejor_juego.estado.get_x_cabezaAzul()
        b = mejor_juego.estado.get_y_cabezaAzul()
        return a,b
    
    ########################################
    ########## IA MODO DIFICIL #############
    ########################################
    
    def minimax(self, juego: Juego, profundidad, maximizando):
        if profundidad == 0 or juego.verificarEstadoMeta(juego.estado.get_x_cabezaAzul(), juego.estado.get_y_cabezaAzul()) or juego.verificarEstadoMeta(juego.estado.get_x_cabezaRoja(), juego.estado.get_y_cabezaRoja()):
            return self.evaluar_estado(juego), None

        vecinos_vacios = self.encontrar_vacios(
            juego.estado.get_x_cabezaAzul() if maximizando else juego.estado.get_x_cabezaRoja(),
            juego.estado.get_y_cabezaAzul() if maximizando else juego.estado.get_y_cabezaRoja(),
            juego.estado.tablero.get_casillas()
        )

        mejor_movimiento = None

        if maximizando:
            max_eval = float('-inf')
            for vecino in vecinos_vacios:
                juego_copia = copy.deepcopy(juego)
                juego_copia.establecerAzul(vecino[0], vecino[1])
                evaluacion, _ = self.minimax(juego_copia, profundidad - 1, False)
                if evaluacion > max_eval:
                    max_eval = evaluacion
                    mejor_movimiento = (vecino[0], vecino[1])
            return max_eval, mejor_movimiento
        else:
            min_eval = float('inf')
            for vecino in vecinos_vacios:
                juego_copia = copy.deepcopy(juego)
                juego_copia.establecerRojo(vecino[0], vecino[1])
                evaluacion, _ = self.minimax(juego_copia, profundidad - 1, True)
                if evaluacion < min_eval:
                    min_eval = evaluacion
                    mejor_movimiento = (vecino[0], vecino[1])
            return min_eval, mejor_movimiento

    def informado_minimax(self, juego: Juego, profundidad=5):
        _, mejor_movimiento = self.minimax(juego, profundidad, True)
        return mejor_movimiento