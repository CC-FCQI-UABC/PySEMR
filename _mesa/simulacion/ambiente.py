#ambiente.py
import random

class Environment:
    def __init__(self):
        self.temperature = 20
        self.season = "Primavera"
        self.traffic_level = 0

    def simulate_season_change(self):
        # Simular cambios estacionales
        seasons = ["Primavera", "Verano", "Otoño", "Invierno"]
        current_season_index = seasons.index(self.season)
        next_season_index = (current_season_index + 1) % len(seasons)
        self.season = seasons[next_season_index]

        # Ajustar la temperatura según la estación
        if self.season == "Primavera":
            self.temperature = random.randint(15, 25)
        elif self.season == "Verano":
            self.temperature = random.randint(25, 35)
        elif self.season == "Otoño":
            self.temperature = random.randint(10, 20)
        elif self.season == "Invierno":
            self.temperature = random.randint(0, 10)

    def simulate_traffic(self):
        # Simular cambios en el nivel de tráfico
        # Por ejemplo, el nivel de tráfico podría variar aleatoriamente entre 0 y 100
        self.traffic_level = random.randint(0, 100)