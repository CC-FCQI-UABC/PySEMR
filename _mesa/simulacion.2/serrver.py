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
