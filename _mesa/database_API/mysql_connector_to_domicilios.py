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

from flask import Flask, jsonify
from sqlalchemy import create_engine, text

# Initialize the Flask application
app = Flask(__name__)

DB_USER = 'openemr'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'emr_datasets'
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DB_URI)

def query_to_dict_list(results, dataset_list):
    columns = list(results.keys())
    for row in results:
        data_dict = {}
        for i in range(len(row)):
            data_dict[columns[i]] = row[i]
        dataset_list.append(data_dict)   

@app.route('/data')
def obtener_data():
    try:
        with engine.connect() as connection:
            
            query_address = text('SELECT * FROM address limit 50000;')
            query_female_names = text('SELECT * FROM female_names;')
            query_male_names = text('SELECT * FROM male_names;')
            query_last_names = text('SELECT * FROM apellidos;')

            address_results = connection.execute(query_address)
            female_names_results = connection.execute(query_female_names)
            male_names_results = connection.execute(query_male_names)
            last_names_results = connection.execute(query_last_names)

            data = {
                "Address": [],
                "FemaleNames": [],
                "MaleNames": [],
                "LastNames": []
            }

            query_to_dict_list(address_results, data["Address"])
            query_to_dict_list(female_names_results, data["FemaleNames"])
            query_to_dict_list(male_names_results, data["MaleNames"])
            query_to_dict_list(last_names_results, data["LastNames"])

            return jsonify({"status": "success", "data": data})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
