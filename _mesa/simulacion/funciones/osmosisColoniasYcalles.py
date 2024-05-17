import osmnx as ox
import json

north, south, east, west = 32.5452, 32.3746, -116.8326, -117.1007

# Obtener geometrías de colonias en Tijuana
colonias_tijuana = ox.geometries_from_bbox(north, south, east, west, tags={'place': True})

colonias_data = {}
for index, colonia in colonias_tijuana.iterrows():
    nombre_colonia = colonia['name']

    # Verificar si nombre_colonia es una cadena de texto válida
    if isinstance(nombre_colonia, str) and "United States" not in nombre_colonia and "California" not in nombre_colonia and "San Diego" not in nombre_colonia and "County" not in nombre_colonia:
        if nombre_colonia not in colonias_data:
            colonias_data[nombre_colonia] = []

        # Verificar si la geometría de la colonia es un polígono
        if colonia['geometry'].geom_type == 'Polygon':
            # Obtener las coordenadas de las calles de la colonia
            calles_colonia = list(colonia['geometry'].exterior.coords)
            colonias_data[nombre_colonia].extend(calles_colonia)

# Guardar los nombres de las colonias con sus calles en un archivo JSON
json_file = "colonias_tijuana.json"
with open(json_file, 'w') as file:
    json.dump(colonias_data, file)

print("Se ha guardado la lista de colonias de Tijuana con sus respectivas calles en el archivo:", json_file)
