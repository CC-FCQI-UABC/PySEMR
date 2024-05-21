# patient_data.py
from mesa import Agent
from faker import Faker
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
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def contract_disease(self):
        for disease in self.model.possible_diseases:
            probability = disease.calculate_probability(self.model.ambiente.clima.temperature, self.model.ambiente.clima.season)
            if random.random() < probability * 0.1:
                if disease not in self.diseases_contracted:
                    if len(self.diseases_contracted) < 3:
                        disease.contracted_on = self.model.schedule.time 
                        self.diseases_contracted.append(disease) 
                        self.sick_status = True
                        self.model.enfermos.append(self)
                        if disease.nombre == "COVID-19":
                            if random.random() < 0.01:
                                self.sick_status = False
                                self.model.enfermos.remove(self)
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
            base_probability *= 0.95
        elif season == "Verano":
            base_probability *= 1.05
        if days_since_contracted > 14:
            base_probability *= 1.1
        base_probability = min(base_probability, 1.0)
        return base_probability
        
    def heal_diseases(self):
        for disease in self.diseases_contracted:
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

    def calculate_window(self, disease):
        for contracted_disease in self.diseases_contracted:
            if contracted_disease.nombre == disease:
                days_since_contracted = self.days_since_contracted(disease)
                if days_since_contracted is not None:
                    if contracted_disease.nombre == "COVID-19":
                        return max(0, 14 - days_since_contracted)
                    else:
                        return max(0, 7 - days_since_contracted)
        return None 