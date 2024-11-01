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
    def __init__(self, gender, Dataset):
        # Ensure gender is either "Male" or "Female"; if not, choose randomly
        if gender not in ["Male", "Female"]:
            gender = random.choice(["Male", "Female"])
        
        # Assign title and names based on gender
        self.title = self.Title(gender)
        self.fname = self.nameAssign(gender, Dataset)
        apellidos = Dataset["data"]["LastNames"]
        self.lname = random.choice(apellidos)["apellido"]
        self.mname = self.nameAssign(gender, Dataset)
        self.preferred_name = random.choice([self.fname, self.mname])
    
    def nameAssign(self, gender, Dataset):
        # Randomly select a name based on gender
        name = ""
        if gender == "Male":
            male_names = Dataset["data"]["MaleNames"]
            name = random.choice(male_names)["Nombre"]
        elif gender == "Female":
            female_names = Dataset["data"]["FemaleNames"]
            name = random.choice(female_names)["Nombre"] 
        return name
    
    def Title(self, gender):
        # Assign a title based on gender
        title = ""
        if gender == "Male":
            title = random.choice(["Mr.", "Dr."])
        elif gender == "Female":
            title = random.choice(["Mrs.", "Ms.", "Dr."])
        return title
