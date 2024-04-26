import sys
import os
from mesa import Agent
from funciones import randomizer, numeroTelefono, licenciaConducir
from faker import Faker
from datos_paciente import PersonalData, ContactData, AddressData
import random
import datetime

# Agregar el directorio padre al sys.path si no está presente
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_padre = os.path.dirname(directorio_actual)
directorio_funciones = os.path.join(directorio_padre, 'funciones')
if directorio_funciones not in sys.path:
    sys.path.append(directorio_funciones)

from user import UserModel

fake = Faker('es_MX')

class PatientData(Agent):
    def __init__(self, model, domicilios_data):
        super().__init__(model)
        self.name_data = NameData()
        self.address_data = AddressData(domicilios_data)
        self.contact_data = ContactData(self.address_data.city)
        self.personal_data = PersonalData()
        self.diseases_contracted = []

    def step(self, environment, possible_diseases):
        # Verificar si el paciente está expuesto a enfermedades y calcular la probabilidad de contraer una enfermedad
        for disease in possible_diseases:
            if disease.calculate_probability(environment.temperature, environment.season):
                if random.random() < disease.calculate_probability(environment.temperature, environment.season):
                    self.diseases_contracted.append(disease.nombre)
