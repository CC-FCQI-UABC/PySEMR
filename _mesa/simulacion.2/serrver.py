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

# server.py
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from patient_model import PatientModel
from patient_data import PatientData

def agent_portrayal(agent):
    if isinstance(agent, PatientData):
        portrayal = {
            "Shape": "circle",
            "Color": "red" if agent.sick_status else "green",
            "Filled": "true",
            "Layer": 0,
            "r": 0.5
        }
        return portrayal
    return {}

# Calcular tamaño de la cuadrícula basado en el número de pacientes
model = PatientModel()
grid_size = model.calculate_grid_size(len(model.pacientesData['data']))
grid = CanvasGrid(agent_portrayal, grid_size, grid_size, 500, 500)

server = ModularServer(
    PatientModel,
    [grid],
    "Patient Model",
    {}
)

server.port = 8521
server.launch()
