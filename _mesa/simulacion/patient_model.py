import csv
import sys
import os

directorio_padre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if directorio_padre not in sys.path:
    sys.path.append(directorio_padre)

from user import UserModel  # Ahora puedes importar desde el directorio padre
from domicilios_data import domiciliosData
from ambiente import Environment
from enfermedad import Enfermedad
import time
from mesa import Model
from patient_data import PatientData

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.patients = []
        
    def agregar_patient_aleatorio(self, domicilios_data):
        patient = PatientData(self, domicilios_data, len(self.patients))
        self.patients.append(patient)
        
