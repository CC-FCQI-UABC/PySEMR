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

import requests

def get_data():
    try:
        # Make a GET request to the Flask server to obtain the data
        response = requests.get('http://localhost:5000/data')

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the data from the JSON response body
            Data = response.json()
            # Return the data
            return Data
        else:
            # Print an error message if the request was not successful
            print("Error retrieving data:", response.text)
    except Exception as e:
        # Print an error message if there was an exception during the request
        print("Error connecting to the server:", e)
