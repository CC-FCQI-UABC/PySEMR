from mesa import Agent, Model
from mesa.time import RandomActivation
import uuid
import datetime
from faker import Faker
from funciones import randomizer, numeroTelefono, googleSigninMail, callesBC, licenciaConducir

import random

# Data visualization tools
import seaborn as sns

import numpy as np

import pandas as pd
fake = Faker('es_MX')

class User(Agent):
    def __init__(self, model):
        super().__init__(self, model)
        self.id = 0
        self.uuid = "0x" + uuid.uuid4().hex
        self.username = ""
        self.password = ""
        self.authorized = random.choice([True, False])
        self.info = ""
        self.source = ""
        self.fname = ""   #Llenada al final
        self.mname = ""   #Llenada al final
        self.lname = fake.last_name() + " " + fake.last_name()
        self.suffix = ""
        self.federaltaxid = ""
        self.federaldrugid = ""
        self.upin = ""
        self.facility = ""
        self.facility_id = ""
        self.see_auth = ""
        self.active = random.choice([True, False])
        self.npi = ""
        self.title = ""
        self.specialty = fake.job()
        self.billname = ""
        self.email = fake.free_email()
        self.email_direct = ""
        self.google_signin_email = random.choice([self.email, googleSigninMail.returnMail()]) if self.email.endswith('gmail.com') else googleSigninMail.returnMail()
        self.url = ""
        self.assistant = fake.first_name() + " " + fake.first_name() + " " + fake.last_name() + " " + fake.last_name()
        self.organization = fake.company()
        self.valedictory = ""
        self.street = "" #Llenado mas adelante
        self.streetb = "" #Dejar en vacio?
        self.city = randomizer.randomize('municipios.txt')
        self.state = "Baja California"
        self.zip = None
        self.street2 = "" #Dejar en vacio?
        self.streetb2 = "" #Dejar en vacio?
        self.city2 = "" #Dejar en vacio?
        self.state2 = "" #Dejar en vacio?
        self.zip2 = ""
        self.phone = numeroTelefono.numeroTelefono(7, self.city)
        self.fax = ""
        self.phonew1 = numeroTelefono.numeroTelefono(7, self.city)
        self.phonew2 = numeroTelefono.numeroTelefono(7, self.city)
        self.phonecell = numeroTelefono.numeroTelefono(7, self.city)
        self.notes = ""
        self.cal_ui = ""
        self.taxonomy = ""
        self.calendar = date = f"{random.randint(2020, 2023)}-{random.randint(1, 12)}-{random.randint(1, 30)}"       
        self.abook_type = ""
        self.default_warehouse = ""
        self.irnpool = ""
        self.state_license_number = ""
        self.weno_prov_id = ""
        self.newcrop_user_role = ""
        self.cpoe = ""
        self.physician_type = ""
        self.main_menu_role = ""
        self.patient_menu_role = ""
        self.portal_user = ""
        self.supervisor_id = ""
        self.billing_facility = ""
        self.billing_facility_id = ""
        self.DOB = ""
        self.gender = random.choice(["male", "female", "non-binary"])
        
        if self.gender == "male":
            self.fname = fake.first_name_male()
            self.mname = fake.first_name_male()
        elif self.gender == "female":
            self.fname = fake.first_name_female()
            self.mname = fake.first_name_female()
            
        self.street = callesBC.calle(self.city)
            

    def step(self):
        pass

class UserModel(Model):
    def __init__(self):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.users = []

    def step(self):
        self.schedule.step()
        
    def agregar_usuario_aleatorio(self):
        usuario = User(self)
        usuario.id = len(self.users) + 1
        self.schedule.add(usuario)
        self.users.append(usuario)
        self.schedule.step()