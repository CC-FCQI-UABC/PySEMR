# run.py
from flask import Flask, render_template, request
from patient_model import PatientModel
from csv_saver import save_data_to_csv
import os

# Define the Flask app with the correct static folder
app = Flask(__name__, static_folder='templates/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    patient_model = PatientModel()
    patients = patient_model.run_simulation()
    save_data_to_csv(patients, 'patient_data')
    save_data_to_csv(patient_model.enfermos, 'diseased_patients', True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)