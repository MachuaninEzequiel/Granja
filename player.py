from plant import Plant

class Player:
    def __init__(self, renderer, farm):
        self.position = [1, 5]  # Posición inicial
        self.renderer = renderer
        self.farm = farm

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

    def plant(self, plant_type):
        """Planta un tipo de cultivo en la posición actual."""
        x, y = self.position
        self.farm.plant(x, y, plant_type)

    def harvest(self):
        """Recolecta el cultivo en la posición actual."""
        x, y = self.position
        self.farm.harvest(x, y)