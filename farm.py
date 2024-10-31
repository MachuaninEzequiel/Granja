class Farm:
    def __init__(self):
        # Usamos un diccionario para almacenar las posiciones de las plantas
        self.crops = {}

    def plant_crop(self, position, plant):
        # Planta un cultivo en la posición dada, si está libre
        if tuple(position) not in self.crops:
            self.crops[tuple(position)] = plant
            print(f"Plantado {plant.name} en {position}")
        else:
            print("Ya hay un cultivo en esta posición.")

    def harvest_crop(self, position):
        # Cosecha el cultivo en la posición dada, si existe
        if tuple(position) in self.crops:
            harvested_plant = self.crops.pop(tuple(position))
            print(f"Se ha recolectado {harvested_plant.name} de {position}")
        else:
            print("No hay cultivo para cosechar en esta posición.")
