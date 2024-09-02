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

#patient_model.py
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from domicilios_data import domiciliosData

class PatientModel(Model):
    def __init__(self, domiciliosData):
        super().__init__()
        self.patients = []
        self.schedule = RandomActivation(self)
        self.ambiente = Ambiente(1, self)
        self.domicilios = domiciliosData
        self.possible_diseases = [
            Enfermedad("Gripe", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Resfriado", 0.1, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.1, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        self.enfermos = []
        self.schedule.add(self.ambiente)
        
    def run_simulation(self):
        for day in range(365):
            print(f"Día {day + 1}")
            self.step()
            self.remove_cured_patients()  # Remove cured patients after each day
        return self.patients

    def step(self):
        self.ambiente.step()  # Ejecutar el paso del ambiente

        # Crear 137 pacientes nuevos cada día
        self.add_random_patients(1370)

        # Los pacientes existentes realizan sus pasos
        for patient in self.patients:
            patient.step()

        # Remove cured patients
        self.remove_cured_patients()

    def add_random_patients(self, num_patients):
        for _ in range(num_patients):
            # Crear 137 pacientes nuevos cada día
            patient = PatientData(self, self.domicilios, len(self.patients))
            self.patients.append(patient)

    def remove_cured_patients(self):
        # Remove cured patients from the list
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status]