import random
from datetime import datetime

class Estudiante:
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.anio_nacimiento = anio_nacimiento
        self.carrera = carrera
        self.matricula = self.generar_matricula()

    def generar_matricula(self):
        year = datetime.now().year % 100
        year_nac = int(str(self.anio_nacimiento)[-2:])
        letra_nombre = self.nombre[0]
        letras_apellido = self.apellido_paterno[:3] + self.apellido_materno[:3]
        random_num = str(random.randint(100,999))
        letras_carrera = self.carrera[:3]
        matricula = "{:02d}{:02d}{}{}{}{}".format(year, year_nac, letra_nombre, letras_apellido, random_num, letras_carrera)
