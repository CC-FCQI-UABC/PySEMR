import random

def licencia():
    licencia = "BC"
    for i in range(9):
        licencia += str(random.randint(0, 9))
    return licencia
