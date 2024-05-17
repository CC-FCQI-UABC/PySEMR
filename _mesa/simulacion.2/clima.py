# clima.py
from mesa import Agent
import random

class Clima(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.temperature = 20
        self.season = "Primavera"
        self.traffic_level = 0

    def step(self):
        self.simulate_season_change()
        self.simulate_traffic()

    def simulate_season_change(self):
        seasons = ["Primavera", "Verano", "Otoño", "Invierno"]
        current_season_index = seasons.index(self.season)
        next_season_index = (current_season_index + 1) % len(seasons)
        self.season = seasons[next_season_index]

        if self.season == "Primavera":
            self.temperature = random.randint(15, 25)
        elif self.season == "Verano":
            self.temperature = random.randint(25, 35)
        elif self.season == "Otoño":
            self.temperature = random.randint(10, 20)
        elif self.season == "Invierno":
            self.temperature = random.randint(0, 10)

    def simulate_traffic(self):
        self.traffic_level = random.randint(0, 100)
