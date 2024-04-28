import os
import pygame
import sys

def imprimirTablero(matriz):
    disclaimer("TABLERO")
    linea("#",15)
    linea("#",15)
    filas = 8
    columnas = 8
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end=" ")
        print()
    linea("#",15)
    linea("#",15)

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

def limpiar_terminal():
    """
    Función para limpiar la terminal según el sistema operativo.
    """
    # Detectar el sistema operativo
    if os.name == 'posix':  # Linux, Unix o macOS
        os.system('clear')  # Comando para limpiar la terminal en sistemas basados en Unix
    elif os.name == 'nt':  # Windows
        os.system('cls')  # Comando para limpiar la terminal en Windows
    else:
        # Manejar otros sistemas operativos
        print("No se pudo limpiar la terminal en este sistema operativo.")

# Inicializar Pygame
pygame.init()

# Crear la ventana
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Snake vs Snake')

disclaimer("Snake vs Snake")

filas = 8
columnas = 8
T = [[0] * columnas for _ in range(filas)]

# Llenar la primera fila con los índices de las columnas (del 1 al 7)
for j in range(1, columnas):
    T[0][j] = str(j)

# Llenar la primera columna con los índices de las filas (del 1 al 7)
for i in range(1, filas):
    T[i][0] = str(i)

t = "-"

# (Aa, Ab)
Aa = 999
Ab = 999

# (Ra, Rb)
Ra = 999
Rb = 999

fin = False

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

opcion = 0

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

    for x, y in puntos_vecinos:
        # Verificar si el elemento en las coordenadas (x, y) es diferente de cero
        if T[x][y] == 0:
            return False  # Si encontramos un cero, retornar False
    return True  # Si todos los elementos son diferentes de cero, retornar True

while True:
    opcion = input("Por favor, ingresa quien inicia el juego:\n1. Rojo\n2. Azul\n")
    if opcion == "1":
        t = "R"
        break
    elif opcion == "2":
        t = "A"
        break
    else:
        print("Ingresa una opción válida (1 o 2)")

disclaimer(f"El juego será iniciado por el equipo {t}")

def establecerPrimeraFichaRoja():
    global Aa, Ab, Ra, Rb, T, t
    disclaimer("Elige la primera posicion de tu ficha")
    while(True):
        a = int(input("Ingrese la posicion en el eje x: "))
        b = int(input("Ingrese la posicion en el eje y: "))
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

def establecerPrimeraFichaAzul():
    global Aa, Ab, Ra, Rb, T, t
    disclaimer("Elige la primera posicion de tu ficha")
    while(True):
        a = int(input("Ingrese la posicion en el eje x: "))
        b = int(input("Ingrese la posicion en el eje y: "))
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

def establecerRojo():
    global Aa, Ab, Ra, Rb, T, t
    disclaimer("Elige la posicion de tu ficha")
    while(True):
        a = int(input("Ingrese la posicion en el eje x: "))
        b = int(input("Ingrese la posicion en el eje y: "))
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

def establecerAzul():
    global Aa, Ab, Ra, Rb, T, t
    disclaimer("Elige la posicion de tu ficha")
    while(True):
        a = int(input("Ingrese la posicion en el eje x: "))
        b = int(input("Ingrese la posicion en el eje y: "))
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

if(t == "R"):
    limpiar_terminal()
    turno(f"Turno de {t}")
    establecerPrimeraFichaRoja()
    limpiar_terminal()
    imprimirTablero(T)
    turno(f"Turno de {t}")
    establecerPrimeraFichaAzul()
    limpiar_terminal()
    imprimirTablero(T)
else:
    limpiar_terminal()
    turno(f"Turno de {t}")
    establecerPrimeraFichaAzul()
    limpiar_terminal()
    imprimirTablero(T)
    turno(f"Turno de {t}")
    establecerPrimeraFichaRoja()
    limpiar_terminal()
    imprimirTablero(T)

while(True):
    if(t == "R"):
        if(verificarEstadoMeta(Ra,Rb)):
            disclaimer("GANA AZUL")
            break
        else:
            turno(f"Turno de {t}")
            establecerRojo()
            limpiar_terminal()
            imprimirTablero(T)
    else:
        if(verificarEstadoMeta(Aa,Ab)):
            disclaimer("GANA ROJO")
            break
        else:
            turno(f"Turno de {t}")
            establecerAzul()
            limpiar_terminal()
            imprimirTablero(T)