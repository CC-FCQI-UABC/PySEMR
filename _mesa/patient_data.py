from mesa import Agent, Model
from mesa.time import RandomActivation
import user
import datetime
import uuid

import random
from faker import Faker
from funciones import randomizer, numeroTelefono

fake = Faker('es_MX')

class PatientData(Agent):
    def __init__(self, model, user):
        super().__init__(self, model)
        self.id = 0
        self.uuid = "0x" + uuid.uuid4().hex
        self.title = ""
        self.language = "Español"
        self.financial = ""
        self.fname = user.fname
        self.mname = user.mname
        self.lname = user.lname
        self.DOB = user.DOB
        self.street = user.street
        self.postal_code = user.zip
        self.city = user.city
        self.state = "Baja California"
        self.country_code = "52"
        self.drivers_license = user.state_license_number
        self.ss = fake.ssn()
        self.occupation = random.choice([user.specialty, fake.job()])
        self.phone_home = user.phone
        self.phone_biz = numeroTelefono.numeroTelefono(7, self.city)
        self.phone_contact = numeroTelefono.numeroTelefono(7, self.city)
        self.phone_cell = user.phonecell
        self.pharmacy_id = ""
        self.status = randomizer.randomize('estadoCivil.txt')
        self.contact_relationship = randomizer.randomize('vinculosContactos.txt')
        self.date = fake.date_between(datetime.date(2000, 1, 1))
        self.sex = user.gender
        
    def step(self):
        pass

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.patients = []

    def step(self):
        self.schedule.step()

    def agregar_patient_aleatorio(self, user):
        patient = PatientData(self, user)
        patient.id = len(self.patients) + 1
        self.schedule.add(patient)
        self.patients.append(patient)
        self.schedule.step()