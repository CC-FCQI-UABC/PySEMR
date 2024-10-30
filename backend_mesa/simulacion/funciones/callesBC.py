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

import os
import random

def calle(nombre_ciudad):
    archivo = ""

    # Determine the file name based on the city name
    if nombre_ciudad == 'Tijuana':
        archivo = "callesTijuana.txt"
    elif nombre_ciudad == 'Mexicali':
        archivo = "callesMexicali.txt"
    elif nombre_ciudad == 'Rosarito':
        archivo = "callesRosarito.txt"
    elif nombre_ciudad == 'Tecate':
        archivo = "callesTecate.txt"
    else:  # For Ensenada and other municipalities
        archivo = "callesEnsenada.txt"
    
    # Construct the full file path
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data_mexicana', 'calles', archivo)
    
    linea_aleatoria = None
    contador = 0
    
    # Open the file and read lines
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read each line from the file
        for linea in file:
            contador += 1
            # Randomly select a line based on the count of lines read
            if random.randint(0, contador - 1) == 0:
                linea_aleatoria = linea.strip() 
    
    return linea_aleatoria
