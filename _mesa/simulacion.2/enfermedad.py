#enfermedad.py
class Enfermedad:
    def __init__(self, nombre, probabilidad_inicial, estaciones_afectadas):
        self.nombre = nombre
        self.probabilidad_inicial = probabilidad_inicial
        self.estaciones_afectadas = estaciones_afectadas

    def calculate_probability(self, temperature, season):
        # Ajustar la probabilidad inicial según la estación del año
        if season in self.estaciones_afectadas:
            if season == "Invierno":
                # Multiplicar por un factor más alto en invierno
                return self.probabilidad_inicial * 1.5
            elif season == "Verano":
                # Multiplicar por un factor más bajo en verano
                return self.probabilidad_inicial * 0.8
            else:
                # Otra estación, mantener la probabilidad inicial
                return self.probabilidad_inicial
        else:
            # Si no es una estación afectada, mantener la probabilidad inicial
            return self.probabilidad_inicial