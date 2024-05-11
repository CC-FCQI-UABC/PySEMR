# patient_model.py
import os
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from pacientes_data import get_data
import matplotlib.pyplot as plt
import mpld3
from plot import PlotGenerator

from mesa.time import RandomActivation
from mesa import Model

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.patients = []
        self.schedule = RandomActivation(self)
        self.ambiente = Ambiente(1, self)
        self.pacientesData = get_data()
        self.possible_diseases = [
            Enfermedad("Influenza", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Resfriado", 0.1, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.0206, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        self.enfermos = []
        self.schedule.add(self.ambiente)
        
    def run_simulation(self):
        plotGenerator = PlotGenerator()
        self.load_all_patients()
        diseased_count = []
        for day in range(365):
            print(f"Day: {day}")
            diseased_count.append(len(self.enfermos))
            self.step()
            self.remove_cured_patients()
        
        plotGenerator.create_diseased_patients_plot(diseased_count)
        plotGenerator.save_html_files("diseased_patients_graph.html")

        return self.patients

    def load_all_patients(self):
        for pid in range(len(self.pacientesData['data'])):
            patient = PatientData(self, self.pacientesData, pid)
            self.patients.append(patient)

    def step(self):
        self.ambiente.step()  # simulate the change of season

        # simulate the contagion of the patients
        for patient in self.patients:
            patient.step()

    def remove_cured_patients(self):
        # remove cured patients
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status]

