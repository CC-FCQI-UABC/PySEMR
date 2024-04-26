import requests

class domiciliosData:
    def __init__(self):
        self.data = None
        self.length = 0
    
    def get_data(self):
        try:
            # Realiza una solicitud GET al servidor Flask para obtener los datos
            response = requests.get('http://localhost:5000/data')

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Extrae los datos del cuerpo de la respuesta JSON
                Data = response.json()
                # Almacena los datos en el objeto de almacenamiento
                self.data = Data
                self.length = len(Data)
            else:
                print("Error al obtener los datos:", response.text)
        except Exception as e:
            print("Error al conectarse al servidor:", e)