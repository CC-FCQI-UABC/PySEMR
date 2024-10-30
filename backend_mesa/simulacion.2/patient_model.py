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

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Disease  # Changed to Disease from Enfermedad
from pacientes_data import get_data
from plot import PlotGenerator

class PatientModel(Model):
    def __init__(self, patients_data):
        super().__init__()
        self.patients_data = patients_data
        self.schedule = RandomActivation(self)
        self.patients = []
        self.sick_patients = []

        # Initialize environment and possible diseases
        self.environment = Ambiente(1, self)
        self.possible_diseases = [
            Disease("Flu", 0.1, ["Winter", "Autumn"]),
            Disease("Common cold", 0.1, ["Winter", "Spring"]),
            Disease("COVID-19", 0.0206, ["Winter", "Spring", "Summer", "Autumn"])
        ]
        
        self.schedule.add(self.environment)
        self.load_all_patients()

    def load_all_patients(self):
        for pid in range(len(self.patients_data['data'])):
            patient = PatientData(self, self.patients_data, pid)
            self.patients.append(patient)
            self.schedule.add(patient)

    def step(self):
        self.environment.step()  # Simulate the change of season
        self.schedule.step()

    def remove_cured_patients(self):
        self.sick_patients = [patient for patient in self.sick_patients if patient.sick_status]

    def run_simulation(self, steps=365):
        plot_generator = PlotGenerator()
        diseased_count = []
        temperatures = []

        # Calculate grid dimensions
        num_patients = len(self.patients)
        grid_size = math.ceil(math.sqrt(num_patients))
        
        fig, ax = plt.subplots(figsize=(6, 6))
        im = ax.imshow([[0] * grid_size for _ in range(grid_size)], cmap='viridis', vmin=0, vmax=1)

        def update(day):
            self.step()
            temperatures.append(self.environment.climate.temperature)
            diseased_count.append(len(self.sick_patients))
            self.remove_cured_patients()

            # Update data for visualization based on sick_status of agents
            grid_data = [[0] * grid_size for _ in range(grid_size)]
            for idx, patient in enumerate(self.patients):
                x = idx % grid_size
                y = idx // grid_size
                grid_data[y][x] = 1 if patient.sick_status else 0

            im.set_data(grid_data)
            ax.set_title(f"Day: {day}")
            plt.draw()

        anim = FuncAnimation(fig, update, frames=range(steps), repeat=False)
        plt.tight_layout()
        plt.show()

        # Plot static graphs after the simulation completes
        plot_generator.create_diseased_patients_plot(diseased_count)
        plot_generator.create_disease_distribution_pie_chart(self.sick_patients)
        plot_generator.create_histogram(self.patients)
        plot_generator.create_temperature_disease_correlation(diseased_count, temperatures)

        return self.patients, self.sick_patients

# Example usage
if __name__ == "__main__":
    patients_data = get_data()  # Assuming get_data() function retrieves patient data
    model = PatientModel(patients_data)
    model.run_simulation(steps=365)
