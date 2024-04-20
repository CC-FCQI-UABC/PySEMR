from mesa import Agent, Model
from mesa.time import RandomActivation
import user
import datetime
import uuid
import domicilios_data
import hashlib
from funciones import randomizer, numeroTelefono, googleSigninMail, callesBC, licenciaConducir

import random
from faker import Faker
from funciones import randomizer, numeroTelefono

fake = Faker('es_MX')

class PatientData(Agent):
    def __init__(self, model, domicilios_data, pid):
        super().__init__(self, model)
        self.language = "Español"
        self.fname = "" #Llenada al final
        self.lname = fake.last_name() + " " + fake.last_name()
        self.mname = "" #Llenada al final
        self.DOB = fake.date_of_birth(minimum_age  = 20, maximum_age = 80)
        # REEMPLAZAR CON DATA DE DOMICILIOS
        idx = random.randint(0, domicilios_data.length)
        while(domicilios_data.data['data'][idx]["NOMREF1"]=="N/A"):
            idx += 1
        self.street = self.street = domicilios_data.data['data'][idx]["NOMREF1"]
        self.postal_code = domicilios_data.data['data'][idx]["CP"]
        # REEMPLAZAR CON DATA DE DOMICILIOS
        self.city = "Tijuana"
        self.state = "Baja California"
        self.country_code = "52"
        self.drivers_license = licenciaConducir.licencia()
        self.ss = fake.ssn()
        self.occupation = fake.job()
        self.phone_home = numeroTelefono.numeroTelefono(7, random.choices(["Tijuana", "Ensenada", "Mexicali", "Playas de Rosarito", "Tecate", "San Quintín", "Valle de Las Palmas", "San Felipe"],
                                                                            [60, 5, 10, 5, 5, 5, 5, 5])[0])
        self.phone_biz = numeroTelefono.numeroTelefono(7, self.city)
        self.phone_contact = numeroTelefono.numeroTelefono(7, self.city)
        self.phone_cell = numeroTelefono.numeroTelefono(7, self.city)
        # self.pharmacy_id = ""
        self.status = randomizer.randomize('estadoCivil.txt')
        self.contact_relationship = ""
        self.date = fake.date_between(datetime.date(2000, 1, 1))
        self.sex = random.choice(["masculino", "femenino", "prefiero no decirlo"])
        #omitidos
        # self.referrer = ""
        # self.referrerID = ""
        # self.providerID = None
        # self.ref_providerID = None
        self.email = fake.free_email()
        self.email_direct = self.email
        self.ethnoracial = random.choices(["Caucásica/o", "Mestiza/o", "Indígena", "Afrodescendiente"], [20,65,10,5])[0] #Aproximados
        self.race = self.ethnoracial
        self.ethnicity = self.race
        self.religion = random.choices(["Católica", "Protestante/Cristiano evangélico", "Otras religiones", "Sin adscripción religiosa (creyente)", "Sin religión"],[62, 16.4, 0.2, 2, 19])[0]
        # omitidos
        #   `interpretter` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `migrantseasonal` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        self.family_size = random.choices(["Tres", "Cuatro", "Cingo"], [42, 53, 5])[0]
        self.monthly_income = "29637" #Promedio obtenido
        #omitido `billing_note` text COLLATE utf8mb4_general_ci,
        self.homeless = random.choices(["Falso", "Verdadero"], [99.99, 0.01])[0]
        #omitidos
        #   `financial_review` datetime DEFAULT NULL,
        #   `pubpid` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `pid` bigint NOT NULL DEFAULT '0',
        self.pid = pid
        #   `genericname1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `genericval1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `genericname2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `genericval2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `hipaa_mail` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `hipaa_voice` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `hipaa_notice` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `hipaa_message` varchar(20) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `hipaa_allowsms` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'NO',
        #   `hipaa_allowemail` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'NO',
        #   `squad` varchar(32) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `fitness` int NOT NULL DEFAULT '0',
        #   `referral_source` varchar(30) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext4` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext5` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext6` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext7` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `usertext8` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist4` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist5` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist6` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `userlist7` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `pricelevel` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'standard',
        #   `regdate` datetime DEFAULT NULL COMMENT 'Registration Date',
        #   `contrastart` date DEFAULT NULL COMMENT 'Date contraceptives initially used',
        #   `completed_ad` varchar(3) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'NO',
        #   `ad_reviewed` date DEFAULT NULL,
        #   `vfc` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `mothersname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `guardiansname` text COLLATE utf8mb4_general_ci,
        #   `allow_imm_reg_use` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `allow_imm_info_share` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `allow_health_info_ex` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `allow_patient_portal` varchar(31) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `deceased_date` datetime DEFAULT NULL,
        #   `deceased_reason` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `soap_import_status` tinyint DEFAULT NULL COMMENT '1-Prescription Press 2-Prescription Import 3-Allergy Press 4-Allergy Import',
        #   `cmsportal_login` varchar(60) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        #   `care_team_provider` text COLLATE utf8mb4_general_ci,
        #   `care_team_facility` text COLLATE utf8mb4_general_ci,
        #   `care_team_status` text COLLATE utf8mb4_general_ci,
        #   `county` varchar(40) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
        self.county = "Tijuana"
        #omitidos
        #   `industry` text COLLATE utf8mb4_general_ci,
        #   `imm_reg_status` text COLLATE utf8mb4_general_ci,
        #   `imm_reg_stat_effdate` text COLLATE utf8mb4_general_ci,
        #   `publicity_code` text COLLATE utf8mb4_general_ci,
        #   `publ_code_eff_date` text COLLATE utf8mb4_general_ci,
        #   `protect_indicator` text COLLATE utf8mb4_general_ci,
        #   `prot_indi_effdate` text COLLATE utf8mb4_general_ci,
        #   `guardianrelationship` text COLLATE utf8mb4_general_ci,
        #   `guardiansex` text COLLATE utf8mb4_general_ci,
        #   `guardianaddress` text COLLATE utf8mb4_general_ci,
        #   `guardiancity` text COLLATE utf8mb4_general_ci,
        #   `guardianstate` text COLLATE utf8mb4_general_ci,
        #   `guardianpostalcode` text COLLATE utf8mb4_general_ci,
        #   `guardiancountry` text COLLATE utf8mb4_general_ci,
        #   `guardianphone` text COLLATE utf8mb4_general_ci,
        #   `guardianworkphone` text COLLATE utf8mb4_general_ci,
        #   `guardianemail` text COLLATE utf8mb4_general_ci,
        self.sexual_orientation = random.choices(["Heterosexual", "Bisexual", "Homosexualidad", "Otra"], [95.2, 2.4816, 1.7808, 0.5376])[0] 
        self.gender_identity = random.choices(["Cisgénero", "Transgénero", "Otra"], [99.1, 0.3132, 0.5868])[0]
        #omitidos
        #   `birth_fname` text COLLATE utf8mb4_general_ci,
        #   `birth_lname` text COLLATE utf8mb4_general_ci,
        #   `birth_mname` text COLLATE utf8mb4_general_ci,
        #   `dupscore` int NOT NULL DEFAULT '-9',
        #   `name_history` tinytext COLLATE utf8mb4_general_ci,
        #   `suffix` tinytext COLLATE utf8mb4_general_ci,
        self.street_line_2 = domicilios_data.data['data'][idx]["NOMREF2"]
        #   `patient_groups` text COLLATE utf8mb4_general_ci,
        #   `prevent_portal_apps` text COLLATE utf8mb4_general_ci,
        #   `provider_since_date` tinytext COLLATE utf8mb4_general_ci,
        #   `created_by` bigint DEFAULT NULL COMMENT 'users.id the user that first created this record',
        #   `updated_by` bigint DEFAULT NULL COMMENT 'users.id the user that last modified this record',
        #   `preferred_name` tinytext COLLATE utf8mb4_general_ci,
        self.preferred_name = ""
        self.nationality_country = "México"
        
        if self.sex == "masculino":
            self.fname = fake.first_name_male()
            self.mname = fake.first_name_male()
            self.preferred_name = random.choice([self.fname, self.mname])
        elif self.sex == "femenino":
            self.fname = fake.first_name_female()
            self.mname = fake.first_name_female()
            self.preferred_name = random.choice([self.fname, self.mname])
        
    def step(self):
        pass

class PatientModel(Model):
    def __init__(self):
        super().__init__()
        self.patients = []
        
    def agregar_patient_aleatorio(self, domicilios_data):
        patient = PatientData(self, domicilios_data, len(self.patients))
        self.patients.append(patient)