import csv
import sys
import os

from patient_model import PatientModel
from domicilios_data import domiciliosData
from ambiente import Environment
from enfermedad import Enfermedad
import time


# Crear instancia de UserModel
user_model = UserModel()

# Crear instancia de patientModel
patient_model = PatientModel()

environment = Environment()

# Creamos instancia de domicilios_data
domicilios = domiciliosData()

domicilios.get_data()
counter = 0

# Define una lista de posibles enfermedades
possible_diseases = [
    Enfermedad("Gripe", 0.2, ["Invierno", "Otoño"]),
    Enfermedad("Resfriado", 0.15, ["Invierno", "Primavera"]),
    Enfermedad("COVID-19", 0.1, ["Invierno", "Primavera", "Verano", "Otoño"]),
    # Agrega más enfermedades según sea necesario
]


# Agregar usuarios aleatorios
for day in range(365):  # Simular un año
    print(f"Día {day + 1}")

    # Simular cambios estacionales y de tráfico
    environment.simulate_season_change()
    environment.simulate_traffic()

    # Generar pacientes aleatorios para este día
    for _ in range(137):  # Por ejemplo, generar 100 pacientes nuevos al día
        patient_model.agregar_patient_aleatorio(domicilios)

    # Llamar al método step() de cada paciente para simular su comportamiento
    for patient in patient_model.patients:
        patient.step(environment, possible_diseases)

# Specify directory for CSV files
directory = "_mesa"

# Guardar datos de patientModel en un archivo CSV
with open(directory + 'patient_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Escribir los nombres de los atributos como la primera fila
    csv_writer.writerow([
        "language", "fname", "mname", "lname",
        "DOB", "street", "postal_code", "city", "state", "country_code", "drivers_license",
        "ss", "occupation", "phone_home", "phone_biz", "phone_contact", "phone_cell",
        "status", "contact_relationship", "date", "sex", "email", "email_direct", 
        "ethnoracial", "race", "ethnicity", "religion", "family_size", "monthly_income", 
        "homeless", "pid", "county", "sexual_orientation", "gender_identity",
        "street_line_2", "preferred_name", "nationality_country"
    ])

    # Escribir los datos de los pacientes
    for patient in patient_model.patients:
        csv_writer.writerow([
            patient.personal_data.language, 
            patient.name_data.fname, patient.name_data.mname, patient.name_data.lname, patient.personal_data.DOB, 
            patient.address_data.street, patient.address_data.postal_code, patient.address_data.city, patient.address_data.state, 
            patient.address_data.country_code, patient.personal_data.drivers_license, patient.personal_data.ss, patient.personal_data.occupation, 
            patient.contact_data.phone_home, patient.contact_data.phone_biz, patient.contact_data.phone_contact, patient.contact_data.phone_cell,
            patient.personal_data.status, patient.personal_data.contact_relationship, patient.personal_data.date, patient.personal_data.sex, 
            patient.contact_data.email, patient.contact_data.email_direct, patient.personal_data.ethnoracial, patient.personal_data.race, patient.personal_data.ethnicity, 
            patient.personal_data.religion, patient.personal_data.family_size, patient.personal_data.monthly_income, patient.personal_data.homeless, patient.personal_data.pid, 
            patient.personal_data.county, patient.personal_data.sexual_orientation, patient.personal_data.gender_identity, patient.address_data.street_line_2, 
            patient.name_data.preferred_name, patient.personal_data.nationality_country
        ])