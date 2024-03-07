import random

def numeroTelefono(cantidad_digitos, ciudad):
    min_valor = 10 ** (cantidad_digitos - 1)  
    max_valor = (10 ** cantidad_digitos) - 1 
    digitos = random.randint(min_valor, max_valor)
    numTelefono = "+52" + ladas(ciudad) + str(digitos)
    return numTelefono

def ladas(case):
    if case == "Ensenada": 
        return "(646)"
    elif case == "Tijuana": 
        return "(664)"
    elif case == "Mexicali": 
        return "(686)"
    elif case == "Tecate": 
        return "(665)"
    elif case == "Playas de Rosarito": 
        return "(661)"
    elif case =="San Quintín": 
        return "(616)"
    elif case == "San Felipe": 
        return "(686)"