from plant import Plant

class Player:
    def __init__(self):
        self.position = [1, 5]  # Posición inicial en la granja

    def move(self, direction):
        if direction == 'w':
            self.position[1] = max(1, self.position[1] - 1)  # Mantener dentro de los límites
        elif direction == 's':
            self.position[1] = min(7, self.position[1] + 1)
        elif direction == 'a':
            self.position[0] = max(1, self.position[0] - 1)
        elif direction == 'd':
            self.position[0] = min(20, self.position[0] + 1)  # Mapa extendido

    def plant(self, farm, plant):
        # Intenta plantar una nueva planta en la posición actual del jugador
        farm.plant_crop(self.position, plant)

    def harvest(self, farm):
        # Intenta cosechar una planta en la posición actual del jugador
        farm.harvest_crop(self.position)