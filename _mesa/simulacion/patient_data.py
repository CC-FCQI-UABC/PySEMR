import sys
import os
from mesa import Agent, Model
from funciones import randomizer, numeroTelefono, licenciaConducir
from faker import Faker
import random
import datetime

from datos_paciente.personal_data import PersonalData
from datos_paciente.name_data import NameData
from datos_paciente.contact_data import ContactData
from datos_paciente.address_data import AddressData

# Agregar el directorio padre al sys.path si no está presente
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_padre = os.path.dirname(directorio_actual)
directorio_funciones = os.path.join(directorio_padre, 'funciones')
if directorio_funciones not in sys.path:
    sys.path.append(directorio_funciones)

from user import UserModel

fake = Faker('es_MX')

class PatientData(Agent):
    def __init__(self, model, domicilios_data, pid):
        super().__init__(self, model)
        self.personal_data = PersonalData(pid)
        self.name_data = NameData(self.personal_data.sex)
        self.address_data = AddressData(domicilios_data)
        self.contact_data = ContactData(self.address_data.city)
        self.diseases_contracted = []

    def step(self, environment, possible_diseases):
        # Verificar si el paciente está expuesto a enfermedades y calcular la probabilidad de contraer una enfermedad
        for disease in possible_diseases:
            if disease.calculate_probability(environment.temperature, environment.season):
                if random.random() < disease.calculate_probability(environment.temperature, environment.season):
                    self.diseases_contracted.append(disease.nombre)