import pygame

class Interfaz:
    def __init__(self, width, height, rows, cols):
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

        # Inicializar Pygame
        pygame.init()

        # Crear la ventana
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake vs Snake')

    def draw_matrix(self, T):
        for row in range(self.rows):
            for col in range(self.cols):
                value = T[row][col]

                if isinstance(value, int):
                    # Dibujar número
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(value), True, self.WHITE)
                    text_rect = text_surface.get_rect(center=(col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2))
                    self.window.blit(text_surface, text_rect)
                elif value == 'R':
                    # Dibujar círculo rojo oscuro
                    pygame.draw.circle(self.window, self.DARK_RED, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                elif value == 'r':
                    # Dibujar círculo rojo
                    pygame.draw.circle(self.window, self.RED, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                elif value == 'A':
                    # Dibujar círculo azul oscuro
                    pygame.draw.circle(self.window, self.DARK_BLUE, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                elif value == 'a':
                    # Dibujar círculo azul
                    pygame.draw.circle(self.window, self.BLUE, (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2), self.square_size // 3)
                elif value.isdigit():
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(value, True, self.WHITE)
                    text_rect = text_surface.get_rect(center=(col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2))
                    self.window.blit(text_surface, text_rect)

    def update_display(self):
        pygame.display.flip()