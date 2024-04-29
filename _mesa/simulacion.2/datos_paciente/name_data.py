from funciones import randomizer
import random
from faker import Faker

fake = Faker('es_MX')


class NameData:
    def __init__(self, gender):
        if gender not in ["Male", "Female"]:
            gender = random.choice(["Male", "Female"])
        self.title = self.Title(gender)
        self.fname = self.nameAssign(gender)
        self.lname = fake.last_name() + " " + fake.last_name()
        self.mname = self.nameAssign(gender)
        self.preferred_name = random.choice([self.fname, self.mname])
            
    def nameAssign(self, gender):
        name = ""
        if gender == "Male":
            name = randomizer.randomize('male_names_processed.csv')
        elif gender == "Female":
            name = randomizer.randomize('male_names_processed.csv')
        return name
            
            
    def Title(self, gender):
        title = ""
        if gender == "Male":
            title = random.choice(["Mr.", "Dr."])
        if gender == "Female":
            title = random.choice(["Mrs.", "Ms.", "Dr."])
        return title
