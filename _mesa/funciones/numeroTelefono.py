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

def numeroTelefono(cantidad_digitos, ciudad):
    min_valor = 10 ** (cantidad_digitos - 1)  
    max_valor = (10 ** cantidad_digitos) - 1 
    digitos = random.randint(min_valor, max_valor)
    numTelefono = "+52" + ladas(ciudad) + str(digitos)
    return numTelefono

def ladas(case):
    if case == "Ensenada" or case == "ENSENADA": 
        return "(646)"
    elif case == "Tijuana" or case ==  "TIJUANA": 
        return "(664)"
    elif case == "Mexicali" or case ==  "MEXICALI": 
        return "(686)"
    elif case == "Tecate" or case ==  "TECATE": 
        return "(665)"
    elif case == "Playas de Rosarito" or case ==  "PLAYAS DE ROSARITO": 
        return "(661)"
    elif case =="San Quintín" or case ==  "SAN QUINTÍN" or case ==  "SAN QUINTIN": 
        return "(616)"
    elif case == "San Felipe" or case ==  "SAN FELIPE": 
        return "(686)"
    elif case =="Valle de Las Palmas" or case == "Valle de Las Palmas":
        return "(665)"#