### Solo imprime tablero con los numeros

def imprimirTablero(matriz):
    filas = 8
    columnas = 8
    for i in range(filas):
        for j in range(columnas):
            # Imprimir el elemento de la matriz
            print(matriz[i][j], end=" ")  # Usar end=" " para evitar un salto de línea
        print()  # Salto de línea después de imprimir cada fila



print("Iniciando jueguito")

#T = [[0 for _ in range(7)] for _ in range(7)]\
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
    if(t == "R" and 1<=a<=7 and 1<=b<=7 and T[a][b]==0 and Ra-1<=a%7<=Ra+1 and Rb-1<=b%7<=Rb+1):
        return True
    else:
        return False
    
def ColocarAzul(a,b):
    if(t == "A" and 1<=a<=7 and 1<=b<=7 and T[a][b]==0 and Aa-1<=a%7<=Aa+1 and Ab-1<=b%7<=Ab+1):
        return True
    else:
        return False

opcion = 0

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

print(f"El juego será iniciado por el equipo {t}")

def establecerPrimeraFichaRoja():
    global Aa, Ab, Ra, Rb, T, t
    print("Elige la primera posicion de tu ficha \n")
    a = int(input("Ingrese la posicion en el eje x: "))
    b = int(input("Ingrese la posicion en el eje y: "))
    while(True):
        if(ColocarPrimR(a,b)):
            t="A"
            T[a][b]=1
            Aa = Aa
            Ab = Ab
            Ra = a
            Rb = b
            break
        else:
            input("Ingrese una coordenada vacia o valida")

def establecerPrimeraFichaAzul():
    global Aa, Ab, Ra, Rb, T, t
    print("Elige la primera posicion de tu ficha \n")
    a = int(input("Ingrese la posicion en el eje x: "))
    b = int(input("Ingrese la posicion en el eje y: "))
    while(True):
        if(ColocarPrimA(a,b)):
            t="R"
            T[a][b]=2
            Aa = a
            Ab = b
            Ra = Ra
            Rb = Rb
            break
        else:
            input("Ingrese una coordenada vacia o valida")

def establecerRojo():
    global Aa, Ab, Ra, Rb, T, t
    print("Elige donde colocar tu ficha \n")
    a = int(input("Ingrese la posicion en el eje x: "))
    b = int(input("Ingrese la posicion en el eje y: "))
    while(True):
        if(ColocarRojo(a,b)):
            t="A"
            T[a][b]=1
            Aa = Aa
            Ab = Ab
            Ra = a
            Rb = b
            break
        else:
            input("Ingrese una coordenada vacia o valida")

def establecerAzul():
    global Aa, Ab, Ra, Rb, T, t
    print("Elige la primera posicion de tu ficha \n")
    a = int(input("Ingrese la posicion en el eje x: "))
    b = int(input("Ingrese la posicion en el eje y: "))
    while(True):
        if(ColocarAzul(a,b)):
            t="R"
            T[a][b]=2
            Aa = a
            Ab = b
            Ra = Ra
            Rb = Rb
            break
        else:
            input("Ingrese una coordenada vacia o valida")

if(t == "R"):
    establecerPrimeraFichaRoja()
    imprimirTablero(T)
    establecerPrimeraFichaAzul()
    imprimirTablero(T)
else:
    establecerPrimeraFichaAzul()
    imprimirTablero(T)
    establecerPrimeraFichaRoja()
    imprimirTablero(T)

while(True):
    if(t == "R"):
        establecerRojo()
        imprimirTablero(T)
    else:
        establecerAzul()
        imprimirTablero(T)










