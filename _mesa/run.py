import csv
from user import UserModel
from patient_data import RegistroModel

# Crear instancia de UserModel
user_model = UserModel()

# Crear instancia de RegistroModel
registro_model = RegistroModel()

# Agregar usuarios aleatorios
for i in range(10):
    user_model.agregar_usuario_aleatorio()
    for j in range(10):
        registro_model.agregar_registro_aleatorio(user_model.users[i])


# Agregar registros médicos aleatorios

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

# Guardar datos de RegistroModel en un archivo CSV
with open(directory + 'registro_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for registro in registro_model.registros:
        csv_writer.writerow([
            registro.id, registro.uuid, registro.title, registro.language, registro.financial,
            registro.fname, registro.mname, registro.lname, registro.DOB, registro.street,
            registro.postal_code, registro.city, registro.state, registro.country_code,
            registro.drivers_license, registro.ss, registro.occupation, registro.phone_home,
            registro.phone_biz, registro.phone_contact, registro.phone_cell, registro.pharmacy_id,
            registro.status, registro.contact_relationship, registro.date, registro.sex
        ])
