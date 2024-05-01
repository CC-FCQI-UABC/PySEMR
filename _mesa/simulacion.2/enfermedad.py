#enfermedad.py
class Enfermedad:
    def __init__(self, nombre, probabilidad_inicial, estaciones_afectadas):
        self.nombre = nombre
        self.probabilidad_inicial = probabilidad_inicial
        self.estaciones_afectadas = estaciones_afectadas

    def calculate_probability(self, temperature, season):
        if season in self.estaciones_afectadas:
            if season == "Invierno":
                return self.probabilidad_inicial * 1.5
            elif season == "Verano":
                return self.probabilidad_inicial * 0.8
            else:
                return self.probabilidad_inicial
        else:
            return self.probabilidad_inicial