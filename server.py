from mesa_geo.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from model import Territorio, PersonAgent
from mesa_geo.visualization.MapModule import MapModule


class InfectedText(TextElement):
    """
    Display a text count of how many steps have been taken
    """

    def __init__(self):
        pass

    def render(self, model):
        return "Steps: " + str(model.steps)


model_params = {
    "pop_size": UserSettableParameter("slider", "Population size", 30, 10, 100, 10),
    "init_relacion": UserSettableParameter(
        "slider", "Fraction initial infection", 0.2, 0.00, 1.0, 0.05
    ),
    "exposure_distance": UserSettableParameter(
        "slider", "Exposure distance", 500, 100, 1000, 100
    ),
}


def infected_draw(agent):
    """
    Portrayal Method for canvas
    """
    portrayal = dict()
    if isinstance(agent, PersonAgent):
        portrayal["radius"] = "2"
    if agent.atype in ["hotspot", "relacion"]:
        portrayal["color"] = "Red"
    elif agent.atype in ["safe", "normal"]:
        portrayal["color"] = "Green"
    elif agent.atype in ["neutral"]:
        portrayal["color"] = "Blue"
    elif agent.atype in ["sin_relacion"]:
        portrayal["color"] = "Black"
    elif agent.atype in ["otros"]:
        portrayal["color"] = "Yellow"
    return portrayal


infected_text = InfectedText()
map_element = MapModule(infected_draw, Territorio.MAP_COORDS, 10, 800, 760)
infected_chart = ChartModule(
    [
        {"Label": "relacion", "Color": "Red"},
        {"Label": "normal", "Color": "Green"},
        {"Label": "neutral", "Color": "Blue"},
        {"Label": "otros", "Color": "Yellow"},
        {"Label": "sin_relacion", "Color": "Black"},
    ]
)
server = ModularServer(
    Territorio,
    [map_element, infected_text, infected_chart],
    "Agrotopia 1.0.0",
    model_params,
)
server.launch()