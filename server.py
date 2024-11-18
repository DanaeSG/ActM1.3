# A00836760 Danaé Sánchez

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization import Slider

from model import DanceHall

def dance_hall_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}

    if agent.estado == "soltero":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
    elif agent.estado == "emparejado":
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
    elif agent.estado == "cansado":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2

    return portrayal


# Parameters for the visualization
NUM_DANCERS = 20
WIDTH = 10
HEIGHT = 10

model_params = {
    "num_dancers": Slider("Número de bailarines", NUM_DANCERS, 10, 50, 1),
    "width": WIDTH,
    "height": HEIGHT,
}

canvas_element = CanvasGrid(dance_hall_portrayal, WIDTH, HEIGHT, 500, 500)

chart_element = ChartModule([
    {"Label": "Parejas Formadas", "Color": "#00AA00"},
    {"Label": "Bailarines Cansados", "Color": "#AA0000"}
])

server = ModularServer(
    DanceHall,
    [canvas_element, chart_element],
    "Salón de Baile",
    model_params,
)

server.port = 8521
