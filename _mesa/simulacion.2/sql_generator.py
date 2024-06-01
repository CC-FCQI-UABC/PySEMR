import os

def divide_list_into_chunks(lst, n):
    """Divide una lista en n partes aproximadamente iguales."""
    size = (len(lst) + n - 1) // n
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def generate_insert_from_diseases(enfermos):
    output_file = "/home/ec2-user/environment/PySEMR/_mesa/simulacion.2/patient_data/insert_into_diseases_list.sql"
    insert_into_sql = "INSERT INTO lists (type, title, pid, verification, list_option_id) VALUES\n"
    for enfermo in enfermos:
        for disease in enfermo.diseases_contracted:
            insert_into_sql += "('medical_problem', '{}', {}, 'confirmed', '{}'),\n".format(disease, enfermo.personal_data.pid, disease)
    # Eliminar la coma y el salto de línea finales innecesarios
    insert_into_sql = insert_into_sql.rstrip(",\n")
    with open(output_file, 'w', encoding='utf8') as output:
        output.write(insert_into_sql)
    

def generate_sql_from_patients(patients):
    # Script to create the table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS `mesapatient_data` (
      `id` bigint NOT NULL AUTO_INCREMENT,
      `uuid` binary(16) DEFAULT NULL,
      `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `language` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `financial` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `fname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `lname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `mname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `DOB` date DEFAULT NULL,
      `street` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `postal_code` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `city` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `state` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `country_code` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `drivers_license` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `ss` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `occupation` longtext COLLATE utf8mb4_general_ci,
      `phone_home` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `phone_biz` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `phone_contact` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `phone_cell` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `pharmacy_id` int NOT NULL DEFAULT '0',
      `status` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `contact_relationship` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `date` datetime DEFAULT NULL,
      `sex` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `referrer` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `referrerID` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `providerID` int DEFAULT NULL,
      `ref_providerID` int DEFAULT NULL,
      `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `email_direct` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `ethnoracial` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `race` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `ethnicity` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `religion` varchar(40) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `interpretter` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `migrantseasonal` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `family_size` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `monthly_income` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `billing_note` text COLLATE utf8mb4_general_ci,
      `homeless` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `financial_review` datetime DEFAULT NULL,
      `pubpid` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `pid` bigint NOT NULL DEFAULT '0',
      `genericname1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `genericval1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `genericname2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `genericval2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `hipaa_mail` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `hipaa_voice` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `hipaa_notice` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `hipaa_message` varchar(20) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `hipaa_allowsms` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'NO',
      `hipaa_allowemail` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'NO',
      `squad` varchar(32) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `fitness` int NOT NULL DEFAULT '0',
      `referral_source` varchar(30) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext4` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext5` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext6` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext7` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `usertext8` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist4` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist5` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist6` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `userlist7` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `pricelevel` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'standard',
      `regdate` datetime DEFAULT NULL COMMENT 'Registration Date',
      `contrastart` date DEFAULT NULL COMMENT 'Date contraceptives initially used',
      `completed_ad` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'NO',
      `ad_reviewed` date DEFAULT NULL,
      `vfc` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `mothersname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `guardiansname` text COLLATE utf8mb4_general_ci,
      `allow_imm_reg_use` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `allow_imm_info_share` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `allow_health_info_ex` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `allow_patient_portal` varchar(31) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `deceased_date` datetime DEFAULT NULL,
      `deceased_reason` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `soap_import_status` tinyint DEFAULT NULL COMMENT '1-Prescription Press 2-Prescription Import 3-Allergy Press 4-Allergy Import',
      `cmsportal_login` varchar(60) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `care_team_provider` text COLLATE utf8mb4_general_ci,
      `care_team_facility` text COLLATE utf8mb4_general_ci,
      `care_team_status` text COLLATE utf8mb4_general_ci,
      `county` varchar(40) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
      `industry` text COLLATE utf8mb4_general_ci,
      `imm_reg_status` text COLLATE utf8mb4_general_ci,
      `imm_reg_stat_effdate` text COLLATE utf8mb4_general_ci,
      `publicity_code` text COLLATE utf8mb4_general_ci,
      `publ_code_eff_date` text COLLATE utf8mb4_general_ci,
      `protect_indicator` text COLLATE utf8mb4_general_ci,
      `prot_indi_effdate` text COLLATE utf8mb4_general_ci,
      `guardianrelationship` text COLLATE utf8mb4_general_ci,
      `guardiansex` text COLLATE utf8mb4_general_ci,
      `guardianaddress` text COLLATE utf8mb4_general_ci,
      `guardiancity` text COLLATE utf8mb4_general_ci,
      `guardianstate` text COLLATE utf8mb4_general_ci,
      `guardianpostalcode` text COLLATE utf8mb4_general_ci,
      `guardiancountry` text COLLATE utf8mb4_general_ci,
      `guardianphone` text COLLATE utf8mb4_general_ci,
      `guardianworkphone` text COLLATE utf8mb4_general_ci,
      `guardianemail` text COLLATE utf8mb4_general_ci,
      `sexual_orientation` text COLLATE utf8mb4_general_ci,
      `gender_identity` text COLLATE utf8mb4_general_ci,
      `birth_fname` text COLLATE utf8mb4_general_ci,
      `birth_lname` text COLLATE utf8mb4_general_ci,
      `birth_mname` text COLLATE utf8mb4_general_ci,
      `dupscore` int NOT NULL DEFAULT '-9',
      `name_history` tinytext COLLATE utf8mb4_general_ci,
      `suffix` tinytext COLLATE utf8mb4_general_ci,
      `street_line_2` tinytext COLLATE utf8mb4_general_ci,
      `patient_groups` text COLLATE utf8mb4_general_ci,
      `prevent_portal_apps` text COLLATE utf8mb4_general_ci,
      `provider_since_date` tinytext COLLATE utf8mb4_general_ci,
      `created_by` bigint DEFAULT NULL COMMENT 'users.id the user that first created this record',
      `updated_by` bigint DEFAULT NULL COMMENT 'users.id the user that last modified this record',
      `preferred_name` tinytext COLLATE utf8mb4_general_ci,
      `nationality_country` tinytext COLLATE utf8mb4_general_ci,
      PRIMARY KEY (`id`),
      UNIQUE KEY `pid` (`pid`),
      UNIQUE KEY `uuid` (`uuid`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    
    ALTER TABLE mesapatient_data AUTO_INCREMENT = 0;
    """

    patients_chunks = divide_list_into_chunks(patients, 10)

    for i, chunk in enumerate(patients_chunks, start=1):
        output_file = f"/home/ec2-user/environment/PySEMR/_mesa/simulacion.2/patient_data/create_mesapatient_data_table_{i}.sql"
        if i == 1:
            delete_from_table = "DELETE FROM mesapatient data;"
            with open(output_file, 'w', encoding='utf8') as output:
                output.write(delete_from_table)
                output.write("\n\n")
        insert_into_sql = "INSERT INTO mesapatient_data (language, fname, mname, lname, DOB, street, postal_code, city, state, country_code, drivers_license, ss, occupation, phone_home, phone_biz, phone_contact, phone_cell, status, contact_relationship, date, sex, email, email_direct, ethnoracial, race, ethnicity, religion, family_size, monthly_income, homeless, pid, county, sexual_orientation, gender_identity, street_line_2, preferred_name, nationality_country) VALUES\n"
        for patient in chunk:
            data_row = [
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
            ]
            data_row = [f"'{val}'" if isinstance(val, str) else str(val) for val in data_row]
            insert_into_sql += "({}),\n".format(', '.join(data_row))
        insert_into_sql = insert_into_sql.rstrip(",\n")

        with open(output_file, 'w', encoding='utf8') as output:
            output.write(create_table_sql)
            output.write("\n\n")
            output.write(insert_into_sql + ";")