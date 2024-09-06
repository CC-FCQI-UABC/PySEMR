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

# Function to read a CSV file and process names from a specified column
def get_names_from_csv(file_path, idx):
    names = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip the header row
        next(csv_reader)
        for row in csv_reader:
            # Get the name from the specified column index
            name = row[idx]
            # Split the name if it contains multiple parts
            split_names = name.split()
            # Process each part of the name
            for part in split_names:
                # Capitalize the first letter and make the rest lowercase
                processed_name = part.capitalize() if len(part) == 1 else part[0].upper() + part[1:].lower()
                # Add the processed name to the list
                names.append(processed_name)
    return names

# Name of the input CSV file
csv_file_name = "Nombres_mas_populares_2021.csv"

# Full path to the input CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), csv_file_name)

# Get male names from the specified column (index 7) in the input CSV file
male_names = get_names_from_csv(csv_file_path, 7)

# Get female names from the specified column (index 1) in the input CSV file
female_names = get_names_from_csv(csv_file_path, 1)

# Name of the output CSV file for processed male names
output_csv_file_name = "male_names_processed.csv"

# Name of the output CSV file for processed female names
output_csv_file_name_2 = "female_names_processed.csv"

# Full path to the output CSV file for processed male names
output_csv_file_path = os.path.join(os.path.dirname(__file__), output_csv_file_name)

# Full path to the output CSV file for processed female names
output_csv_file_path_2 = os.path.join(os.path.dirname(__file__), output_csv_file_name_2)

# Write the processed male names to a new CSV file
with open(output_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for name in male_names:
        csv_writer.writerow([name])

print("The file 'male_names_processed.csv' has been created with the processed male names.")

# Write the processed female names to a new CSV file
with open(output_csv_file_path_2, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for name in female_names:
        csv_writer.writerow([name])
        
print("The file 'female_names_processed.csv' has been created with the processed female names.")
