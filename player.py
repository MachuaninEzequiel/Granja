from plant import Plant

class Player:
    def __init__(self, renderer):
        self.position = [1, 5]  # Posición inicial
        self.renderer = renderer

    def move(self, direction):
        new_position = self.position[:]
        if direction == 'w':
            new_position[1] -= 1
        elif direction == 's':
            new_position[1] += 1
        elif direction == 'a':
            new_position[0] -= 1
        elif direction == 'd':
            new_position[0] += 1

        # Verificar si el nuevo tile es transitable
        if self.renderer.is_walkable(new_position[0], new_position[1]):
            self.position = new_position

    def plant(self, farm, plant):
        # Intenta plantar una nueva planta en la posición actual del jugador
        farm.plant_crop(self.position, plant)

    def harvest(self, farm):
        # Intenta cosechar una planta en la posición actual del jugador
        farm.harvest_crop(self.position)