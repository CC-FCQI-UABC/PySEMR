from funciones import numeroTelefono
from faker import Faker

fake = Faker('es_MX')

class ContactData:
    def __init__(self, pacientes_data, pid):
        self.phone_home = pacientes_data['data'][pid]["phone_home"]
        self.phone_biz = pacientes_data['data'][pid]["phone_biz"]
        self.phone_contact = pacientes_data['data'][pid]["phone_contact"]
        self.phone_cell = pacientes_data['data'][pid]["phone_cell"]
        self.email = pacientes_data['data'][pid]["email"]
        self.email_direct = pacientes_data['data'][pid]["email_direct"]