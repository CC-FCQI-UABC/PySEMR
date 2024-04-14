import requests

# URL de la ruta de la API
url = 'http://localhost:5000/data'

# Realizar la solicitud GET
response = requests.get(url)

# Verificar el código de estado de la respuesta
if response.status_code == 200:
    # Extraer los datos del cuerpo de la respuesta JSON
    data = response.json()
    print("Data obtenida exitosamente:", data)
    # Aquí puedes guardar la data en algún lugar, como una base de datos local o un archivo
else:
    print("Error al obtener los datos:", response.text)
