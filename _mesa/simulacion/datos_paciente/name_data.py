######################################################################
## PythonSyntheticElectronicMedicalRecords 1.0
## Modelo computacional de registros medicos electrónicos sintéticos 
## en Python.
######################################################################
## This software are distributed using the Creative Commons Public
## License "Attribution-NonCommercial-ShareAlike 4.0 International"
## https://creativecommons.org/licenses/by-nc-sa/4.0/
######################################################################
## Author: Manuel Castañón Puga, Claudio Emiliano Palacio Martínez, 
## Ricardo Fernando Rosales Cisneros, Carelia Guadalupe Gaxiola
## Pacheco, Luis Enrique Palafox Maestre.
## Copyright: Copyright 2024, Universidad Autónoma de Baja California.
######################################################################
## Credits: matplotlib, mesa, Flask, SQLAlchemy, Faker, requests, 
## tqdm, pandas and click libraries.
## License: CC BY-NC-SA 4.0
## Version: 1.0.0
## Mmaintainer: https://github.com/pugapuga.
## Email: puga@uabc.edu.mx
## Status: Released.
######################################################################
from funciones import randomizer
import random
from faker import Faker

fake = Faker('es_MX')

class NameData:
    def __init__(self, gender):
        # Ensure gender is either "Male" or "Female"; if not, choose randomly
        if gender not in ["Male", "Female"]:
            gender = random.choice(["Male", "Female"])
        
        # Assign title and names based on gender
        self.title = self.Title(gender)
        self.fname = self.nameAssign(gender)
        self.lname = fake.last_name() + " " + fake.last_name()
        self.mname = self.nameAssign(gender)
        self.preferred_name = random.choice([self.fname, self.mname])
    
    def nameAssign(self, gender):
        # Randomly select a name based on gender
        name = ""
        if gender == "Male":
            name = randomizer.randomize('male_names_processed.csv')
        elif gender == "Female":
            name = randomizer.randomize('female_names_processed.csv')
        return name
    
    def Title(self, gender):
        # Assign a title based on gender
        title = ""
        if gender == "Male":
            title = random.choice(["Mr.", "Dr."])
        elif gender == "Female":
            title = random.choice(["Mrs.", "Ms.", "Dr."])
        return title
