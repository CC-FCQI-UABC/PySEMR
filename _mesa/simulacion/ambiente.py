# ambiente.py
from mesa import Agent
from clima import Clima

class Ambiente(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.clima = Clima(unique_id, model)  # Creamos una instancia de Clima
        model.schedule.add(self.clima)  # Agregamos el agente Clima al schedule del modelo

    def step(self):
        self.clima.step()  # Ejecutamos el paso de Clima
