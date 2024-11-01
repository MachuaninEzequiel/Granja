import pygame

class Renderer:
    TILE_SIZE = 30  # Tamaño de cada tile (carácter) en píxeles
    VIEWPORT_WIDTH = 50  # Número de tiles visibles en el ancho de la pantalla

    def __init__(self, map_file):
        self.map_data = self.load_map(map_file)
        self.map_width = len(self.map_data[0])
        self.map_height = len(self.map_data)
        self.width = self.VIEWPORT_WIDTH * self.TILE_SIZE
        self.height = self.map_height * self.TILE_SIZE

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Juego de la Granja")

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            return [list(line.strip()) for line in file.readlines()]

    def render(self, player_position):
        self.screen.fill((0, 0, 0))  # Color de fondo negro
        # Calcular el offset para scroll lateral
        offset_x = max(0, player_position[0] - self.VIEWPORT_WIDTH // 2)
        
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row[offset_x:offset_x + self.VIEWPORT_WIDTH]):
                screen_x = x * self.TILE_SIZE
                screen_y = y * self.TILE_SIZE
                
                if tile == '*':  # Edificio
                    color = (150, 75, 0)  # Marrón
                elif tile == '%':  # Lechuga
                    color = (0, 255, 0)  # Verde
                elif tile == '$':  # Tomate
                    color = (255, 0, 0)  # Rojo
                else:
                    continue
                pygame.draw.rect(self.screen, color, (screen_x, screen_y, self.TILE_SIZE, self.TILE_SIZE))

        # Renderizar el personaje en varias líneas
        self.draw_player(player_position, offset_x)
        pygame.display.flip()

    def draw_player(self, player_position, offset_x):
        player_x = (player_position[0] - offset_x) * self.TILE_SIZE
        player_y = player_position[1] * self.TILE_SIZE
        player_color = (255, 255, 0)  # Amarillo

        # Dibujo del personaje en tres líneas
        pygame.draw.line(self.screen, player_color, (player_x + 16, player_y), (player_x + 16, player_y + 8), 2)  # Cabeza (O)
        pygame.draw.line(self.screen, player_color, (player_x + 16, player_y + 8), (player_x + 12, player_y + 16), 2)  # Brazo izquierdo
        pygame.draw.line(self.screen, player_color, (player_x + 16, player_y + 8), (player_x + 20, player_y + 16), 2)  # Brazo derecho
        pygame.draw.line(self.screen, player_color, (player_x + 16, player_y + 8), (player_x + 16, player_y + 20), 2)  # Cuerpo
        pygame.draw.line(self.screen, player_color, (player_x + 16, player_y + 20), (player_x + 12, player_y + 28), 2)  # Pierna izquierda
        pygame.draw.line(self.screen, player_color, (player_x + 16, player_y + 20), (player_x + 20, player_y + 28), 2)  # Pierna derecha

    def is_walkable(self, x, y):
        """Comprueba si el tile en (x, y) es transitable."""
        if 0 <= x < self.map_width and 0 <= y < self.map_height:
            return self.map_data[y][x] != '*'
        return False
