#patient_model.py
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model

from patient_data import PatientData

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.patients = []
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, True)

    def agregar_patient_aleatorio(self, domicilios_data):
        patient = PatientData(self, domicilios_data, len(self.patients))
        self.schedule.add(patient)
        self.patients.append(patient)

    def step(self):
        self.schedule.step()
        schedule.run_pending()