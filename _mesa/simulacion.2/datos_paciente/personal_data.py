import sys
import os
from mesa import Agent, Model
from funciones import randomizer, numeroTelefono, licenciaConducir
from faker import Faker
import random
import datetime

fake = Faker('es_MX')

class PersonalData:
    def __init__(self, pacientes_data, pid):
        self.language = pacientes_data['data'][pid]["language"]
        self.DOB = pacientes_data['data'][pid]["DOB"]
        self.sex = pacientes_data['data'][pid]["sex"]
        self.ss = pacientes_data['data'][pid]["ss"]
        self.drivers_license = pacientes_data['data'][pid]["drivers_license"]
        self.occupation = pacientes_data['data'][pid]["occupation"]
        self.status = pacientes_data['data'][pid]["status"]
        self.contact_relationship = pacientes_data['data'][pid]["contact_relationship"]
        self.date = pacientes_data['data'][pid]["date"]
        self.ethnoracial = pacientes_data['data'][pid]["ethnoracial"]
        self.race = pacientes_data['data'][pid]["race"]
        self.ethnicity = pacientes_data['data'][pid]["ethnicity"]
        self.religion = pacientes_data['data'][pid]["religion"]
        self.family_size = pacientes_data['data'][pid]["family_size"]
        self.monthly_income = pacientes_data['data'][pid]["monthly_income"]
        self.homeless = pacientes_data['data'][pid]["homeless"]
        self.pid = pacientes_data['data'][pid]["pid"]
        self.county = "Tijuana"
        self.sexual_orientation = pacientes_data['data'][pid]["sexual_orientation"]
        self.gender_identity = pacientes_data['data'][pid]["gender_identity"]
        self.nationality_country = pacientes_data['data'][pid]["nationality_country"]
        