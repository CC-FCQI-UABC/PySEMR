######################################################################
## PythonSyntheticElectronicMedicalRecords 1.0
## Modelo computacional de registros medicos electrónicos sintéticos 
## en Python.
######################################################################
## This software are distributed using the Creative Commons Public
## License "Attribution-NonCommercial-ShareAlike 4.0 International"
## https://creativecommons.org/licenses/by-nc-sa/4.0/
######################################################################
## Author: Manuel Castañón Puga, Claudio Emiliano Palacio Martínez, 
## Ricardo Fernando Rosales Cisneros, Carelia Guadalupe Gaxiola
## Pacheco, Luis Enrique Palafox Maestre.
## Copyright: Copyright 2024, Universidad Autónoma de Baja California.
######################################################################
## Credits: matplotlib, mesa, Flask, SQLAlchemy, Faker, requests, 
## tqdm, pandas and click libraries.
## License: CC BY-NC-SA 4.0
## Version: 1.0.0
## Mmaintainer: https://github.com/pugapuga.
## Email: puga@uabc.edu.mx
## Status: Released.
######################################################################

# ambiente.py
from mesa import Agent
from clima import Clima

class Ambiente(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # Initialize the Clima object and add it to the model's schedule
        self.clima = Clima(unique_id, model)
        model.schedule.add(self.clima)
        # Set the initial season
        self.current_season = "Winter"
    
    def update_season(self):
        # Calculate the day of the year from the model's schedule steps
        day_of_year = self.model.schedule.steps % 365
        
        # Determine the current season based on the day of the year
        if 79 <= day_of_year < 172:
            self.current_season = "Spring"
        elif 172 <= day_of_year < 266:
            self.current_season = "Summer"
        elif 266 <= day_of_year < 354:
            self.current_season = "Autumn"
        else:
            self.current_season = "Winter"
    
    def step(self):
        # Update the season and assign it to the Clima object
        self.update_season()
        self.clima.season = self.current_season
        # Call the step method of Clima
        self.clima.step()
