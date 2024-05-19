import pygame

class Interfaz:
    def __init__(self, width, height, rows, cols):
        # Inicializar Pygame
        pygame.init()
        
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.square_size = self.width // self.cols

        # Definir colores
        self.BLACK = (0, 0, 0)
        self.DARK_RED = (139, 0, 0)
        self.RED = (255, 0, 0)
        self.DARK_BLUE = (0, 0, 139)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.GREY = (128, 128, 128)
        self.LIGHT_BLUE = (173, 216, 230)  # Color de fondo claro
        self.LIGHTER_BLUE = (135, 206, 250)  # Color de fondo claro alternativo
        self.BORDER_COLOR = (255, 105, 180)  # Color del borde del tablero

        # Crear la ventana
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake vs Snake')
        
        self.message_font = pygame.font.SysFont("comicsansms", 28)  # Define la fuente para el mensaje

    def draw_matrix(self, T):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = (col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                
                # Alternar colores de las casillas
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.window, self.LIGHT_BLUE, rect)
                else:
                    pygame.draw.rect(self.window, self.LIGHTER_BLUE, rect)

                pygame.draw.rect(self.window, self.BORDER_COLOR, rect, 3)  # Borde de las casillas

                value = T[row][col]

                if row == 0 or col == 0:  # Si es la primera fila o la primera columna
                    if row == 0 and col == 0:
                        continue  # No dibujar nada en la esquina superior izquierda
                    else:
                        # Dibujar número
                        font = pygame.font.SysFont("comicsansms", 28)  # Puedes ajustar el tamaño de la fuente
                        text_surface = font.render(str(row + col), True, self.BLACK)
                        text_rect = text_surface.get_rect(center=(col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2))
                        self.window.blit(text_surface, text_rect)
                else:
                    if value == 'R':
                        # Dibujar círculo rojo oscuro
                        pygame.draw.circle(self.window, self.RED, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                    elif value == 'r':
                        # Dibujar círculo rojo
                        pygame.draw.circle(self.window, self.DARK_RED, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                    elif value == 'A':
                        # Dibujar círculo azul oscuro
                        pygame.draw.circle(self.window, self.BLUE, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                    elif value == 'a':
                        # Dibujar círculo azul
                        pygame.draw.circle(self.window, self.DARK_BLUE, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)

    def draw_message(self, turno):
        # Crear la superficie del texto
        if(turno=="R"):
            text_surface = self.message_font.render("Turno de Rojo", True, self.RED)
            text_rect = text_surface.get_rect(center=(self.width // 2, 30))
            # Crear el rectángulo de fondo negro
            padding = 10  # Espacio alrededor del texto
            background_rect = pygame.Rect(
                text_rect.left - padding,
                text_rect.top - padding,
                text_rect.width + 2 * padding,
                text_rect.height + 2 * padding
            )
        
            # Dibujar el rectángulo de fondo negro
            pygame.draw.rect(self.window, self.WHITE, background_rect, border_radius=20)
            # Dibujar el borde blanco alrededor del rectángulo
            pygame.draw.rect(self.window, self.BLACK, background_rect, 3, border_radius=20)
        
            # Dibujar el texto sobre el rectángulo
            self.window.blit(text_surface, text_rect)
        elif(turno=="A"):
            text_surface = self.message_font.render("Turno de Azul", True, self.BLUE)
            text_rect = text_surface.get_rect(center=(self.width // 2, 30))
            # Crear el rectángulo de fondo negro
            padding = 10  # Espacio alrededor del texto
            background_rect = pygame.Rect(
                text_rect.left - padding,
                text_rect.top - padding,
                text_rect.width + 2 * padding,
                text_rect.height + 2 * padding
            )
        
             # Dibujar el rectángulo de fondo negro
            pygame.draw.rect(self.window, self.WHITE, background_rect, border_radius=20)
            # Dibujar el borde blanco alrededor del rectángulo
            pygame.draw.rect(self.window, self.BLACK, background_rect, 3, border_radius=20)
        
            # Dibujar el texto sobre el rectángulo
            self.window.blit(text_surface, text_rect)
            
    def draw_winner(self,ganador):
        if(ganador=="R"):
            message="Ganador ROJO (Human)"
            color = self.RED
        else:
            message="Ganador AZUL (IA)"
            color = self.BLUE
        text_surface = self.message_font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(self.width // 2, 30))
        # Crear el rectángulo de fondo negro
        padding = 10  # Espacio alrededor del texto
        background_rect = pygame.Rect(
            text_rect.left - padding,
            text_rect.top - padding,
            text_rect.width + 2 * padding,
            text_rect.height + 2 * padding
        )
        
        # Dibujar el rectángulo de fondo negro
        pygame.draw.rect(self.window, self.WHITE, background_rect, border_radius=20)
        # Dibujar el borde blanco alrededor del rectángulo
        pygame.draw.rect(self.window, self.BLACK, background_rect, 3, border_radius=20)
        # Dibujar el texto sobre el rectángulo
        self.window.blit(text_surface, text_rect)
        
    def draw_button(self, rect, text, font, color, border_radius):
        pygame.draw.rect(self.window, color, rect, border_radius=border_radius)
        pygame.draw.rect(self.window, self.WHITE, rect, 5, border_radius=border_radius)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.window.blit(text_surface, text_rect)

    def draw_menu(self):
        self.window.fill(self.BLACK)

        # Título del menú
        title_font = pygame.font.SysFont("comicsansms", 72)
        title = title_font.render("Snake VS Snake", True, self.WHITE)
        title_rect = title.get_rect(center=(self.width // 2, self.height // 4))
        self.window.blit(title, title_rect)

        # Botones del menú
        button_font = pygame.font.SysFont("comicsansms", 36)
        button_width = 500
        button_height = 80
        button_y_offset = 150

        easy_button = pygame.Rect(self.width // 2 - button_width // 2, self.height // 4 + button_y_offset, button_width, button_height)
        intermediate_button = pygame.Rect(self.width // 2 - button_width // 2, self.height // 4 + button_y_offset + 100, button_width, button_height)
        hard_button = pygame.Rect(self.width // 2 - button_width // 2, self.height // 4 + button_y_offset + 200, button_width, button_height)

        self.draw_button(easy_button, "Principiante", button_font, self.BORDER_COLOR, border_radius=20)
        self.draw_button(intermediate_button, "Normal", button_font, self.BORDER_COLOR, border_radius=20)
        self.draw_button(hard_button, "Experto", button_font, self.BORDER_COLOR, border_radius=20)
        pygame.display.update()

    def draw_player_selection_menu(self):
        self.window.fill(self.BLACK)

        # Título del menú
        title_font = pygame.font.SysFont("comicsansms", 72)
        title = title_font.render("¿Quien inicia?", True, self.WHITE)
        title_rect = title.get_rect(center=(self.width // 2, self.height // 4))
        self.window.blit(title, title_rect)

        # Botones del menú
        button_font = pygame.font.SysFont("comicsansms", 36)
        button_width = 500
        button_height = 80
        button_y_offset = 150

        human_button = pygame.Rect(self.width // 2 - button_width // 2, self.height // 4 + button_y_offset, button_width, button_height)
        ia_button = pygame.Rect(self.width // 2 - button_width // 2, self.height // 4 + button_y_offset + 100, button_width, button_height)

        self.draw_button(human_button, "Humano (Rojo)", button_font, self.RED, border_radius=20)
        self.draw_button(ia_button, "IA (Azul)", button_font, self.BLUE, border_radius=20)
        pygame.display.update()

    def update_display(self):
        pygame.display.flip()