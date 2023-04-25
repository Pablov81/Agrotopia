#Import classess from modules (agents,load_files)
from agents import Agente
from load_files import Rates

#Initializate Classes
class Mesa_Directiva(Agente):
    """Mesa Directiva se encarga de ODD

    Parameters:
        nombre (str): Nombre de la Mesa Directiva
        embalse_max, embalse_min(float): volumen maximo y minimo del embalse
    """
    pass
    
class Presidente_Canal(Agente):
    """_summary_

    Args:
        Agente (_type_): _description_
    """
    pass

class Agricultor(Agente):
    """_summary_

    Args:
        Agente (_type_): _description_
    """
    pass
    
class Cultivo(Agente):
    """_summary_

    Args:
        Agente (_type_): _description_
    """
    pass

#Jhon_Test=Agente("Jhon Test",100,100,100)
#Jhon_Test.atributos()