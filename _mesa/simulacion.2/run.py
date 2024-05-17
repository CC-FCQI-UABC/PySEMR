# run.py
from flask import Flask, render_template, request
from patient_model import PatientModel
from sql_generator import *
import pymysql
import os

# Define the Flask app with the correct static folder
app = Flask(__name__, static_folder='templates/static')

def execute_sql_script(sql_script_file):
    connection = pymysql.connect(host='148.231.130.238',
                                 port=3306,
                                 user='master',
                                 password='elkomba2',
                                 db='openemr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 connect_timeout=30)

    
    try:
        with connection.cursor() as cursor:
            with open(sql_script_file, 'r') as file:
                sql_script = file.read()

            cursor.execute(sql_script)
        
        connection.commit()
        print("Script SQL ejecutado correctamente")
    
    except Exception as e:
        print("Error al ejecutar el script SQL:", str(e))
    
    finally:
        # Cerrar la conexión
        connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    patient_model = PatientModel()
    patients, enfermos = patient_model.run_simulation()
    generate_sql_from_patients(patients)
    generate_insert_from_diseases(enfermos)
    return "Simulation completed successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)