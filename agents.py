# A00836760 Danaé Sánchez

from mesa import Agent
import random


class Dancer(Agent):
    DIRECTIONS = ['up', 'down', 'left', 'right']

    def __init__(self, unique_id, model, energia_inicial, tiempo_descanso):
        super().__init__(unique_id, model)
        self.energia = energia_inicial
        self.tiempo_descanso = tiempo_descanso
        self.estado = "soltero"  # Can be "soltero", "emparejado", or "cansado"
        self.pareja = None
        self.tiempo_bailando = 0
        self.tiempo_restante_descanso = 0
        self.next_pos = None
        self.direction = random.choice(self.DIRECTIONS)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction
        if self._direction == 'up':
            self.dx, self.dy = -1, 0
        elif self._direction == 'down':
            self.dx, self.dy = 1, 0
        elif self._direction == 'right':
            self.dx, self.dy = 0, 1
        elif self._direction == 'left':
            self.dx, self.dy = 0, -1

    def move(self):
        """Decides the next position for the agent based on its state."""
        next_pos = (self.pos[0] + self.dx, self.pos[1] + self.dy)

        if self.estado == "soltero":  # Single agents move within the dance floor
            if not self.model.is_in_dance_floor(next_pos) or not self.model.grid.is_cell_empty(next_pos):
                # Change direction if blocked or leaving the dance floor
                self.direction = random.choice(self.DIRECTIONS)
            else:
                self.next_pos = next_pos

        elif self.estado == "emparejado":  # Paired agents move within the dance floor
            if not self.model.is_in_dance_floor(next_pos) or not self.model.grid.is_cell_empty(next_pos):
                self.direction = random.choice(self.DIRECTIONS)
            else:
                self.next_pos = next_pos

        elif self.estado == "cansado":  # Tired agents move toward the borders
            if not self.model.is_in_border(next_pos) or not self.model.grid.is_cell_empty(next_pos):
                self.direction = random.choice(self.DIRECTIONS)
            else:
                self.next_pos = next_pos

        # Debug print
        print(f"Agent {self.unique_id}: pos={self.pos}, next_pos={self.next_pos}, estado={self.estado}, direction={self.direction}")

    def buscar_pareja(self):
        """Searches for a partner in the neighborhood."""
        if self.estado != "soltero":
            return
        
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        posibles_parejas = [agente for agente in neighbors if isinstance(agente, Dancer) and agente.estado == "soltero"]
        
        if posibles_parejas:
            pareja = random.choice(posibles_parejas)
            self.emparejar(pareja)

    def emparejar(self, pareja):
        """Forms a pair with another agent."""
        self.estado = "emparejado"
        pareja.estado = "emparejado"
        self.pareja = pareja
        pareja.pareja = self

    def bailar(self):
        """Simulates dancing if paired."""
        if self.estado == "emparejado":
            self.energia -= 1
            self.tiempo_bailando += 1
            if self.energia <= 0:
                self.estado = "cansado"
                self.pareja.estado = "soltero"
                self.pareja.pareja = None
                self.pareja = None
                self.tiempo_restante_descanso = self.tiempo_descanso

    def descansar(self):
        """Simulates resting for a tired dancer."""
        if self.estado == "cansado":
            self.tiempo_restante_descanso -= 1
            if self.tiempo_restante_descanso <= 0:
                self.estado = "soltero"
                self.energia = random.randint(5, 20)

    def step(self):
        """Determines the next action based on the state."""
        if self.estado == "soltero":
            self.move()
            self.buscar_pareja()
        elif self.estado == "emparejado":
            self.bailar()
            self.move()
        elif self.estado == "cansado":
            self.descansar()
            self.move()

    def advance(self):
        """Moves the agent to its next position."""
        if self.next_pos is not None:
            # Check if the next position is empty
            if self.model.grid.is_cell_empty(self.next_pos):
                self.model.grid.move_agent(self, self.next_pos)
            