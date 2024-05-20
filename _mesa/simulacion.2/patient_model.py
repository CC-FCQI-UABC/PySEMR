import os
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from pacientes_data import get_data
import matplotlib.pyplot as plt
import mpld3
from plot import PlotGenerator
import math
from datetime import datetime  # Import datetime for age calculation
from mesa.time import RandomActivation
from mesa import Model
from mesa.space import MultiGrid

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.pacientesData = get_data()
        num_patients = len(self.pacientesData['data'])
        grid_size = self.calculate_grid_size(num_patients)
        self.grid = MultiGrid(grid_size, grid_size, torus=True)
        self.schedule = RandomActivation(self)
        self.patients = []
        self.ambiente = Ambiente(1, self)
        self.possible_diseases = [
            Enfermedad("Flu", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Common cold", 0.1, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.0206, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        self.enfermos = []
        self.schedule.add(self.ambiente)
        self.load_all_patients()

    def calculate_grid_size(self, num_agents):
        size = math.ceil(math.sqrt(num_agents))
        while size ** 2 < num_agents:
            size += 1
        return size

    def load_all_patients(self):
        for pid in range(len(self.pacientesData['data'])):
            patient = PatientData(self, self.pacientesData, pid)
            self.patients.append(patient)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(patient, (x, y))
            self.schedule.add(patient)

    def step(self):
        self.ambiente.step()
        self.schedule.step()

    def remove_cured_patients(self):
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status]

    def run_simulation(self):
        plotGenerator = PlotGenerator()
        diseased_count = []
        for day in range(365):
            print(f"Day: {day}")
            diseased_count.append(len(self.enfermos))
            self.step()
            self.remove_cured_patients()
        
        plotGenerator.create_diseased_patients_plot(diseased_count)
        plotGenerator.create_histogram(self.patients)
        plotGenerator.create_disease_distribution_pie_chart(self.patients)
        plotGenerator.save_html_files("diseased_patients_graph.html", "patients_histogram.html", "disease_distribution_pie_chart.html")

        return self.patients, self.enfermos