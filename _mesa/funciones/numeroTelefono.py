import random

def numeroTelefono(cantidad_digitos, ciudad):
    min_valor = 10 ** (cantidad_digitos - 1)  
    max_valor = (10 ** cantidad_digitos) - 1 
    digitos = random.randint(min_valor, max_valor)
    numTelefono = "+52" + ladas(ciudad) + str(digitos)
    return numTelefono

def ladas(case):
    if case == "Ensenada" or case == "ENSENADA": 
        return "(646)"
    elif case == "Tijuana" or case ==  "TIJUANA": 
        return "(664)"
    elif case == "Mexicali" or case ==  "MEXICALI": 
        return "(686)"
    elif case == "Tecate" or case ==  "TECATE": 
        return "(665)"
    elif case == "Playas de Rosarito" or case ==  "PLAYAS DE ROSARITO": 
        return "(661)"
    elif case =="San Quintín" or case ==  "SAN QUINTÍN" or case ==  "SAN QUINTIN": 
        return "(616)"
    elif case == "San Felipe" or case ==  "SAN FELIPE": 
        return "(686)"
    elif case =="Valle de Las Palmas" or case == "Valle de Las Palmas":
        return "(665)"#