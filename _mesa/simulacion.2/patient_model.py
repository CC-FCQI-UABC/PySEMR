#patient_model.py
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Environment
from enfermedad import Enfermedad
from domicilios_data import domiciliosData

class PatientModel(Model):
    def __init__(self, domiciliosData):
        super().__init__()
        self.patients = []
        self.schedule = RandomActivation(self)
        self.environment = Environment()
        self.domicilios = domiciliosData
        self.possible_diseases = [
            Enfermedad("Gripe", 0.2, ["Invierno", "Otoño"]),
            Enfermedad("Resfriado", 0.15, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.1, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        self.enfermos = []
        
    def run_simulation(self):
        for day in range(365):
            print(f"Día {day + 1}")
            self.step()
        return self.patients

    def step(self):
        self.environment.simulate_season_change()
        self.environment.simulate_traffic()

        for _ in range(137):
            self.agregar_patient_aleatorio(self.domicilios)

        self.schedule.step()

    def agregar_patient_aleatorio(self, domicilios_data):
        patient = PatientData(self, domicilios_data, len(self.patients))
        self.schedule.add(patient)
        self.patients.append(patient)