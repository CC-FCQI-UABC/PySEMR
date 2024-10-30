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

# Función para leer el archivo CSV y procesar los nombres masculinos
def get_names_from_csv(file_path, idx):
    names = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Saltar la cabecera
        next(csv_reader)
        for row in csv_reader:
            # Obtener el nombre de la columna especificada
            name = row[idx]
            # Dividir el nombre si contiene dos cadenas
            split_names = name.split()
            # Procesar cada parte del nombre
            for part in split_names:
                # Convertir la primera letra a mayúscula y el resto a minúscula
                processed_name = part.capitalize() if len(part) == 1 else part[0].upper() + part[1:].lower()
                # Agregar el nombre procesado a la lista
                names.append(processed_name)
    return names

# Nombre del archivo CSV
csv_file_name = "Nombres_mas_populares_2021.csv"

# Ruta completa del archivo CSV
csv_file_path = os.path.join(os.path.dirname(__file__), csv_file_name)

# Obtener nombres masculinos del archivo CSV
male_names = get_names_from_csv(csv_file_path, 7)

female_names = get_names_from_csv(csv_file_path, 1)

# Nombre del archivo CSV de salida
output_csv_file_name = "male_names_processed.csv"

output_csv_file_name_2 = "female_names_processed.csv"

# Ruta completa del archivo CSV de salida
output_csv_file_path = os.path.join(os.path.dirname(__file__), output_csv_file_name)

output_csv_file_path_2 = os.path.join(os.path.dirname(__file__), output_csv_file_name_2)

# Escribir los nombres masculinos procesados en un nuevo archivo CSV
with open(output_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for name in male_names:
        csv_writer.writerow([name])

print("Se ha creado el archivo 'male_names_processed.csv' con los nombres masculinos procesados.")

# Escribir los nombres masculinos procesados en un nuevo archivo CSV
with open(output_csv_file_path_2, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for name in female_names:
        csv_writer.writerow([name])
        
print("Se ha creado el archivo 'female_names_processed.csv' con los nombres masculinos procesados.")