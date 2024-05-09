import os
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from pacientes_data import pacientesData
import matplotlib.pyplot as plt

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
        diseased_count = []
        for day in range(365):
            print(f"Day: {day}")
            diseased_count.append(len(self.enfermos))
            self.step()
            self.remove_cured_patients()

        # Plot the graph of diseased patients
        plt.plot(range(1, 365), diseased_count[1:])
        plt.xlabel('Days')
        plt.ylabel('Number of Diseased Patients')
        plt.title('Diseased Patients Over Time')
        plt.grid(True)
        plt.xlim(0, 366)
        
        # Save the graph in the templates directory
        graph_filename = os.path.join(os.path.dirname(__file__), 'templates', 'diseased_patients_graph.png')
        plt.savefig(graph_filename)
        plt.close()

        return graph_filename, self.patients

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
