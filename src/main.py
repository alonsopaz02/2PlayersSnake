from juego import Juego
from IAJugador import IAJugador
import pygame
import sys
import time


def draw_matrix(T):
    for row in range(ROWS):
        for col in range(COLS):
            value = T[row][col]

            if isinstance(value, int):
                # Dibujar número
                font = pygame.font.Font(None, 36)
                text_surface = font.render(str(value), True, WHITE)
                text_rect = text_surface.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                window.blit(text_surface, text_rect)
            elif value == 'R':
                # Dibujar círculo rojo oscuro
                pygame.draw.circle(window, DARK_RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
            elif value == 'r':
                # Dibujar círculo rojo
                pygame.draw.circle(window, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
            elif value == 'A':
                # Dibujar círculo azul oscuro
                pygame.draw.circle(window, DARK_BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
            elif value == 'a':
                # Dibujar círculo azul
                pygame.draw.circle(window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
            elif value.isdigit():
                font = pygame.font.Font(None, 36)
                text_surface = font.render(value, True, WHITE)
                text_rect = text_surface.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                window.blit(text_surface, text_rect)

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana y del tablero
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

# Definir colores
BLACK = (0, 0, 0)
DARK_RED = (139, 0, 0)
RED = (255, 0, 0)
DARK_BLUE = (0, 0, 139)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake vs Snake')

# Función principal
def main():
    juego = Juego("R")
    ia = IAJugador("facil",[999,999])
    
    running = True

    ganador = "0"

    while running:
        for event in pygame.event.get():
            if(juego.movimientos>1):
                if(juego.verificarEstadoMeta(juego.estado.get_x_cabezaRoja(),juego.estado.get_y_cabezaRoja())):
                    ganador = "Azul"
                    break
                if(juego.verificarEstadoMeta(juego.estado.get_x_cabezaAzul(),juego.estado.get_y_cabezaAzul())):
                    ganador = "Rojo"
                    break

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                a = y // SQUARE_SIZE
                b = x // SQUARE_SIZE

                if(juego.movimientos<=1):
                    if(juego.estado.get_turno() == "R"):
                        if(juego.establecerPrimeraFichaRoja(a,b)==False):
                            break
                        else:
                            juego.movimientos = juego.movimientos + 1
                    elif(juego.estado.get_turno()== "A"):
                        
                        if(juego.establecerPrimeraFichaAzul(a,b)==False):
                            break
                        else:
                            juego.movimientos = juego.movimientos + 1
                else:
                    if(juego.estado.get_turno()== "R"):
                        if(juego.establecerRojo(a,b)==False):
                            break
                    else:
                        if(juego.establecerAzul(a,b)==False):
                            break
        window.fill(BLACK)
        draw_matrix(juego.estado.get_tablero().get_casillas())
        print("Turno de " + juego.estado.get_turno())
        pygame.display.flip()

        if(ganador != "0"):
            print("Gana "+ ganador)
            pygame.display.flip()
            time.sleep(10)
            break

if __name__ == '__main__':
    main()