import pygame
import sys
import time
import random

from gui.interfaz import Interfaz
from easyIA import IAFacil
from game.juego import Juego

from pygame.locals import QUIT, MOUSEBUTTONDOWN

def main():
    interfaz = Interfaz(800, 800, 8, 8)
    difficulty = None
    starter = None
    
    while difficulty is None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if interfaz.width // 2 - 250 <= x <= interfaz.width // 2 + 250:
                    if interfaz.height // 4 + 150 <= y <= interfaz.height // 4 + 230:
                        difficulty = "Principiante"
                        print(difficulty)
                    elif interfaz.height // 4 + 250 <= y <= interfaz.height // 4 + 330:
                        difficulty = "Normal"
                        print(difficulty)
                    elif interfaz.height // 4 + 350 <= y <= interfaz.height // 4 + 430:
                        difficulty = "Experto"
                        print(difficulty)
        interfaz.draw_menu()
        
    while starter is None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if interfaz.width // 2 - 250 <= x <= interfaz.width // 2 + 250:
                    if interfaz.height // 4 + 150 <= y <= interfaz.height // 4 + 230:
                        starter = "R"
                    elif interfaz.height // 4 + 250 <= y <= interfaz.height // 4 + 330:
                        starter = "A"
        interfaz.draw_player_selection_menu()

    
    juego = Juego(starter)
    ia = IAFacil(difficulty,"A")

    running = True
    ganador = "0"

    while running:
        for event in pygame.event.get():
            if(juego.movimientos > 1):
                if(juego.verificarEstadoMeta(juego.estado.get_x_cabezaRoja(), juego.estado.get_y_cabezaRoja())):
                    ganador = "A"
                    running = False
                    break
                if(juego.verificarEstadoMeta(juego.estado.get_x_cabezaAzul(), juego.estado.get_y_cabezaAzul())):
                    ganador = "R"
                    running = False
                    break

            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                a = y // interfaz.square_size
                b = x // interfaz.square_size

                if(juego.movimientos <= 1):
                    if(juego.estado.get_turno() == "R"):
                        if(juego.establecerPrimeraFichaRoja(a, b) == False):
                            break
                        else:
                            juego.movimientos += 1
                    elif(juego.estado.get_turno() == "A"):
                        a = random.randint(1, 7)
                        b = random.randint(1, 7)
                        if(juego.establecerPrimeraFichaAzul(a, b) == False):
                            break
                        else:
                            juego.movimientos += 1
                else:
                    if(juego.estado.get_turno() == "R"):
                        if(juego.establecerRojo(a, b) == False):
                            break
                    else:
                        mejor_juego = ia.decidir_movimiento(juego)
                        a, b = mejor_juego
                        if(juego.establecerAzul(a, b) == False):
                            break

        interfaz.window.fill(interfaz.BLACK)
        interfaz.draw_matrix(juego.estado.get_tablero().get_casillas())
        interfaz.draw_message(juego.estado.get_turno())
        interfaz.update_display()

        if(ganador != "0"):
            interfaz.draw_winner(ganador)
            interfaz.update_display()
            running=False
        
    time.sleep(7)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()