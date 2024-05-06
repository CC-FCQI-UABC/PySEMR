#patient_data.py
from mesa import Agent
from faker import Faker
import random

from datos_paciente.personal_data import PersonalData
from datos_paciente.name_data import NameData
from datos_paciente.contact_data import ContactData
from datos_paciente.address_data import AddressData

fake = Faker('es_MX')

class PatientData(Agent):
    def __init__(self, model, domicilios_data, pid):
        super().__init__(pid, model)
        self.personal_data = PersonalData(pid)
        self.name_data = NameData(self.personal_data.sex)
        self.address_data = AddressData(domicilios_data)
        self.contact_data = ContactData(self.address_data.city)
        self.diseases_contracted = []

    def step(self):
        for disease in possible_diseases:
            if disease.calculate_probability(environment.temperature, environment.season):
                if random.random() < disease.calculate_probability(environment.temperature, environment.season):
                    self.diseases_contracted.append(disease.nombre)