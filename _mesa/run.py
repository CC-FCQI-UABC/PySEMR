import csv
from user import UserModel
from patient_data import PatientModel
from domicilios_data import domiciliosData

# Crear instancia de UserModel
user_model = UserModel()

# Crear instancia de patientModel
patient_model = PatientModel()

# Creamos instancia de domicilios_data
domicilios = domiciliosData()

domicilios.get_data()
counter = 0
# Agregar usuarios aleatorios
for i in range(50000):
    counter += 1
    if counter % 100 == 0:
        print(f"Se han agregado {counter} pacientes.")
    patient_model.agregar_patient_aleatorio(domicilios)

# Agregar patients médicos aleatorios

# Specify directory for CSV files
directory = "_mesa"

# Guardar datos de patientModel en un archivo CSV
with open(directory + 'patient_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Escribir los nombres de los atributos como la primera fila
    csv_writer.writerow([
        "language", "fname", "mname", "lname",
        "DOB", "street", "postal_code", "city", "state", "country_code", "drivers_license",
        "ss", "occupation", "phone_home", "phone_biz", "phone_contact", "phone_cell",
        "status", "contact_relationship", "date", "sex", "email", "email_direct", 
        "ethnoracial", "race", "ethnicity", "religion", "family_size", "monthly_income", 
        "homeless", "pid", "county", "sexual_orientation", "gender_identity",
        "street_line_2", "preferred_name", "nationality_country"
    ])

    # Escribir los datos de los pacientes
    for patient in patient_model.patients:
        csv_writer.writerow([
            patient.language, 
            patient.fname, patient.mname, patient.lname, patient.DOB, patient.street,
            patient.postal_code, patient.city, patient.state, patient.country_code,
            patient.drivers_license, patient.ss, patient.occupation, patient.phone_home,
            patient.phone_biz, patient.phone_contact, patient.phone_cell,
            patient.status, patient.contact_relationship, patient.date, patient.sex, patient.email, 
            patient.email_direct, patient.ethnoracial, patient.race, patient.ethnicity, patient.religion, 
            patient.family_size, patient.monthly_income, patient.homeless, patient.pid, patient.county, 
            patient.sexual_orientation, patient.gender_identity, patient.street_line_2, patient.preferred_name, patient.nationality_country
        ])
