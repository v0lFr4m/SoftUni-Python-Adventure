from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    INITIAL_CAPACITY = 3
    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        for current_astronaut in self.astronauts:
            if current_astronaut.specialization == EngineerAstronaut.INITIAL_SPECIALIZATION and current_astronaut.salary <= min_value:
                current_astronaut.salary += 3_000.0
