from faker import Faker

fake = Faker('es_MX')
def returnMail():
    email = ""
    while not email.endswith("@gmail.com"):
        email = fake.free_email()
    return email
