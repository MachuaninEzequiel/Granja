from player import Player
from plant import Plant
from renderer import Renderer
import pygame

class Game:
    def __init__(self):
        self.renderer = Renderer("map.txt")
        self.player = Player(self.renderer)
        self.clock = pygame.time.Clock()  # Control de la tasa de fotogramas

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.start_moving('w')
                    elif event.key == pygame.K_s:
                        self.player.start_moving('s')
                    elif event.key == pygame.K_a:
                        self.player.start_moving('a')
                    elif event.key == pygame.K_d:
                        self.player.start_moving('d')
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player.stop_moving('w')
                    elif event.key == pygame.K_s:
                        self.player.stop_moving('s')
                    elif event.key == pygame.K_a:
                        self.player.stop_moving('a')
                    elif event.key == pygame.K_d:
                        self.player.stop_moving('d')

            
            self.renderer.render(self.player.position, self.player.direction)
            # Mueve al jugador y renderiza la pantalla
            self.player.handle_movement()
            
            # Control de la velocidad de fotogramas
            self.clock.tick(60)

        pygame.quit()