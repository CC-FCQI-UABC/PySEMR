######################################################################
## PythonSyntheticElectronicMedicalRecords 1.0
## Modelo computacional de registros medicos electrónicos sintéticos 
## en Python.
######################################################################
## This software are distributed using the Creative Commons Public
## License "Attribution-NonCommercial-ShareAlike 4.0 International"
## https://creativecommons.org/licenses/by-nc-sa/4.0/
######################################################################
## Author: Manuel Castañón Puga, Claudio Emiliano Palacio Martínez, 
## Ricardo Fernando Rosales Cisneros, Carelia Guadalupe Gaxiola
## Pacheco, Luis Enrique Palafox Maestre.
## Copyright: Copyright 2024, Universidad Autónoma de Baja California.
######################################################################
## Credits: matplotlib, mesa, Flask, SQLAlchemy, Faker, requests, 
## tqdm, pandas and click libraries.
## License: CC BY-NC-SA 4.0
## Version: 1.0.0
## Mmaintainer: https://github.com/pugapuga.
## Email: puga@uabc.edu.mx
## Status: Released.
######################################################################

from flask import Flask, jsonify
from sqlalchemy import create_engine, text
import sqlalchemy.exc

# Initialize the Flask application
app = Flask(__name__)

DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'openemr'
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URI)

@app.route('/data')
def obtener_data():
    try:
        
        with engine.connect() as connection:
            
            query = text('''SELECT 
    HEX(uuid) as uuid_hex, 
    title, 
    language, 
    financial, 
    fname, 
    lname, 
    mname, 
    DOB, 
    street, 
    postal_code, 
    city, 
    state, 
    country_code, 
    drivers_license, 
    ss, 
    occupation, 
    phone_home, 
    phone_biz, 
    phone_contact, 
    phone_cell, 
    pharmacy_id, 
    status, 
    contact_relationship, 
    date, 
    sex, 
    referrer, 
    referrerID, 
    providerID, 
    ref_providerID, 
    email, 
    email_direct, 
    ethnoracial, 
    race, 
    ethnicity, 
    religion, 
    interpretter, 
    migrantseasonal, 
    family_size, 
    monthly_income, 
    billing_note, 
    homeless, 
    financial_review, 
    pubpid, 
    pid, 
    genericname1, 
    genericval1, 
    genericname2, 
    genericval2, 
    hipaa_mail, 
    hipaa_voice, 
    hipaa_notice, 
    hipaa_message, 
    hipaa_allowsms, 
    hipaa_allowemail, 
    squad, 
    fitness, 
    referral_source, 
    usertext1, 
    usertext2, 
    usertext3, 
    usertext4, 
    usertext5, 
    usertext6, 
    usertext7, 
    usertext8, 
    userlist1, 
    userlist2, 
    userlist3, 
    userlist4, 
    userlist5, 
    userlist6, 
    userlist7, 
    pricelevel, 
    regdate, 
    contrastart, 
    completed_ad, 
    ad_reviewed, 
    vfc, 
    mothersname, 
    guardiansname, 
    allow_imm_reg_use, 
    allow_imm_info_share, 
    allow_health_info_ex, 
    allow_patient_portal, 
    deceased_date, 
    deceased_reason, 
    soap_import_status, 
    cmsportal_login, 
    care_team_provider, 
    care_team_facility, 
    care_team_status, 
    county, 
    industry, 
    imm_reg_status, 
    imm_reg_stat_effdate, 
    publicity_code, 
    publ_code_eff_date, 
    protect_indicator, 
    prot_indi_effdate, 
    guardianrelationship, 
    guardiansex, 
    guardianaddress, 
    guardiancity, 
    guardianstate, 
    guardianpostalcode, 
    guardiancountry, 
    guardianphone, 
    guardianworkphone, 
    guardianemail, 
    sexual_orientation, 
    gender_identity, 
    birth_fname, 
    birth_lname, 
    birth_mname, 
    dupscore, 
    name_history, 
    suffix, 
    street_line_2, 
    patient_groups, 
    prevent_portal_apps, 
    provider_since_date, 
    created_by, 
    updated_by, 
    preferred_name, 
    nationality_country
FROM 
    patient_data 
    limit 50
;
''')

            resultados = connection.execute(query)
            
            data = []
            column_names = list(resultados.keys())
            for row in resultados:
                data_dict = {}
                for i in range(len(row)):
                    data_dict[column_names[i]] = row[i]
                data.append(data_dict)

            return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
