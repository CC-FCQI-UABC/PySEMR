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

class Enfermedad:
    def __init__(self, nombre, probabilidad_inicial, estaciones_afectadas):
        self.name = nombre
        self.base_probability = probabilidad_inicial
        self.seasonality = estaciones_afectadas
        self.contracted_on = None  # Added attribute to track the date of contracting

    def calculate_probability(self, temperature, season):
        # Check if the current season is affected by the disease
        if season in self.estaciones_afectadas:
            # Adjust the probability based on the season
            if season == "Winter":
                return self.probabilidad_inicial * 1.10
            elif season == "Summer":
                return self.probabilidad_inicial * 0.4
            else:
                return self.probabilidad_inicial
        else:
            return self.probabilidad_inicial
