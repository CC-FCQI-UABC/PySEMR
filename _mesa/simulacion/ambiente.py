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

# environment.py
from mesa import Agent
from clima import Climate

# Define the Environment agent class
class Environment(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # Create an instance of the Climate agent
        self.climate = Climate(unique_id, model)
        # Add the Climate agent to the model's schedule
        model.schedule.add(self.climate)

    # Define the step function for the Environment agent
    def step(self):
        # Execute the step function for the Climate agent
        self.climate.step()
