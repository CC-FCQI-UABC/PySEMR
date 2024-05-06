import random

class AddressData:
    def __init__(self, pacientes_data, pid):
        self.street = pacientes_data['data'][pid]["street"]
        self.street_line_2 = pacientes_data['data'][pid]["street_line_2"]
        self.postal_code = pacientes_data['data'][pid]["postal_code"]
        self.city = "Tijuana"
        self.state = "Baja California"
        self.country_code = "MEX"