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

# Function to generate a random phone number with the specified number of digits and city code
def numeroTelefono(cantidad_digitos, ciudad):
    min_valor = 10 ** (cantidad_digitos - 1)  # Calculate the minimum value for the specified number of digits
    max_valor = (10 ** cantidad_digitos) - 1  # Calculate the maximum value for the specified number of digits
    digitos = random.randint(min_valor, max_valor)  # Generate a random number within the specified range
    numTelefono = "+52" + ladas(ciudad) + str(digitos)  # Construct the phone number with country code and city code
    return numTelefono

# Function to get the city code based on the city name
def ladas(case):
    if case == "Ensenada" or case == "ENSENADA": 
        return "(646)"  # City code for Ensenada
    elif case == "Tijuana" or case == "TIJUANA": 
        return "(664)"  # City code for Tijuana
    elif case == "Mexicali" or case == "MEXICALI": 
        return "(686)"  # City code for Mexicali
    elif case == "Tecate" or case == "TECATE": 
        return "(665)"  # City code for Tecate
    elif case == "Playas de Rosarito" or case == "PLAYAS DE ROSARITO": 
        return "(661)"  # City code for Playas de Rosarito
    elif case == "San Quintín" or case == "SAN QUINTÍN" or case == "SAN QUINTIN": 
        return "(616)"  # City code for San Quintín
    elif case == "San Felipe" or case == "SAN FELIPE": 
        return "(686)"  # City code for San Felipe
    elif case == "Valle de Las Palmas" or case == "Valle de Las Palmas":
        return "(665)"  # City code for Valle de Las Palmas
