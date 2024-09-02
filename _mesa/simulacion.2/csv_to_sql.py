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

import csv
import os

def remove_bom(s):
    return s.replace('\ufeff', '')

def csv_to_mysql(csv_file, table_name, output_file):
    # Creación de la tabla
    create_table_sql = """
    
CREATE TABLE IF NOT EXISTS `mesapatient_data` (
  `id` bigint NOT NULL,
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
  `nationality_country` tinytext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `mesapatient_data`
--
ALTER TABLE `mesapatient_data`
  ADD UNIQUE KEY `pid` (`pid`),
  ADD UNIQUE KEY `uuid` (`uuid`),
  ADD KEY `id` (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--
DELIMITER //
CREATE TRIGGER `generate_uuid` BEFORE INSERT ON `mesapatient_data`
FOR EACH ROW
BEGIN
    SET NEW.uuid = UNHEX(REPLACE(UUID(), '-', ''));
END;
//
DELIMITER ;


--
-- AUTO_INCREMENT de la tabla `mesapatient_data`
--
ALTER TABLE `mesapatient_data`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;
COMMIT;
"""
    directory = "/PySEMR/_mesa/simulacion.2/patient_data/patient_data.csv"
    
    with open(output_file, 'w', encoding='utf8') as output:
        output.write(create_table_sql)
        
    delete_from_table_sql = f"DELETE FROM {table_name};"

        
    with open(output_file, 'a', encoding='utf8') as output:
        output.write("\n\n" + delete_from_table_sql)

    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        columns = next(reader)

    columns = [remove_bom(column) for column in columns]

    insert_into_sql = f"INSERT INTO {table_name} (`" + "`, `".join(columns) + "`) VALUES\n"
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        rows = []
        for row in reader:
            row_values = []
            for column, value in zip(columns, row):
                value = value.replace("'", "''")
                row_values.append(f"'{value}'")
            row_str = ', '.join(row_values)
            rows.append(f"({row_str})")
        insert_into_sql += ",\n".join(rows) + ";"

    with open(output_file, 'a', encoding='utf8') as output:
            output.write("\n\n" + insert_into_sql)
            
    return create_table_sql + "\n\n" + delete_from_table_sql + "\n\n" + insert_into_sql
    