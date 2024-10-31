class Plant:
    def __init__(self, name, growth_time):
        self.name = name
        self.growth_time = growth_time
        self.state = 'seed'  # Estado inicial

    def grow(self):
        # Simulación simple del crecimiento
        if self.state == 'seed':
            self.state = 'sprout'
        elif self.state == 'sprout':
            self.state = 'mature'
        print(f"{self.name} ha crecido a estado {self.state}")