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

from faker import Faker

fake = Faker('es_MX')

class NameData:
    def __init__(self, pacientes_data, pid):
        self.title = pacientes_data['data'][pid]["title"]
        self.fname = pacientes_data['data'][pid]["fname"]
        self.lname = pacientes_data['data'][pid]["lname"]
        self.mname = pacientes_data['data'][pid]["mname"]
        self.preferred_name = pacientes_data['data'][pid]["preferred_name"]
    
    def full_name(self):
        return self.fname + " " + self.mname + " " + self.lname