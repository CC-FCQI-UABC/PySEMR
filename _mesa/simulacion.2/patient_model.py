#patient_model.py
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from pacientes_data import pacientesData

class PatientModel(Model):
    def __init__(self, pacientesData):
        super().__init__()
        self.patients = []
        self.schedule = RandomActivation(self)
        self.ambiente = Ambiente(1, self)
        self.pacientesData = pacientesData
        self.possible_diseases = [
            Enfermedad("Influenza", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Resfriado", 0.1, ["Invierno", "Primavera"]),
            
            #Ver /PySEMR/_mesa/simulacion.2/data_epidemiologica/fuentes
            Enfermedad("COVID-19", 0.0206, ["Invierno", "Primavera", "Verano", "Otoño"]) 
        ]
        self.enfermos = []
        self.schedule.add(self.ambiente)
        
    def run_simulation(self):
        self.load_all_patients()
        for day in range(365):
            print(f"Día {day + 1}")
            self.step()
            self.remove_cured_patients()  # quitamos los pacientes curados despues de cada dia
        print(f"Data: {len(self.pacientesData['data'])}")
        print(f"Pacientes: {len(self.patients)}")
        return self.patients

    def load_all_patients(self):
        for pid in range(len(self.pacientesData['data'])):
            patient = PatientData(self, self.pacientesData, pid)
            self.patients.append(patient)

    def step(self):
        self.ambiente.step()  # simulamos el cambio de temporada

        #simulamos el contagio de los pacientes
        for patient in self.patients:
            patient.step()

    def remove_cured_patients(self):
        # quitamos pacientes curados
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status]
