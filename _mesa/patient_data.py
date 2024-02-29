from mesa import Agent, Model
from mesa.time import RandomActivation
import datetime
import uuid
import random
from faker import Faker

fake = Faker()

class RegistroMedico(Agent):
    def __init__(self, unique_id, model, uuid, title, language, financial, fname, lname, mname, DOB, street, postal_code, city, state, country_code, drivers_license, ss, occupation, phone_home, phone_biz, phone_contact, phone_cell, pharmacy_id, status, contact_relationship, date, sex):
        super().__init__(unique_id, model)
        # Atributos del agente
        self.uuid = uuid
        self.title = title
        self.language = language
        self.financial = financial
        self.fname = fname
        self.lname = lname
        self.mname = mname
        self.DOB = DOB
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country_code = country_code
        self.drivers_license = drivers_license
        self.ss = ss
        self.occupation = occupation
        self.phone_home = phone_home
        self.phone_biz = phone_biz
        self.phone_contact = phone_contact
        self.phone_cell = phone_cell
        self.pharmacy_id = pharmacy_id
        self.status = status
        self.contact_relationship = contact_relationship
        self.date = date
        self.sex = sex

    def step(self):
        pass

class RegistroModel(Model):
    def __init__(self):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.registros = []

    def step(self):
        self.schedule.step()

    def agregar_registro_aleatorio(self):
        # Generar datos aleatorios
        unique_id = len(self.registros) + 1
        registro = RegistroMedico(
            unique_id, self,
            uuid=str(uuid.uuid4()),
            title=random.choice(["Sr.", "Sra.", "Dr.", "Dra."]),
            language=random.choice(["Español", "Inglés", "Francés"]),
            financial=random.choice(["Alto", "Medio", "Bajo"]),
            fname=fake.first_name(),
            lname=fake.last_name(),
            mname=fake.first_name(),
            DOB=fake.date_of_birth(minimum_age=18, maximum_age=90),
            street=fake.street_address(),
            postal_code=fake.postcode(),
            city=fake.city(),
            state=fake.state(),
            country_code=fake.country_code(),
            drivers_license=fake.bothify(text='???#######'),
            ss=fake.ssn(),
            occupation=fake.job(),
            phone_home=fake.phone_number(),
            phone_biz=fake.phone_number(),
            phone_contact=fake.phone_number(),
            phone_cell=fake.phone_number(),
            pharmacy_id=str(random.randint(1, 100)),
            status=random.choice(["Activo", "Inactivo"]),
            contact_relationship=random.choice(["Hermano", "Padre", "Madre", "Amigo", "Cónyuge"]),
            date=datetime.date.today(),
            sex=random.choice(["M", "F"])
        )
        self.schedule.add(registro)
        self.registros.append(registro)

