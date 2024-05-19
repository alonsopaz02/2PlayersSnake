class Tablero:
    def __init__(self):
        T = [[0] * 8 for _ in range(8)]
        for j in range(1, 8):
            T[0][j] = str(j)
        for i in range(1, 8):
            T[i][0] = str(i)
        self.casillas = T
        
    def get_estado_casilla(self,a,b):
        return self.casillas[a][b]
        pass
    
    def get_casillas(self):
        return self.casillas
        pass
    
    def set_estado_casilla(self,a,b,valor):
        self.casillas[a][b] = valor
        
    def __str__(self):
        # Crear una representación en forma de cadena del tablero
        board_str = ""
        for fila in self.casillas:
            row_str = " ".join(str(valor) for valor in fila)  # Convertir cada elemento en la fila a cadena
            board_str += row_str + "\n"  # Agregar la fila al tablero, seguida de un salto de línea
        
        return board_str