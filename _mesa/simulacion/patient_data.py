import sys
import os
from mesa import Agent, Model
from funciones import randomizer, numeroTelefono, licenciaConducir
from faker import Faker
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

class NameData:
    def __init__(self, gender):
        self.title = "" 
        self.fname = ""
        self.lname = fake.last_name() + " " + fake.last_name()
        self.mname = ""
        
        if gender == "Male":
            self.fname = randomizer.randomize('male_names_processed.csv')
            self.mname = randomizer.randomize('male_names_processed.csv')
            self.title = random.choice(["Mr.", "Dr."])
        elif gender == "Female":
            self.fname = randomizer.randomize('female_names_processed.csv')
            self.mname = randomizer.randomize('female_names_processed.csv')
            self.title = random.choice(["Mrs.", "Ms.", "Dr."])
        
        self.preferred_name = random.choice([self.fname, self.mname])

class AddressData:
    def __init__(self, domicilios_data):
        idx = random.randint(0, len(domicilios_data.data) - 1)
        while domicilios_data.data['data'][idx]["NOMREF1"] == "N/A":
            idx = random.randint(0, len(domicilios_data.data) - 1)
        self.street = domicilios_data.data['data'][idx]["NOMREF1"]
        self.street_line_2 = domicilios_data.data['data'][idx]["NOMREF2"]
        self.postal_code = domicilios_data.data['data'][idx]["CP"]
        self.city = "Tijuana"
        self.state = "Baja California"
        self.country_code = "MEX"

class ContactData:
    def __init__(self, city):
        self.phone_home = numeroTelefono.numeroTelefono(7, city)
        self.phone_biz = numeroTelefono.numeroTelefono(7, city)
        self.phone_contact = numeroTelefono.numeroTelefono(7, city)
        self.phone_cell = numeroTelefono.numeroTelefono(7, city)
        self.email = fake.free_email()

class PersonalData:
    def __init__(self, pid):
        self.DOB = fake.date_of_birth(minimum_age  = 20, maximum_age = 80)
        self.sex = random.choice(["Female", "Male", "Unknown"])
        self.ss = fake.ssn()
        self.occupation = fake.job()
        self.status = randomizer.randomize('estadoCivil.txt')
        self.contact_relationship = ""
        self.date = fake.date_between(datetime.date(2000, 1, 1))
        self.ethnoracial = random.choice(["Caucásica/o", "Mestiza/o", "Indígena", "Afrodescendiente"])
        self.religion = random.choice(["Católica", "Protestante/Cristiano evangélico", "Otras religiones", "Sin adscripción religiosa (creyente)", "Sin religión"])
        self.family_size = random.choice(["Tres", "Cuatro", "Cinco"])
        self.monthly_income = "29637"
        self.homeless = random.choice(["Falso", "Verdadero"])
        self.pid = pid
        self.county = "Tijuana"
        self.sexual_orientation = random.choice(["Straight or heterosexual", "Lesbian, gay or homosexual", "Bisexual", "Something else, please describe"])
        self.gender_identity = random.choice(["Identifies as Male", "Identifies as Female", "Female-to-Male (FTM)/Transgender Male/Trans Man", "Male-to-Female (MTF)/Transgender Female/Trans Woman", "Genderqueer, neither exclusively male nor female", "Additional gender category or other, please specify"])
        self.nationality_country = "México"

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

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.patients = []
        
    def agregar_patient_aleatorio(self, domicilios_data):
        patient = PatientData(self, domicilios_data, len(self.patients))
        self.patients.append(patient)