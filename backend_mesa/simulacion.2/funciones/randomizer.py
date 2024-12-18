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

# Function to select a random line from a file
def randomize(file_name):
    # Construct the full path to the file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data_mexicana', file_name)
    
    # Open the file and read all lines
    with open(file_path, 'r') as f:
        lines = f.readlines()  # Read all lines from the file
        # Select a random line and strip any leading/trailing whitespace
        return random.choice(lines).strip()
