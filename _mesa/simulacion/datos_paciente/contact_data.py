from funciones import numeroTelefono
from faker import Faker

fake = Faker('es_MX')

class ContactData:
    def __init__(self, city):
        self.phone_home = numeroTelefono.numeroTelefono(7, city)
        self.phone_biz = numeroTelefono.numeroTelefono(7, city)
        self.phone_contact = numeroTelefono.numeroTelefono(7, city)
        self.phone_cell = numeroTelefono.numeroTelefono(7, city)
        self.email = fake.free_email()
        self.email_direct = self.email