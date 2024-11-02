import pygame
import os

class Renderer:
    TILE_SIZE = 30  # Tamaño de cada tile en píxeles
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

        # Cargar sprites del personaje
        self.sprites = {
            'parado': pygame.image.load(os.path.join('assets', 'parado.png')),
            'arriba': pygame.image.load(os.path.join('assets', 'arriba.png')),
            'abajo': pygame.image.load(os.path.join('assets', 'abajo.png')),
            'derecha': pygame.image.load(os.path.join('assets', 'derecha.png')),
            'izquierda': pygame.image.load(os.path.join('assets', 'izquierda.png'))
        }

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            return [list(line.strip()) for line in file.readlines()]

    def render(self, player_position, player_direction):
        self.screen.fill((0, 0, 0))  # Fondo negro
        offset_x = max(0, player_position[0] - self.VIEWPORT_WIDTH // 2)

        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row[offset_x:offset_x + self.VIEWPORT_WIDTH]):
                screen_x = x * self.TILE_SIZE
                screen_y = y * self.TILE_SIZE
                
                if tile == '*':  # Edificio
                    color = (150, 75, 0)  
                elif tile == '%':  # Lechuga
                    color = (0, 255, 0)  
                elif tile == '$':  # Tomate
                    color = (255, 0, 0)  
                elif tile == '&':  # Morron amarillo
                    color = (255, 255, 0)  
                else:
                    continue
                pygame.draw.rect(self.screen, color, (screen_x, screen_y, self.TILE_SIZE, self.TILE_SIZE))

        # Dibujar el personaje usando el sprite correcto
        self.draw_player(player_position, offset_x, player_direction)
        pygame.display.flip()

    def draw_player(self, player_position, offset_x, direction):
        # La posición del jugador ya está en píxeles
        player_x = player_position[0] - offset_x * self.TILE_SIZE
        player_y = player_position[1]

        # Seleccionar el sprite según la dirección y escalarlo
        sprite = self.sprites.get(direction, self.sprites['parado'])
        sprite = pygame.transform.scale(sprite, (self.TILE_SIZE, self.TILE_SIZE))
        self.screen.blit(sprite, (player_x, player_y))  

    def is_walkable(self, x, y):
        """Comprueba si el tile en (x, y) es transitable."""
        if 0 <= x < self.map_width and 0 <= y < self.map_height:
            return self.map_data[y][x] != '*'
        return False
