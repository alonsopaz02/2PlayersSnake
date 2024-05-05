import pygame
import sys
import time

def disclaimer(titulo):
    largo = len(titulo)
    print(f"{'=' * (largo + 4)}")
    print(f"| {titulo} |")
    print(f"{'=' * (largo + 4)}")

def turno(titulo):
    largo = len(titulo)
    borde = '+' + '-' * (largo + 2) + '+'
    contenido = f"| {titulo} |"
    print(borde)
    print(contenido)
    print(borde)

def linea(caracter, longitud):
    """Imprime una línea separadora compuesta por el caracter especificado."""
    print(caracter * longitud)

def indicacion(titulo):
    largo = len(titulo)
    margen = 10
    linea = '*' * (largo + margen * 2)
    espacio = ' ' * margen
    print(linea)
    print(f"{espacio}{titulo}{espacio}")
    print(linea)

def display_mensaje(a):
    font = pygame.font.Font(None, 64)
    text_surface = font.render(a, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text_surface, text_rect)

def draw_matrix():
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

#############Inicializar Tablero#################
filas = 8
columnas = 8
T = [[0] * columnas for _ in range(filas)]
for j in range(1, columnas):
    T[0][j] = str(j)
for i in range(1, filas):
    T[i][0] = str(i)
#################################################


#######Inicializar variables de estado###########
t = "R"
Aa = 999
Ab = 999
Ra = 999
Rb = 999
#################################################


############### REGLAS ##########################
def ColocarPrimR(a,b):
    if(t == "R" and 1<=a<=7 and 1<=b<=7 and T[a][b]==0 and Ra==999 and Rb==999):
        return True
    else:
        return False

def ColocarPrimA(a,b):
    if(t == "A" and 1<=a<=7 and 1<=b<=7 and T[a][b]==0 and Aa==999 and Ab==999):
        return True
    else:
        return False
    
def ColocarRojo(a,b):
    if(t == "R" and 1<=a<=7 and 1<=b<=7 and T[a][b]==0):
        if(a==Ra):
            if(Rb+1==8 and (b==1)):
                return True
            elif(Rb-1==0 and (b==7)):
                return True
            else:
                if(b==Rb+1 or b==Rb-1):
                    return True
                else:
                    return False
        elif(b==Rb):
            if(Ra+1==8 and (a==1)):
                return True
            elif(Ra-1==0 and (a==7)):
                return True
            else:
                if(a==Ra+1 or a==Ra-1):
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
         
def ColocarAzul(a,b):
    if(t == "A" and 1<=a<=7 and 1<=b<=7 and T[a][b]==0):
        if(a==Aa):
            if(Ab+1==8 and (b==1)):
                return True
            elif(Ab-1==0 and (b==7)):
                return True
            else:
                if(b==Ab+1 or b==Ab-1):
                    return True
                else:
                    return False
        elif(b==Ab):
            if(Aa+1==8 and (a==1)):
                return True
            elif(Aa-1==0 and (a==7)):
                return True
            else:
                if(a==Aa+1 or a==Aa-1):
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
#################################################


############ VERIFICAR ESTADO META ##############
def verificarEstadoMeta(a,b):
    # Inicializar el arreglo para almacenar los puntos vecinos
    vecinos = []

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

    for x, y in vecinos:
        # Verificar si el elemento en las coordenadas (x, y) es diferente de cero
        if T[x][y] == 0:
            return False  # Si encontramos un cero, retornar False
    return True  # Si todos los elementos son diferentes de cero, retornar True
#################################################


############# NUEVOS ESTADOS ####################
def establecerPrimeraFichaRoja(a,b):
    global Aa, Ab, Ra, Rb, T, t
    while(True):
        if(ColocarPrimR(a,b)):
            t="A"
            T[a][b]="R"
            Aa = Aa
            Ab = Ab
            Ra = a
            Rb = b
            break
        else:
            print("Ingrese una coordenada vacia o valida")
            return False
    return True

def establecerPrimeraFichaAzul(a,b):
    global Aa, Ab, Ra, Rb, T, t
    while(True):
        if(ColocarPrimA(a,b)):
            t="R"
            T[a][b]="A"
            Aa = a
            Ab = b
            Ra = Ra
            Rb = Rb
            break
        else:
            print("Ingrese una coordenada vacia o valida")
            return False
    return True

def establecerRojo(a,b):
    global Aa, Ab, Ra, Rb, T, t
    while(True):
        if(ColocarRojo(a,b)):
            t="A"
            T[a][b]="R"
            T[Ra][Rb]="r"
            Aa = Aa
            Ab = Ab
            Ra = a
            Rb = b
            break
        else:
            print("Ingrese una coordenada vacia o valida")
            return False
    return True

def establecerAzul(a,b):
    global Aa, Ab, Ra, Rb, T, t
    while(True):
        if(ColocarAzul(a,b)):
            t="R"
            T[a][b]="A"
            T[Aa][Ab]="a"
            Aa = a
            Ab = b
            Ra = Ra
            Rb = Rb
            break
        else:
            print("Ingrese una coordenada vacia o valida")
            return False
    return True
#################################################

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake vs Snake')

# Función principal
def main():
    running = True
    movimientos = 0
    ganador = "0"

    while running:
        for event in pygame.event.get():
            if(movimientos>1):
                if(verificarEstadoMeta(Ra,Rb)):
                    ganador = "Azul"
                    break
                if(verificarEstadoMeta(Aa,Ab)):
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

                if(movimientos<=1):
                    if(t == "R"):
                        if(establecerPrimeraFichaRoja(a,b)==False):
                            break
                        else:
                            movimientos = movimientos + 1
                    elif(t == "A"):
                        if(establecerPrimeraFichaAzul(a,b)==False):
                            break
                        else:
                            movimientos = movimientos + 1
                else:
                    if(t == "R"):
                        if(establecerRojo(a,b)==False):
                            break
                    else:
                        if(establecerAzul(a,b)==False):
                            break
        window.fill(BLACK)
        draw_matrix()
        display_mensaje("Turno de " + t)
        pygame.display.flip()

        if(ganador != "0"):
            display_mensaje("Gana "+ ganador)
            pygame.display.flip()
            time.sleep(10)
            break

if __name__ == '__main__':
    main()