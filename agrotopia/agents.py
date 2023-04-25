class Agente:
    """Create a new Agent
    """
    def __init__(self, nombre, fuerza, personalidad, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.personalidad = personalidad
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·personalidad:", self.personalidad)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, personalidad, defensa):
        self.fuerza = self.fuerza + fuerza
        self.personalidad = self.personalidad + personalidad
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
class Gaia:
    pass