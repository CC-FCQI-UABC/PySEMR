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

# run.py
from csv_saver import save_data_to_csv
from patient_model import PatientModel
from domicilios_data import domiciliosData

# Initialize the domicilios data object
domicilios = domiciliosData()

# Create an instance of PatientModel with the domicilios data
patient_model = PatientModel(domicilios.get_data())

# Run the simulation
patient_model.run_simulation()

# Save the data of all patients to a CSV file named 'patient_data'
save_data_to_csv(patient_model.patients, 'patient_data')

# Save the data of patients with diseases to a CSV file named 'diseased_patients'
# The 'True' argument indicates that this data is filtered (diseased patients)
save_data_to_csv(patient_model.enfermos, 'diseased_patients', True)
