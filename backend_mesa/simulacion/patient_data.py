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

# patient_data.py
from mesa import Agent
import random
from datos_paciente.personal_data import PersonalData
from datos_paciente.name_data import NameData
from datos_paciente.contact_data import ContactData
from datos_paciente.address_data import AddressData

class PatientData(Agent):
    def __init__(self, model, Dataset, pid):
        super().__init__(pid, model)
        self.personal_data = PersonalData(pid)
        self.name_data = NameData(self.personal_data.sex, Dataset)
        self.address_data = AddressData(Dataset)
        self.contact_data = ContactData(self.address_data.city)
        self.diseases_contracted = []
        self.sick_status = False  # Indicates if the patient is sick

    def step(self, season):
        if self.sick_status:
            self.heal_diseases()
        else:
            self.contract_disease(season)
            
    def contract_disease(self, season):
        # Simplified random chance of contracting a disease
        if len(self.diseases_contracted) < 3:
            probability = 0.01
            if season == "Summer":
                probability *= 1
            elif season == "Spring":
                probability *= 3
            elif season == "Autumn":
                probability *= 4
            elif season == "Winter":
                probability *= 7
            if random.random() < probability:
                disease = random.choice(self.model.possible_diseases)
                if disease not in self.diseases_contracted:
                    self.diseases_contracted.append(disease)
                    self.sick_status = True
                    self.model.enfermos.append(self)

    def heal_diseases(self):
        # Simplified random chance of healing from diseases
        for disease in list(self.diseases_contracted):  # Iterate over a copy of the list
            if random.random() < 0.2:  # 20% chance to heal from each disease
                self.diseases_contracted.remove(disease)
                if not self.diseases_contracted:  # If no diseases remain
                    self.sick_status = False
                    break
