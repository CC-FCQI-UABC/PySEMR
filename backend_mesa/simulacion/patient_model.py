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
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import matplotlib.pyplot as plt
import numpy as np
import os

class PatientModel(Model):
    def __init__(self, Dataset):
        super().__init__()
        self.patients = []  # Lista para almacenar todos los pacientes
        self.schedule = RandomActivation(self)  # Scheduler para manejar la activación de agentes
        self.ambiente = Environment(1, self)  # Objeto de entorno
        self.datasetData = Dataset  # Dataset para información aleatoria
        self.possible_diseases = [
            Enfermedad("Gripe", 0.1, ["Winter", "Autumn"]),
            Enfermedad("Resfriado", 0.1, ["Winter", "Spring"]),
            Enfermedad("COVID-19", 0.1, ["Winter", "Spring", "Summer", "Autumn"])
        ]
        self.enfermos = []  # Lista para rastrear pacientes enfermos
        self.schedule.add(self.ambiente)  # Añadir el ambiente al scheduler
        
        # Inicializar contador por estación
        self.season_counts = {
            "Winter": 0,
            "Spring": 0,
            "Summer": 0,
            "Autumn": 0
        }

    def run_simulation(self, parameters):
        # Ejecuta la simulación durante 365 días
        season = ""
        for day in range(parameters['dias']):
            print(f"Day {day + 1}")
            if (0 <= day <= 90):
                season = "Winter"
            elif (91 <= day <= 182):
                season = "Spring"
            elif (183 <= day <= 274):
                season = "Summer"
            elif (275 <= day <= 365):
                season = "Autumn"
            self.step(parameters, season)  # Ejecutar un paso del modelo
        
        self.plot_seasonal_data()  # Graficar los resultados al final de la simulación
        return self.patients  # Retorna la lista de pacientes
    
    def step(self, parameters, season):
        try:
            self.add_random_patients(parameters["pacientes_por_dia"])  # Agregar pacientes aleatorios
            
            # Impresión de depuración
            print(f"Total pacientes después de agregar: {len(self.patients)}")
            
            self.update_seasonal_counts(season)  # Actualizar los conteos estacionales
            for patient in self.patients:
                patient.step(season)  # Ejecutar paso del paciente
                if patient.sick_status == True:
                    self.enfermos.append(patient)

            self.remove_cured_patients()  # Eliminar pacientes curados
        except Exception as e:
            print(f"Error en el día {self.schedule.time}: {e}")

    def add_random_patients(self, num_patients):
        # Agregar un número específico de pacientes aleatorios al modelo
        for _ in range(num_patients):
            patient = PatientData(self, self.datasetData, len(self.patients))
            self.patients.append(patient)

    def remove_cured_patients(self):
        # Eliminar de la lista de enfermos aquellos que se han curado
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status == False]
        # Mantener todos los pacientes, pero actualizar solo el estado de salud
        self.patients = [patient for patient in self.patients]

    def update_seasonal_counts(self, season):
        # Actualiza el conteo de pacientes enfermos por estación

        self.season_counts[season] = sum(1 for patient in self.patients if patient.sick_status)
        
        print(f"Pacientes totales: {len(self.patients)}")
        print(f"Pacientes enfermos: {sum(1 for p in self.enfermos)}")
        print(f"Pacientes enfermos: {sum(1 for p in self.patients if p.sick_status == True)}")
        print(f"Estación actual: {season}")


    def plot_seasonal_data(self):
        # Graficar los resultados de la simulación
        seasons = list(self.season_counts.keys())
        counts = list(self.season_counts.values())
        print(seasons)
        print(counts)

        plt.bar(seasons, counts, color=['blue', 'green', 'yellow', 'orange'])
        plt.title("Number of patients sick throughout the year according to each season")
        plt.xlabel("Season")
        plt.ylabel("Number of sick patients")
        plt.xticks(rotation=45)
        plt.grid(axis='y')

        # Definir la ruta completa a la carpeta 'frontend/src'
        image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'src'))
        image_path = os.path.join(image_dir, 'seasonal_patient_counts.png')
        
        # Crear el directorio si no existe
        os.makedirs(image_dir, exist_ok=True)

        # Guardar la imagen en el directorio especificado
        plt.savefig(image_path)
        plt.close()  # Cerrar la figura para liberar memoria

        print(f"Imagen guardada en: {image_path}")
        return image_path  # Retornar la ruta de la imagen para que el frontend la use