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

class domiciliosData:
    def __init__(self):
        self.data = None
        try:
            # Realiza una solicitud GET al servidor Flask para obtener los datos
            response = requests.get('http://localhost:5000/data')

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Extrae los datos del cuerpo de la respuesta JSON
                Data = response.json()
                # Almacena los datos en el objeto de almacenamiento
                self.data = Data
            else:
                print("Error al obtener los datos:", response.text)
        except Exception as e:
            print("Error al conectarse al servidor:", e)
    
    def get_data(self):
        return self.data