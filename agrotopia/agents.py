class Agente:
    """Create a new person agent.
        param unique_id:   Unique identifier for the agent
        param model:       Model in which the agent runs
        param shape:       Shape object for the agent
        param agent_type:  Indicator if agent is infected ("infected", "susceptible", "neutral" or "dead")
        param mobility_range:  Range of distance to move in one step
    """
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
class Gaia:
    pass