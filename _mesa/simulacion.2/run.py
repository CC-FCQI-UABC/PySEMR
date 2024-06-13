# run.py
from flask import Flask, render_template, request
from patient_model import PatientModel
from sql_generator import *
import pymysql
import os

# Define the Flask app with the correct static folder
app = Flask(__name__, static_folder='templates/static')

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
    app.run(host='0.0.0.0', port=8081, debug=True)