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