class Persona:
    def __init__(self, nombre, anio_nacimiento,edad):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento
        self.edad= edad

    def calcular_edad(self, anio_actual):
        self.edad = anio_actual - self.anio_nacimiento
        return self.edad