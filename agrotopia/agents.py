class Agente:
    """Create a new Agent
    the attributes
    """
    def __init__(self, nombre:str, resistencia:float, personalidad:str, vitalidad:int):
        self.nombre = nombre
        self.resistencia = resistencia
        self.personalidad = personalidad
        self.vitalidad = vitalidad
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·resistencia:", self.resistencia)
        print("·personalidad:", self.personalidad)
        print("·vitalidad:", self.vitalidad)

    def esta_vivo(self):
        return self.vitalidad > 0
    
class Gaia:
    """Disaster or Environment Agent
    """
    pass