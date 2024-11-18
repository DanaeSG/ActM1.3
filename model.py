# A00836760 Danaé Sánchez

from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from agents import Dancer

import random


class DanceHall(Model):
    """Model representing the dance hall."""
    def __init__(self, num_dancers, width, height):
        super().__init__()  # Properly initialize the parent Model class

        self.num_agents = num_dancers
        self.grid = SingleGrid(width, height, False)  # SingleGrid ensures one agent per cell
        self.schedule = SimultaneousActivation(self)

        self.border_cells = self.get_border_cells(width, height)
        self.dance_floor_cells = self.get_dance_floor_cells(width, height)

        # Create agents
        for i in range(self.num_agents):
            energia_inicial = random.randint(5, 20)  # Random initial energy
            tiempo_descanso = random.randint(3, 7)  # Random rest time
            dancer = Dancer(i, self, energia_inicial, tiempo_descanso)
            self.schedule.add(dancer)

            # Place agents in random empty positions
            position = self.get_random_empty_position()
            self.grid.place_agent(dancer, position)

        # DataCollector for metrics
        self.datacollector = DataCollector(
            model_reporters={
                "Parejas Formadas": lambda m: sum(1 for a in m.schedule.agents if a.estado == "emparejado") // 2,
                "Bailarines Cansados": lambda m: sum(1 for a in m.schedule.agents if a.estado == "cansado"),
            }
        )

    def get_border_cells(self, width, height):
        """Returns the border cells of the grid."""
        return [(x, y) for x in range(width) for y in range(height)
                if x == 0 or y == 0 or x == width - 1 or y == height - 1]

    def get_dance_floor_cells(self, width, height):
        """Returns the dance floor cells of the grid."""
        return [(x, y) for x in range(1, width - 1) for y in range(1, height - 1)]

    def get_random_empty_position(self):
        """Finds a random empty cell on the grid."""
        while True:
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            if self.grid.is_cell_empty((x, y)):
                return x, y

    def is_in_border(self, pos):
        """Checks if a position is in the border."""
        return pos in self.border_cells

    def is_in_dance_floor(self, pos):
        """Checks if a position is in the dance floor."""
        return pos in self.dance_floor_cells

    def step(self):
        """Advances the simulation by one step."""
        self.datacollector.collect(self)
        self.schedule.step()
