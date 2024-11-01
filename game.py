from player import Player
from plant import Plant
from renderer import Renderer
import pygame

class Game:
    def __init__(self):
        self.renderer = Renderer('map.txt')
        self.player = Player(self.renderer)
        self.running = True

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.move('w')
                    elif event.key == pygame.K_s:
                        self.player.move('s')
                    elif event.key == pygame.K_a:
                        self.player.move('a')
                    elif event.key == pygame.K_d:
                        self.player.move('d')
                    elif event.key == pygame.K_t:
                        x, y = self.player.position
                        self.player.plant(x, y, "Tomate")
                    elif event.key == pygame.K_m:
                        x, y = self.player.position
                        self.player.plant(x, y, "Morron amarillo")
                    elif event.key == pygame.K_l:
                        x, y = self.player.position
                        self.player.plant(x, y, "Lechuga")
                    elif event.key == pygame.K_h:
                        x, y = self.player.position
                        self.player.harvest(x, y)

            self.renderer.render(self.player.position)