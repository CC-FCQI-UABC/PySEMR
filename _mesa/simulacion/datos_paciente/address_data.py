import random

class AddressData:
    def __init__(self, domicilios_data):
        idx = random.randint(0, len(domicilios_data) - 1)
        while domicilios_data['data'][idx]["NOMREF1"] == "N/A":
            idx = random.randint(0, len(domicilios_data) - 1)
        self.street = domicilios_data['data'][idx]["NOMREF1"]
        self.street_line_2 = domicilios_data['data'][idx]["NOMREF2"]
        self.postal_code = domicilios_data['data'][idx]["CP"]
        self.city = "Tijuana"
        self.state = "Baja California"
        self.country_code = "MEX"