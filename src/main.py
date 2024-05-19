import pygame
import sys
import time

from gui.interfaz import Interfaz
from easyIA import IAFacil
from game.juego import Juego

def main():
    juego = Juego("R")
    ia = IAFacil("Intermedio")
    interfaz = Interfaz(800, 800, 8, 8)
    
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
                a = y // interfaz.square_size
                b = x // interfaz.square_size

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
                        mejor_juego = ia.decidir_movimiento(juego)
                        a, b = mejor_juego
                        print(a)
                        print(b) 
                        if(juego.establecerAzul(a,b)==False):
                            break
        interfaz.window.fill(interfaz.BLACK)
        interfaz.draw_matrix(juego.estado.get_tablero().get_casillas())
        interfaz.draw_message("Turno de " + juego.estado.get_turno())
        interfaz.update_display()

        if(ganador != "0"):
            print("Gana "+ ganador)
            interfaz.update_display()
            time.sleep(10)
            break

if __name__ == '__main__':
    main()