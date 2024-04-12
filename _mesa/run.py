import csv
from user import UserModel
from patient_data import PatientModel

# Crear instancia de UserModel
user_model = UserModel()

# Crear instancia de patientModel
patient_model = PatientModel()

# Agregar usuarios aleatorios
for i in range(10):
    user_model.agregar_usuario_aleatorio()
    for j in range(10):
        patient_model.agregar_patient_aleatorio(user_model.users[i])


# Agregar patients médicos aleatorios

# Specify directory for CSV files
directory = "_mesa"

# Guardar datos de UserModel en un archivo CSV
with open(directory + 'user_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for usuario in user_model.users:
        csv_writer.writerow([usuario.id,
            usuario.uuid, usuario.username, usuario.password, usuario.authorized, usuario.info,
            usuario.source, usuario.fname, usuario.mname, usuario.lname, usuario.suffix,
            usuario.federaltaxid, usuario.federaldrugid, usuario.upin, usuario.facility,
            usuario.facility_id, usuario.see_auth, usuario.active, usuario.npi, usuario.title,
            usuario.specialty, usuario.billname, usuario.email, usuario.email_direct,
            usuario.google_signin_email, usuario.url, usuario.assistant, usuario.organization,
            usuario.valedictory, usuario.street, usuario.streetb, usuario.city, usuario.state,
            usuario.zip, usuario.street2, usuario.streetb2, usuario.city2, usuario.state2,
            usuario.zip2, usuario.phone, usuario.fax, usuario.phonew1, usuario.phonew2,
            usuario.phonecell, usuario.notes, usuario.cal_ui, usuario.taxonomy, usuario.calendar,
            usuario.abook_type, usuario.default_warehouse, usuario.irnpool, usuario.state_license_number,
            usuario.weno_prov_id, usuario.newcrop_user_role, usuario.cpoe, usuario.physician_type,
            usuario.main_menu_role, usuario.patient_menu_role, usuario.portal_user, usuario.supervisor_id,
            usuario.billing_facility, usuario.billing_facility_id
        ])

# Guardar datos de patientModel en un archivo CSV
with open(directory + 'patient_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for patient in patient_model.patients:
        csv_writer.writerow([
            patient.id, patient.uuid, patient.title, patient.language, patient.financial,
            patient.fname, patient.mname, patient.lname, patient.DOB, patient.street,
            patient.postal_code, patient.city, patient.state, patient.country_code,
            patient.drivers_license, patient.ss, patient.occupation, patient.phone_home,
            patient.phone_biz, patient.phone_contact, patient.phone_cell, patient.pharmacy_id,
            patient.status, patient.contact_relationship, patient.date, patient.sex
        ])
