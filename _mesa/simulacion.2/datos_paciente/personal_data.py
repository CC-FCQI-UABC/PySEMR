import sys
import os
from mesa import Agent, Model
from funciones import randomizer, numeroTelefono, licenciaConducir
from faker import Faker
import random
import datetime

fake = Faker('es_MX')

class PersonalData:
    def __init__(self, pid):
        self.language = "Español"
        self.DOB = fake.date_of_birth(minimum_age  = 20, maximum_age = 80)
        self.sex = random.choice(["Female", "Male", "Rather not say"])
        self.ss = fake.ssn()
        self.drivers_license = licenciaConducir.licencia()
        self.occupation = fake.job()
        self.status = randomizer.randomize('estadoCivil.txt')
        self.contact_relationship = ""
        self.date = fake.date_between(datetime.date(2000, 1, 1))
        self.ethnoracial = random.choice(["Caucásica/o", "Mestiza/o", "Indígena", "Afrodescendiente"])
        self.race = self.ethnoracial
        self.ethnicity = self.race
        self.religion = random.choice(["Católica", "Protestante/Cristiano evangélico", "Otras religiones", "Sin adscripción religiosa (creyente)", "Sin religión"])
        self.family_size = random.choice(["Tres", "Cuatro", "Cinco"])
        self.monthly_income = "29637"
        self.homeless = random.choice(["Falso", "Verdadero"])
        self.pid = pid
        self.county = "Tijuana"
        self.sexual_orientation = random.choice(["Straight or heterosexual", "Lesbian, gay or homosexual", "Bisexual", "Something else, please describe"])
        self.gender_identity = random.choice(["Identifies as Male", "Identifies as Female", "Female-to-Male (FTM)/Transgender Male/Trans Man", "Male-to-Female (MTF)/Transgender Female/Trans Woman", "Genderqueer, neither exclusively male nor female", "Additional gender category or other, please specify"])
        self.nationality_country = "México"
        