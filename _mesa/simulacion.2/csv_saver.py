import csv
import os

def save_data_to_csv(patients):
    directory = "_mesa"
    # Asegúrate de que el directorio existe
    os.makedirs(directory, exist_ok=True)

    # Guardar datos de patientModel en un archivo CSV
    with open(os.path.join(directory, 'patient_data.csv'), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            "language", "fname", "mname", "lname",
            "DOB", "street", "postal_code", "city", "state", "country_code", "drivers_license",
            "ss", "occupation", "phone_home", "phone_biz", "phone_contact", "phone_cell",
            "status", "contact_relationship", "date", "sex", "email", "email_direct",
            "ethnoracial", "race", "ethnicity", "religion", "family_size", "monthly_income",
            "homeless", "pid", "county", "sexual_orientation", "gender_identity",
            "street_line_2", "preferred_name", "nationality_country"
        ])
        for patient in patients:
            csv_writer.writerow([
                patient.personal_data.language,
                patient.name_data.fname, patient.name_data.mname, patient.name_data.lname, patient.personal_data.DOB,
                patient.address_data.street, patient.address_data.postal_code, patient.address_data.city, patient.address_data.state,
                patient.address_data.country_code, patient.personal_data.drivers_license, patient.personal_data.ss, patient.personal_data.occupation,
                patient.contact_data.phone_home, patient.contact_data.phone_biz, patient.contact_data.phone_contact, patient.contact_data.phone_cell,
                patient.personal_data.status, patient.personal_data.contact_relationship, patient.personal_data.date, patient.personal_data.sex,
                patient.contact_data.email, patient.contact_data.email_direct, patient.personal_data.ethnoracial, patient.personal_data.race, patient.personal_data.ethnicity,
                patient.personal_data.religion, patient.personal_data.family_size, patient.personal_data.monthly_income, patient.personal_data.homeless, patient.personal_data.pid,
                patient.personal_data.county, patient.personal_data.sexual_orientation, patient.personal_data.gender_identity, patient.address_data.street_line_2,
                patient.name_data.preferred_name, patient.personal_data.nationality_country
            ])