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

import sys
import os
from mesa import Agent, Model
from funciones import randomizer, numeroTelefono, licenciaConducir
import random
import datetime

class PersonalData:
    def __init__(self, pacientes_data, pid):
        self.language = pacientes_data['data'][pid]["language"]
        self.DOB = self.convertir_fecha(pacientes_data['data'][pid]["DOB"])
        self.sex = pacientes_data['data'][pid]["sex"]
        self.ss = pacientes_data['data'][pid]["ss"]
        self.drivers_license = pacientes_data['data'][pid]["drivers_license"]
        self.occupation = pacientes_data['data'][pid]["occupation"]
        self.status = pacientes_data['data'][pid]["status"]
        self.contact_relationship = pacientes_data['data'][pid]["contact_relationship"]
        self.date = self.convertir_fecha(pacientes_data['data'][pid]["date"])
        self.ethnoracial = pacientes_data['data'][pid]["ethnoracial"]
        self.race = pacientes_data['data'][pid]["race"]
        self.ethnicity = pacientes_data['data'][pid]["ethnicity"]
        self.religion = pacientes_data['data'][pid]["religion"]
        self.family_size = pacientes_data['data'][pid]["family_size"]
        self.monthly_income = pacientes_data['data'][pid]["monthly_income"]
        self.homeless = pacientes_data['data'][pid]["homeless"]
        self.pid = pacientes_data['data'][pid]["pid"]+1
        self.county = "Tijuana"
        self.sexual_orientation = pacientes_data['data'][pid]["sexual_orientation"]
        self.gender_identity = pacientes_data['data'][pid]["gender_identity"]
        self.nationality_country = pacientes_data['data'][pid]["nationality_country"]

    def convertir_fecha(self, fecha_str):
        fecha_str = fecha_str.split(',')[1].strip()
        fecha = datetime.datetime.strptime(fecha_str, '%d %b %Y %H:%M:%S GMT')
        fecha_formatted = fecha.strftime('%Y-%m-%d')
        return fecha_formatted
