from mesa.datacollection import DataCollector
from mesa import Model
from mesa.time import BaseScheduler
from mesa_geo.geoagent import GeoAgent, AgentCreator
from mesa_geo import GeoSpace
from shapely.geometry import Point

#################################################################

#################################################################
class PersonAgent(GeoAgent):
    """Person Agent."""

    def __init__(
        self,
        unique_id,
        model,
        shape,
        agent_type="normal",
        mobility_range=100,
        recovery_rate=0.2,
        death_risk=0.1,
        init_relacion=0.1,
    ):
        """
        Create a new person agent.
        :param unique_id:   Unique identifier for the agent
        :param model:       Model in which the agent runs
        :param shape:       Shape object for the agent
        :param agent_type:  Indicator if agent is infected ("infected", "susceptible", "neutral" or "dead")
        :param mobility_range:  Range of distance to move in one step
        """
        super().__init__(unique_id, model, shape)
        # Agent parameters
        self.atype = agent_type
        self.mobility_range = mobility_range
        self.recovery_rate = recovery_rate
        self.death_risk = death_risk

        # Random choose if infected
        if self.random.random() < init_relacion:
            self.atype = "relacion"
            self.model.counts["relacion"] += 1  # Adjust initial counts
            self.model.counts["normal"] -= 1

    def move_point(self, dx, dy):
        """
        Move a point by creating a new one
        :param dx:  Distance to move in x-axis
        :param dy:  Distance to move in y-axis
        """
        return Point(self.shape.x + dx, self.shape.y + dy)

    def step(self):
        """Advance one step."""
        # If susceptible, check if exposed
        if self.atype == "normal":
            neighbors = self.model.grid.get_neighbors_within_distance(
                self, self.model.exposure_distance
            )
            for neighbor in neighbors:
                if (
                    neighbor.atype == "relacion"
                    and self.random.random() < self.model.interaccion_risk
                ):
                    self.atype = "relacion"
                    break

        # If infected, check if it recovers or if it dies
        elif self.atype == "relacion":
            if self.random.random() < self.recovery_rate:
                self.atype = "neutral"
            elif self.random.random() < self.death_risk:
                self.atype = "sin_relacion"

        # If not dead, move
        if self.atype != "sin_relacion":
            move_x = self.random.randint(-self.mobility_range, self.mobility_range)
            move_y = self.random.randint(-self.mobility_range, self.mobility_range)
            self.shape = self.move_point(move_x, move_y)  # Reassign shape

        self.model.counts[self.atype] += 1  # Count agent type

    def __repr__(self):
        return "Person " + str(self.unique_id)


class NeighbourhoodAgent(GeoAgent):
    """Neighbourhood agent. Changes color according to number of infected inside it."""

    def __init__(self, unique_id, model, shape, agent_type="safe", hotspot_threshold=1):
        """
        Create a new Neighbourhood agent.
        :param unique_id:   Unique identifier for the agent
        :param model:       Model in which the agent runs
        :param shape:       Shape object for the agent
        :param agent_type:  Indicator if agent is infected ("infected", "susceptible", "neutral" or "dead")
        :param hotspot_threshold:   Number of infected agents in region to be considered a hot-spot
        """
        super().__init__(unique_id, model, shape)
        self.atype = agent_type
        self.hotspot_threshold = (
            hotspot_threshold
        )  # When a neighborhood is considered a hot-spot
        self.color_hotspot()

    def step(self):
        """Advance agent one step."""
        self.color_hotspot()
        self.model.counts[self.atype] += 1  # Count agent type

    def color_hotspot(self):
        # Decide if this region agent is a hot-spot (if more than threshold person agents are infected)
        neighbors = self.model.grid.get_intersecting_agents(self)
        infected_neighbors = [
            neighbor for neighbor in neighbors if neighbor.atype == "relacion"
        ]
        if len(infected_neighbors) >= self.hotspot_threshold:
            self.atype = "hotspot"
        else:
            self.atype = "safe"

    def __repr__(self):
        return "Canal " + str(self.unique_id)


