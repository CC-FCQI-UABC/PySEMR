# enfermedad.py

class Enfermedad:
    def __init__(self, nombre, probabilidad_inicial, estaciones_afectadas):
        self.nombre = nombre
        self.probabilidad_inicial = probabilidad_inicial
        self.estaciones_afectadas = estaciones_afectadas
        self.contracted_on = None

    def calculate_probability(self, temperature, season):
        if season in self.estaciones_afectadas:
            if season == "Invierno":
                return self.probabilidad_inicial * 1.20
            elif season == "Primavera":
                return self.probabilidad_inicial * 0.4                
            elif season == "Verano":
                return self.probabilidad_inicial * 0.7
            elif season == "Invierno":
                return self.probabilidad_inicial * 1.1
            else:
                return self.probabilidad_inicial
        else:
            return self.probabilidad_inicial
