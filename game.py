from player import Player
from farm import Farm
from plant import Plant
from renderer import Renderer
import pygame

class Game:
    def __init__(self):
        self.player = Player()
        self.farm = Farm()
        self.renderer = Renderer('map.txt')
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
                    elif event.key == pygame.K_p:
                        plant = Plant("Tomate", 3)
                        self.player.plant(self.farm, plant)
                    elif event.key == pygame.K_h:
                        self.player.harvest(self.farm)
            self.renderer.render(self.player.position)