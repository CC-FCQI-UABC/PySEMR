#run.py
from csv_saver import save_data_to_csv
from patient_model import PatientModel
from domicilios_data import domiciliosData

domicilios = domiciliosData()

patient_model = PatientModel(domicilios.get_data())

patient_model.run_simulation()

save_data_to_csv(patient_model.patients, 'patient_data')
save_data_to_csv(patient_model.enfermos, 'diseased_patients')