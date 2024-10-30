# run.py
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


@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    try:
        # Create an instance of PatientModel with the domicilios data
        patient_model = PatientModel(dataset.get_data())
        
        parameters = request.get_json()
        print(parameters)
        
        # Ejecuta la simulación con los parámetros
        patient_model.run_simulation(parameters)
        
        # Guarda los datos en archivos CSV
        save_data_to_csv(patient_model.patients, 'patient_data')
        save_data_to_csv(patient_model.enfermos, 'diseased_patients', True)

        # Prepara la respuesta
        response_data = {
            "message": "Simulation executed.",
            "days_simulated": 365,
            "patients_generated": len(patient_model.patients),
            "image_path": "seasonal_patient_counts.png"
        }

        # Devuelve la respuesta en formato JSON
        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error: {e}")  # Para depuración
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
