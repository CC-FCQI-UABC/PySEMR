# run.py
import threading
from csv_saver import save_data_to_csv
from patient_model import PatientModel
from Dataset import Dataset
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize the domicilios data object
dataset = Dataset()

# Función para ejecutar la simulación en un hilo
def run_simulation_thread(parameters, response_holder):
    try:
        # Create an instance of PatientModel with the domicilios data
        patient_model = PatientModel(dataset.get_data())
        
        # Ejecuta la simulación con los parámetros
        patient_model.run_simulation(parameters)
        
        # Guarda los datos en archivos CSV
        save_data_to_csv(patient_model.patients, 'patient_data')
        save_data_to_csv(patient_model.enfermos, 'diseased_patients', True)

        # Prepara la respuesta
        response_data = {
            "message": "Simulation executed.",
            "days_simulated": parameters['dias'],
            "patients_generated": len(patient_model.patients),
            "image_path": "seasonal_patient_counts.png",
            "patient_data": [patient.to_dict() for patient in patient_model.patients],
        }

        response_holder["response"] = response_data
        response_holder["status"] = 200
    except Exception as e:
        response_holder["response"] = {"error": str(e)}
        response_holder["status"] = 500

@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    parameters = request.get_json()
    print(parameters)

    # Usar un diccionario para almacenar la respuesta desde el hilo
    response_holder = {}
    simulation_thread = threading.Thread(target=run_simulation_thread, args=(parameters, response_holder))
    simulation_thread.start()
    simulation_thread.join()  # Esto es opcional. Sin esto, el endpoint responde inmediatamente.

    # Devuelve la respuesta almacenada por el hilo
    return jsonify(response_holder.get("response", {})), response_holder.get("status", 500)

    
@app.route('/download_files', methods=['GET'])
def download_files(option):
    if(option):
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)