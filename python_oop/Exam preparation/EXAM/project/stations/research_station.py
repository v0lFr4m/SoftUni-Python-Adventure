from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    INITIAL_CAPACITY = 5
    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value : float):
        for current_astronaut in self.astronauts:
            if current_astronaut.specialization == ScientistAstronaut.INITIAL_SPECIALIZATION and current_astronaut.salary <= min_value:
                current_astronaut.salary += 5_000.0
