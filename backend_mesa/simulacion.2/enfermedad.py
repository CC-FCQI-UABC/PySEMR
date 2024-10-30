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

# enfermedad.py

class Enfermedad:
    def __init__(self, nombre, probabilidad_inicial, estaciones_afectadas):
        # Inicializa una instancia de Enfermedad con el nombre, probabilidad inicial y estaciones afectadas.
        self.nombre = nombre
        self.probabilidad_inicial = probabilidad_inicial
        self.estaciones_afectadas = estaciones_afectadas
        self.contracted_on = None

    def calculate_probability(self, temperature, season):
        # Calcula la probabilidad ajustada de contraer la enfermedad según la estación actual.
        if season in self.estaciones_afectadas:
            if season == "Invierno":
                return self.probabilidad_inicial * 1.20
            elif season == "Primavera":
                return self.probabilidad_inicial * 0.4                
            elif season == "Verano":
                return self.probabilidad_inicial * 0.7
            elif season == "Otoño":
                return self.probabilidad_inicial * 1.1
            else:
                return self.probabilidad_inicial
        else:
            return self.probabilidad_inicial
