# enfermedad.py

class Enfermedad:
    def __init__(self, nombre, probabilidad_inicial, estaciones_afectadas):
        self.nombre = nombre
        self.probabilidad_inicial = probabilidad_inicial
        self.estaciones_afectadas = estaciones_afectadas
        self.contracted_on = None  # Agregamos el atributo para rastrear la fecha de contratación

    # La simulacion de contagio en cuanto al ambiente no esta basada en datos reales
    def calculate_probability(self, temperature, season):
        if season in self.estaciones_afectadas:
            if season == "Invierno":
                return self.probabilidad_inicial * 1.10
            elif season == "Verano":
                return self.probabilidad_inicial * 0.4
            else:
                return self.probabilidad_inicial
        else:
            return self.probabilidad_inicial
