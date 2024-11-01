class Farm:
    def __init__(self, renderer):
        self.renderer = renderer

    def plant(self, x, y, plant_type):
        """Planta una planta en las coordenadas dadas."""
        if plant_type == "Lechuga":
            self.renderer.map_data[y][x] = '%'  
        elif plant_type == "Tomate":
            self.renderer.map_data[y][x] = '$'  

    def harvest(self, x, y):
        """Recolecta la planta en las coordenadas dadas (si existe)."""
        if self.renderer.map_data[y][x] in ['%', '$']:  
            self.renderer.map_data[y][x] = ' ' 
