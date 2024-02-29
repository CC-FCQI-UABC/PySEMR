from mesa import Agent, Model
from mesa.time import RandomActivation
import uuid
from faker import Faker

# Data visualization tools.
import seaborn as sns

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd
fake = Faker()

class User(Agent):
    def __init__(self, model, user_id, username, password, **kwargs):
        super().__init__(user_id, model)
        self.uuid = str(uuid.uuid4())
        self.username = username
        self.password = password
        self.authorized = kwargs.get('authorized', False)
        self.info = kwargs.get('info', '')
        self.source = kwargs.get('source', 'internal')
        self.fname = kwargs.get('fname', fake.first_name())
        self.mname = kwargs.get('mname', fake.first_name())
        self.lname = kwargs.get('lname', fake.last_name())
        self.suffix = kwargs.get('suffix', '')
        self.federaltaxid = kwargs.get('federaltaxid', '')
        self.federaldrugid = kwargs.get('federaldrugid', '')
        self.upin = kwargs.get('upin', '')
        self.facility = kwargs.get('facility', '')
        self.facility_id = kwargs.get('facility_id', 0)
        self.see_auth = kwargs.get('see_auth', '')
        self.active = kwargs.get('active', True)
        self.npi = kwargs.get('npi', '')
        self.title = kwargs.get('title', '')
        self.specialty = kwargs.get('specialty', '')
        self.billname = kwargs.get('billname', '')
        self.email = kwargs.get('email', fake.email())
        self.email_direct = kwargs.get('email_direct', '')
        self.google_signin_email = kwargs.get('google_signin_email', '')
        self.url = kwargs.get('url', '')
        self.assistant = kwargs.get('assistant', '')
        self.organization = kwargs.get('organization', '')
        self.valedictory = kwargs.get('valedictory', '')
        self.street = kwargs.get('street', fake.street_address())
        self.streetb = kwargs.get('streetb', '')
        self.city = kwargs.get('city', fake.city())
        self.state = kwargs.get('state', fake.state_abbr())
        self.zip = kwargs.get('zip', fake.zipcode())
        self.street2 = kwargs.get('street2', '')
        self.streetb2 = kwargs.get('streetb2', '')
        self.city2 = kwargs.get('city2', '')
        self.state2 = kwargs.get('state2', '')
        self.zip2 = kwargs.get('zip2', '')
        self.phone = kwargs.get('phone', fake.phone_number())
        self.fax = kwargs.get('fax', '')
        self.phonew1 = kwargs.get('phonew1', '')
        self.phonew2 = kwargs.get('phonew2', '')
        self.phonecell = kwargs.get('phonecell', fake.phone_number())
        self.notes = kwargs.get('notes', '')
        self.cal_ui = kwargs.get('cal_ui', 1)
        self.taxonomy = kwargs.get('taxonomy', '')
        self.calendar = kwargs.get('calendar', 1)
        self.abook_type = kwargs.get('abook_type', '')
        self.default_warehouse = kwargs.get('default_warehouse', '')
        self.irnpool = kwargs.get('irnpool', '')
        self.state_license_number = kwargs.get('state_license_number', '')
        self.weno_prov_id = kwargs.get('weno_prov_id', '')
        self.newcrop_user_role = kwargs.get('newcrop_user_role', '')
        self.cpoe = kwargs.get('cpoe', False)
        self.physician_type = kwargs.get('physician_type', '')
        self.main_menu_role = kwargs.get('main_menu_role', '')
        self.patient_menu_role = kwargs.get('patient_menu_role', '')
        self.portal_user = kwargs.get('portal_user', False)
        self.supervisor_id = kwargs.get('supervisor_id', 0)
        self.billing_facility = kwargs.get('billing_facility', '')
        self.billing_facility_id = kwargs.get('billing_facility_id', 0)

    def step(self):
        # Aquí se pueden definir acciones específicas que los usuarios pueden realizar
        pass

class UserModel(Model):
    def __init__(self):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.users = []

    def step(self):
        self.schedule.step()

    def agregar_usuario_aleatorio(self):
        # Generar datos aleatorios
        user_id = len(self.users) + 1
        usuario = User(
            self,
            user_id,
            username=fake.user_name(),
            password=fake.password(),
            info=fake.text(),
            fname=fake.first_name(),
            lname=fake.last_name(),
            mname=fake.first_name(),
            federaltaxid=fake.ean8(),
            federaldrugid=fake.ean8(),
            upin=fake.ean8(),
            facility=fake.company(),
            npi=fake.ean8(),
            title=fake.prefix(),
            specialty=fake.job(),
            email=fake.email(),
            phone=fake.phone_number(),
            street=fake.street_address(),
            city=fake.city(),
            state=fake.state_abbr(),
            zip=fake.zipcode(),
            phonecell=fake.phone_number(),
            notes=fake.text(),
            state_license_number=fake.bothify(text='?????????'),
            physician_type=fake.job(),
            billing_facility=fake.company()
        )
        self.schedule.add(usuario)
        self.users.append(usuario)
