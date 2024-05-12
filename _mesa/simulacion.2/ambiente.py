# ambiente.py
from mesa import Agent
from clima import Clima

class Ambiente(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.clima = Clima(unique_id, model)  # Creamos una instancia de Clima
        model.schedule.add(self.clima)  # Agregamos el agente Clima al schedule del modelo
        self.current_season = "Primavera"  # Inicialmente, la temporada es primavera
    
    def update_season(self):
        day_of_year = self.model.schedule.steps % 365
        if 79 <= day_of_year < 172:
            self.current_season = "Primavera"
        elif 172 <= day_of_year < 266:
            self.current_season = "Verano"
        elif 266 <= day_of_year < 354:
            self.current_season = "Otoño"
        else:
            self.current_season = "Invierno"
    
    def step(self):
        self.update_season()  # Actualizamos la temporada
        self.clima.season = self.current_season  # Actualizamos la temporada del clima
        self.clima.step()  # Ejecutamos el paso de Clima
