#patient_data.py
from mesa import Agent
from faker import Faker
import random

from datos_paciente.personal_data import PersonalData
from datos_paciente.name_data import NameData
from datos_paciente.contact_data import ContactData
from datos_paciente.address_data import AddressData

# patient_data.py
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
            probability = disease.calculate_probability(self.model.ambiente.clima.temperature, self.model.ambiente.clima.season)
            if random.random() < probability:
                if disease not in self.diseases_contracted:  # Verificar si ya tiene la enfermedad
                    if len(self.diseases_contracted) < 3:
                        disease.contracted_on = self.model.schedule.time 
                        self.diseases_contracted.append(disease)  # Agregar el objeto Enfermedad completo
                        self.sick_status = True
                        self.model.enfermos.append(self)
                break 


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
                    
    def calculate_healing_probability(self, disease, temperature, season, days_since_contracted):
        return 0.9

    def days_since_contracted(self, disease):
        return self.model.schedule.time - disease.contracted_on