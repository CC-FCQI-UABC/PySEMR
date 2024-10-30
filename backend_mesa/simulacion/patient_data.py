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

    def step(self):
        self.heal_diseases()
        if not self.sick_status:
            self.contract_disease()
            
    def contract_disease(self):
        # Iterar sobre las enfermedades posibles para verificar si el paciente contrae alguna
        for disease in self.model.possible_diseases:
            probability = self.calculate_contraction_probability(disease)
            if random.random() < probability:
                if disease not in self.diseases_contracted and len(self.diseases_contracted) < 3:
                    disease.contracted_on = self.model.schedule.time
                    self.diseases_contracted.append(disease)
                    self.sick_status = True
                    self.model.enfermos.append(self)
                break

    def calculate_contraction_probability(self, disease):
        # Base probability
        base_probability = disease.base_probability
        
        # Modify probability based on climate and disease seasonality
        if self.model.ambiente.climate.season in disease.seasonality:
            base_probability *= 1.5  # Increased chance in relevant seasons
        
        # Adjust probability based on temperature
        if self.model.ambiente.climate.temperature < 0:
            base_probability *= 0.5  # Less chance of contraction in extreme cold
        
        # Adjust for existing diseases (e.g., weakened immune system)
        if self.diseases_contracted:
            base_probability *= (1 - 0.1 * len(self.diseases_contracted))  # Reduce by 10% for each contracted disease
        
        # Ensure the probability does not exceed 1
        return min(base_probability, 1)

    def heal_diseases(self):
        for disease in self.diseases_contracted:
            healing_probability = self.calculate_healing_probability(disease)
            if random.random() < healing_probability:
                self.diseases_contracted.remove(disease)
                if not self.diseases_contracted:
                    self.sick_status = False

    def calculate_healing_probability(self, disease):
        # Dynamic healing probability can depend on days since contracted
        days = self.days_since_contracted(disease)
        return max(0.1, 0.9 - (days / 365))  # Healing chance decreases over time

    def days_since_contracted(self, disease):
        return self.model.schedule.time - disease.contracted_on
