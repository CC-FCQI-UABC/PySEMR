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

import random

class AddressData:
    def __init__(self, domicilios_data):
        idx = random.randint(0, len(domicilios_data) - 1)
        while domicilios_data['data'][idx]["NOMREF1"] == "N/A":
            idx = random.randint(0, len(domicilios_data) - 1)
        # TIPOVIAL + NOMVIAL + NUMEXT 
        self.street = domicilios_data['data'][idx]["TIPOVIAL"] + domicilios_data['data'][idx]["NOMVIAL"] + domicilios_data['data'][idx]["NUMEXT"] 
        self.street_line_2 = domicilios_data['data'][idx]["TIPOASEN"] + domicilios_data['data'][idx]["NOMASEN"]
        # TIPOASEN,NOMASEN
        self.postal_code = domicilios_data['data'][idx]["CP"]
        self.city = "Tijuana"
        self.state = "Baja California"
        self.country_code = "MEX"