class Territorio(Model):
    """Model class for a simplistic infection model."""

    # Geographical parameters for desired map
    MAP_COORDS = [-36.119572927354504, -71.72767639160156]  # Agrotopia
    #geojson_regions = "resources/TorontoNeighbourhoods.geojson"
    geojson_regions = "resources/areas.geojson"
    unique_id = "nombre"

    geojson_canalillo="resources/varilla.geojson"

    def __init__(self, pop_size, init_relacion, exposure_distance, interaccion_risk=0.2):
        """
        Create a new InfectedModel
        :param pop_size:        Size of population
        :param init_infected:   Probability of a person agent to start as infected
        :param exposure_distance:   Proximity distance between agents to be exposed to each other
        :param interaccion_risk:      Probability of agent to become infected, if it has been exposed to another infected
        """
        self.schedule = BaseScheduler(self)
        self.grid = GeoSpace()
        self.steps = 0
        self.counts = None
        self.reset_counts()

        # SIR model parameters
        self.pop_size = pop_size
        self.counts["normal"] = pop_size
        self.exposure_distance = exposure_distance
        self.interaccion_risk = interaccion_risk

        self.running = True
        self.datacollector = DataCollector(
            {
                "relacion": get_relacion_count,
                "normal": get_normal_count,
                "neutral": get_neutral_count,
                "sin_relacion": get_sin_relacion_count,
                "otros": get_otros_count,
            }
        )

        # Set up the Neighbourhood patches for every region in file (add to schedule later)
        AC = AgentCreator(NeighbourhoodAgent, {"model": self})
        neighbourhood_agents = AC.from_file(
            self.geojson_regions, unique_id=self.unique_id
        )
        self.grid.add_agents(neighbourhood_agents)

        # Generate PersonAgent population
        ac_population = AgentCreator(
            PersonAgent, {"model": self, "init_relacion": init_relacion}
        )
        # Generate random location, add agent to grid and scheduler
        for i in range(pop_size):
            this_neighbourhood = self.random.randint(
                0, len(neighbourhood_agents) - 1
            )  # Region where agent starts
            center_x, center_y = neighbourhood_agents[
                this_neighbourhood
            ].shape.centroid.coords.xy
            this_bounds = neighbourhood_agents[this_neighbourhood].shape.bounds
            spread_x = int(
                this_bounds[2] - this_bounds[0]
            )  # Heuristic for agent spread in region
            spread_y = int(this_bounds[3] - this_bounds[1])
            this_x = center_x[0] + self.random.randint(0, spread_x) - spread_x / 2
            this_y = center_y[0] + self.random.randint(0, spread_y) - spread_y / 2
            this_person = ac_population.create_agent(
                Point(this_x, this_y), "P" + str(i)
            )
            self.grid.add_agents(this_person)
            self.schedule.add(this_person)

        # Add the neighbourhood agents to schedule AFTER person agents,
        # to allow them to update their color by using BaseScheduler
        for agent in neighbourhood_agents:
            self.schedule.add(agent)

        self.datacollector.collect(self)

    def reset_counts(self):
            self.counts = {
            "normal": 0,
            "relacion": 0,
            "neutral": 0,
            "sin_relacion": 0,
            "otros":0,
            "safe": 0,
            "hotspot": 0,

        }

    def step(self):
        """Run one step of the model."""
        self.steps += 1
        self.reset_counts()
        self.schedule.step()
        self.grid._recreate_rtree()  # Recalculate spatial tree, because agents are moving

        self.datacollector.collect(self)

        # Run until no one is infected
        if self.counts["relacion"] == 0:
            self.running = False


# Functions needed for datacollector
def get_relacion_count(model):
    return model.counts["relacion"]


def get_normal_count(model):
    return model.counts["normal"]


def get_neutral_count(model):
    return model.counts["neutral"]


def get_sin_relacion_count(model):
    return model.counts["sin_relacion"]

def get_otros_count(model):
    return model.counts["otros"]