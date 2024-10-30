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

import csv
import os

# Function to save patient data to a CSV file
def save_data_to_csv(patients, file_name, show_sick_status: bool = False):
    # Define the directory where the file will be saved
    directory = "PySEMR/_mesa/simulacion/patient_data"
    os.makedirs(directory, exist_ok=True)

    # Open the CSV file for writing
    with open(os.path.join(directory, file_name + '.csv'), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Create the header row for the CSV file
        header_row = [
            "language", "fname", "mname", "lname",
            "DOB", "street", "postal_code", "city", "state", "country_code", "drivers_license",
            "ss", "occupation", "phone_home", "phone_biz", "phone_contact", "phone_cell",
            "status", "contact_relationship", "date", "sex", "email", "email_direct",
            "ethnoracial", "race", "ethnicity", "religion", "family_size", "monthly_income",
            "homeless", "pid", "county", "sexual_orientation", "gender_identity",
            "street_line_2", "preferred_name", "nationality_country"
        ]

        # If the sick status should be included, add the column
        if show_sick_status:
            header_row.append("sick_status")
            csv_writer.writerow(header_row)

            # Write the data rows with sick status
            for patient in patients:
                data_row = [
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
                ]

                # Add sick status to the row
                data_row.append(patient.sick_status)
                csv_writer.writerow(data_row)

        else:
            # Write the header row
            csv_writer.writerow(header_row)

            # Write the data rows without sick status
            for patient in patients:
                data_row = [
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
                ]
                csv_writer.writerow(data_row)
