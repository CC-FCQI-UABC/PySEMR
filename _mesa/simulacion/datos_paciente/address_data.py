import random

class AddressData:
    def __init__(self, domicilios_data):
        idx = random.randint(0, len(domicilios_data) - 1)
        while domicilios_data['data'][idx]["NOMREF1"] == "N/A":
            idx = random.randint(0, len(domicilios_data) - 1)
        # TIPOVIAL + NOMVIAL + NUMEXT 
        self.street = domicilios_data['data'][idx]["TIPOVIAL"] + domicilios_data['data'][idx]["NOMVIAL"] + domicilios_data['data'][idx]["NUMEXT"] 
        self.street_line_2 = domicilios_data['data'][idx]["TIPOASEN"] + domicilios_data['data'][idx]["NOMASEN"]
        # TIPOASEN,NOMASEN
        self.postal_code = domicilios_data['data'][idx]["CP"]
        self.city = "Tijuana"
        self.state = "Baja California"
        self.country_code = "MEX"