import os
import random

def calle(nombre_ciudad):
    archivo = ""

    if nombre_ciudad == 'Tijuana':
        archivo = "callesTijuana.txt"
    elif nombre_ciudad == 'Mexicali':
        archivo = "callesMexicali.txt"
    elif nombre_ciudad == 'Rosarito':
        archivo = "callesRosarito.txt"
    elif nombre_ciudad == 'Tecate':
        archivo = "callesTecate.txt"
    
    else: #Ensenada y otros municipios
        archivo = "callesEnsenada.txt"
    
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data_mexicana', 'calles', archivo)
    
    linea_aleatoria = None
    
    contador = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for linea in archivo:
            contador += 1
            if random.randint(0, contador - 1) == 0:
                linea_aleatoria = linea.strip() 
    
    return linea_aleatoria
