from funciones import randomizer
import random
from faker import Faker

fake = Faker('es_MX')


class NameData:
    def __init__(self, pacientes_data, pid):
        self.title = pacientes_data['data'][pid]["title"]
        self.fname = pacientes_data['data'][pid]["fname"]
        self.lname = pacientes_data['data'][pid]["lname"]
        self.mname = pacientes_data['data'][pid]["mname"]
        self.preferred_name = pacientes_data['data'][pid]["preferred_name"]