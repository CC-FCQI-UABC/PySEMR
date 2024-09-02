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

DB_USER = 'master'
DB_PASSWORD = 'elkomba2'
DB_HOST = 'database-1.cpgwsuckign8.us-east-2.rds.amazonaws.com'
DB_NAME = 'domicilios_tijuana'
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DB_URI)

@app.route('/data')
def obtener_data():
    try:
        
        with engine.connect() as connection:
            
            query = text('SELECT * FROM domicilios')

            resultados = connection.execute(query)
            
            data = []
            column_names = list(resultados.keys())
            for row in resultados:
                data_dict = {}
                for i in range(len(row)):
                    data_dict[column_names[i]] = row[i]
                data.append(data_dict)

            return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
