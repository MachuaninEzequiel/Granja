class Player:
    def __init__(self, renderer):
        self.position = [1, 5]
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


    def plant(self, x, y, plant_type):
        """Planta una planta en las coordenadas dadas."""
        if plant_type == "Lechuga":
            self.renderer.map_data[y][x] = '%'  
        elif plant_type == "Tomate":
            self.renderer.map_data[y][x] = '$'  
        elif plant_type == "Morron amarillo":
            self.renderer.map_data[y][x] = '&'  

    def harvest(self, x, y):
        """Recolecta la planta en las coordenadas dadas (si existe)."""
        if self.renderer.map_data[y][x] in ['%', '$', '&']:  
            plant_type = ("Lechuga" if self.renderer.map_data[y][x] == '%' 
                        else "Tomate" if self.renderer.map_data[y][x] == '$' 
                        else "Morron amarillo")
            self.renderer.map_data[y][x] = ' '  
            print(f"Se cosechó {plant_type} de la posición ({x}, {y})")