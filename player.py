import pygame

class Player:
    def __init__(self, renderer):
        self.position = [20, 25]
        self.renderer = renderer
        self.direction = 'parado'  # Dirección inicial
        self.speed = 1  # Velocidad de movimiento en píxeles por actualización
        self.moving = {'up': False, 'down': False, 'left': False, 'right': False}

    def handle_movement(self):
        """Mueve al jugador continuamente mientras una tecla esté presionada."""
        new_position = self.position[:]  # Posición en píxeles

        if self.moving['up']:
            new_position[1] -= self.speed
            self.direction = 'arriba'
        elif self.moving['down']:
            new_position[1] += self.speed
            self.direction = 'abajo'
        elif self.moving['left']:
            new_position[0] -= self.speed
            self.direction = 'izquierda'
        elif self.moving['right']:
            new_position[0] += self.speed
            self.direction = 'derecha'

        # Convertir la posición a tiles y verificar si es transitable
        tile_x = int(new_position[0] / self.renderer.TILE_SIZE)
        tile_y = int(new_position[1] / self.renderer.TILE_SIZE)
    
        if self.renderer.is_walkable(tile_x, tile_y):
            self.position = new_position  # Actualizar la posición solo si es transitable   

    def start_moving(self, direction):
        """Inicia el movimiento continuo en la dirección dada."""
        if direction == 'w':
            self.moving['up'] = True
        elif direction == 's':
            self.moving['down'] = True
        elif direction == 'a':
            self.moving['left'] = True
        elif direction == 'd':
            self.moving['right'] = True

    def stop_moving(self, direction):
        """Detiene el movimiento y cambia el sprite a 'parado'."""
        if direction == 'w':
            self.moving['up'] = False
        elif direction == 's':
            self.moving['down'] = False
        elif direction == 'a':
            self.moving['left'] = False
        elif direction == 'd':
            self.moving['right'] = False
        self.direction = 'parado'

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
