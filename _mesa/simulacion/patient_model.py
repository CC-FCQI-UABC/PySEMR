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

# patient_model.py
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Environment
from enfermedad import Enfermedad
from Dataset import Dataset

# Define the PatientModel class inheriting from Mesa's Model
class PatientModel(Model):
    def __init__(self, Dataset):
        super().__init__()
        self.patients = []  # List to store all patient agents
        self.schedule = RandomActivation(self)  # Scheduler to manage agent activation
        self.ambiente = Environment(1, self)  # Environment object
        self.datasetData = Dataset  # Dataset for random information
        # List of possible diseases with their probabilities and affected seasons
        self.possible_diseases = [
            Enfermedad("Gripe", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Resfriado", 0.1, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.1, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        self.enfermos = []  # List to track sick patients
        self.schedule.add(self.ambiente)  # Add the environment to the scheduler
        
    def run_simulation(self):
        # Run the simulation for 365 days
        for day in range(365):
            print(f"Day {day + 1}")
            self.step()  # Execute one step of the model
            self.remove_cured_patients()  # Remove cured patients after each day
        return self.patients  # Return the list of patients

    def step(self):
        # Advance the environment and patient agents by one step
        self.ambiente.step()  # Execute the environment step

        # Create 137 new patients each day
        self.add_random_patients(137)

        # Execute steps for all existing patients
        for patient in self.patients:
            patient.step()

        # Remove cured patients
        self.remove_cured_patients()

    def add_random_patients(self, num_patients):
        # Add a specified number of random patients to the model
        for _ in range(num_patients):
            patient = PatientData(self, self.datasetData, len(self.patients))
            self.patients.append(patient)

    def remove_cured_patients(self):
        # Remove patients who have been cured from the list of sick patients
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status]
