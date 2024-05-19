from .estado import Estado

class Juego:
    def __init__(self,turno):
        self.estado = Estado(turno)
        self.movimientos = 0
                   
    def get_movimientos(self):
        return self.movimientos
            
    def increase_movimientos(self):
        self.movimientos = self.movimientos + 1
    
    # REGLAS DEL JUEGO
    def ColocarPrimR(self,a,b):
        if(self.estado.get_turno() == "R" 
           and 1<=a<=7 
           and 1<=b<=7 
           and self.estado.get_tablero().get_estado_casilla(a,b)==0 
           and self.estado.cabezaRoja.get_x_cabeza()==999 
           and self.estado.cabezaRoja.get_y_cabeza()==999):
            return True
        else:
            return False
        
    def ColocarPrimA(self,a,b):
        if(self.estado.get_turno() == "A" 
           and 1<=a<=7 
           and 1<=b<=7 
           and self.estado.get_tablero().get_estado_casilla(a,b)==0 
           and self.estado.cabezaAzul.get_x_cabeza()==999 
           and self.estado.cabezaAzul.get_y_cabeza()==999):
            return True
        else:
            return False
        
    def ColocarRojo(self,a,b):
        if(self.estado.get_turno() == "R"  
            and 1<=a<=7 
            and 1<=b<=7 
            and self.estado.get_tablero().get_estado_casilla(a,b)==0):
            if(a==self.estado.cabezaRoja.get_x_cabeza()):
                if(self.estado.cabezaRoja.get_y_cabeza()+1==8 and (b==1)):
                    return True
                elif(self.estado.cabezaRoja.get_y_cabeza()-1==0 and (b==7)):
                    return True
                else:
                    if(b==self.estado.cabezaRoja.get_y_cabeza()+1 or b==self.estado.cabezaRoja.get_y_cabeza()-1):
                        return True
                    else:
                        return False
            elif(b==self.estado.cabezaRoja.get_y_cabeza()):
                if(self.estado.cabezaRoja.get_x_cabeza()+1==8 and (a==1)):
                    return True
                elif(self.estado.cabezaRoja.get_x_cabeza()-1==0 and (a==7)):
                    return True
                else:
                    if(a==self.estado.cabezaRoja.get_x_cabeza()+1 or a==self.estado.cabezaRoja.get_x_cabeza()-1):
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
        
    def ColocarAzul(self,a,b):
        if(self.estado.get_turno() == "A"  
            and 1<=a<=7 
            and 1<=b<=7 
            and self.estado.get_tablero().get_estado_casilla(a,b)==0):
            if(a==self.estado.cabezaAzul.get_x_cabeza()):
                if(self.estado.cabezaAzul.get_y_cabeza()+1==8 and (b==1)):
                    return True
                elif(self.estado.cabezaAzul.get_y_cabeza()-1==0 and (b==7)):
                    return True
                else:
                    if(b==self.estado.cabezaAzul.get_y_cabeza()+1 or b==self.estado.cabezaAzul.get_y_cabeza()-1):
                        return True
                    else:
                        return False
            elif(b==self.estado.cabezaAzul.get_y_cabeza()):
                if(self.estado.cabezaAzul.get_x_cabeza()+1==8 and (a==1)):
                    return True
                elif(self.estado.cabezaAzul.get_x_cabeza()-1==0 and (a==7)):
                    return True
                else:
                    if(a==self.estado.cabezaAzul.get_x_cabeza()+1 or a==self.estado.cabezaAzul.get_x_cabeza()-1):
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False

############ VERIFICAR ESTADO META ##############
    def verificarEstadoMeta(self,a,b):
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
            if self.estado.get_tablero().get_estado_casilla(x,y) == 0:
                return False  # Si encontramos un cero, retornar False
        return True  # Si todos los elementos son diferentes de cero, retornar True
    
    # Actualizacion de estados
    def establecerPrimeraFichaRoja(self,a,b):
        while(True):
            if(self.ColocarPrimR(a,b)):
                self.estado.set_turno("A")
                self.estado.get_tablero().set_estado_casilla(a,b,"R")
                self.estado.set_x_cabezaRoja(a)
                self.estado.set_y_cabezaRoja(b)
                break
            else:
                print("Ingrese una coordenada vacia o valida")
                return False
        return True
    
    def establecerPrimeraFichaAzul(self,a,b):
        while(True):
            if(self.ColocarPrimA(a,b)):
                self.estado.set_turno("R")
                self.estado.get_tablero().set_estado_casilla(a,b,"A")

                self.estado.set_x_cabezaAzul(a)
                self.estado.set_y_cabezaAzul(b)
                break
            else:
                print("Ingrese una coordenada vacia o valida")
                return False
        return True
    
    def establecerRojo(self,a,b):
        while(True):
            if(self.ColocarRojo(a,b)):
                self.estado.set_turno("A")
                
                self.estado.get_tablero().set_estado_casilla(a,b,"R")
                self.estado.get_tablero().set_estado_casilla(self.estado.get_x_cabezaRoja(),self.estado.get_y_cabezaRoja(),"r")
                
                self.estado.set_x_cabezaRoja(a)
                self.estado.set_y_cabezaRoja(b)
                break
            else:
                print("Ingrese una coordenada vacia o valida")
                return False
        return True
    
    def establecerAzul(self,a,b):
        while(True):
            if(self.ColocarAzul(a,b)):
                self.estado.set_turno("R")
                
                self.estado.get_tablero().set_estado_casilla(a,b,"A")
                self.estado.get_tablero().set_estado_casilla(self.estado.get_x_cabezaAzul(),self.estado.get_y_cabezaAzul(),"a")
                
                self.estado.set_x_cabezaAzul(a)
                self.estado.set_y_cabezaAzul(b)
                break
            else:
                print("Ingrese una coordenada vacia o valida")
                return False
        return True