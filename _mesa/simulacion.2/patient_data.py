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
    def __init__(self, model, pacientes_data, pid):
        super().__init__(pid, model)
        self.personal_data = PersonalData(pacientes_data, pid)
        self.name_data = NameData(pacientes_data, pid)
        self.address_data = AddressData(pacientes_data, pid)
        self.contact_data = ContactData(pacientes_data, pid)
        self.diseases_contracted = []
        self.sick_status = False

    def step(self):
        self.heal_diseases()
        if not self.sick_status:
            self.contract_disease()

    def contract_disease(self):
        for disease in self.model.possible_diseases:
            probability = disease.calculate_probability(
                self.model.ambiente.clima.temperature, 
                self.model.ambiente.clima.season)
            if disease.nombre == "COVID-19":
                if random.random() < 0.0206:  # Estadistica implementada de la bibliografia
                    if disease not in self.diseases_contracted:
                        if len(self.diseases_contracted) < 3:
                            disease.contracted_on = self.model.schedule.time 
                            self.diseases_contracted.append(disease) 
                            self.sick_status = True
                            self.model.enfermos.append(self)
                        else:
                            break
            else:
                if random.random() < probability * 0.1:
                    if disease not in self.diseases_contracted:
                        if len(self.diseases_contracted) < 3:
                            disease.contracted_on = self.model.schedule.time 
                            self.diseases_contracted.append(disease) 
                            self.sick_status = True
                            self.model.enfermos.append(self)
                            break
                        else:
                            break
    
    def calculate_healing_probability(self, disease, temperature, season, days_since_contracted):
        base_probability = 0.9
        if disease.nombre == "Influenza":
            base_probability *= 1.1
        elif disease.nombre == "Resfriado":
            base_probability *= 1.05
        if temperature > 25:
            base_probability *= 1.1
        elif temperature < 10:
            base_probability *= 0.95
        if season == "Invierno":
            base_probability *= 0.85
        elif season == "Verano":
            base_probability *= 1.15
        if days_since_contracted > 14:
            base_probability *= 1.1
        base_probability = min(base_probability, 1.0)
        return base_probability
        

    def heal_diseases(self):
        for disease in self.diseases_contracted:
            if disease.nombre == "COVID-19":
                days_since_contracted = self.days_since_contracted(disease)
                if days_since_contracted is not None and days_since_contracted > 4:
                    if random.random() < 0.016025:  # Estadistica implementada de la bibliografia
                        self.model.fallecidos += 1
                        self.model.schedule.remove(self)
                        return
                else:
                    if random.random() < 0.1:
                        self.diseases_contracted.remove(disease)
                        if not self.diseases_contracted:
                            self.sick_status = False
            else:
                self.heal_normal_disease(disease)

    def heal_normal_disease(self, disease):
        healing_probability = self.calculate_healing_probability(
            disease,
            self.model.ambiente.clima.temperature,
            self.model.ambiente.clima.season,
            self.days_since_contracted(disease)
        )
        if random.random() < healing_probability:
            self.diseases_contracted.remove(disease)
            if not self.diseases_contracted:
                self.sick_status = False

    def days_since_contracted(self, disease):
        for contracted_disease in self.diseases_contracted:
            if contracted_disease.nombre == disease:
                return self.model.schedule.time - contracted_disease.contracted_on
        return 0
