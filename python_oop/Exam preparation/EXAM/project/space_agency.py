from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    VALID_TYPES_OF_ASTRONAUTS = ["EngineerAstronaut", "ScientistAstronaut"]
    VALID_TYPES_OF_STATIONS = ["ResearchStation", "MaintenanceStation"]
    def __init__(self):
        self.astronauts :list[BaseAstronaut] = []
        self.stations : list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if not astronaut_type in self.VALID_TYPES_OF_ASTRONAUTS:
            raise ValueError("Invalid astronaut type!")

        for astronaut in self.astronauts:
            if astronaut.id_number == astronaut_id_number:
                raise ValueError(f"{astronaut_id_number} has been already added!")

        if astronaut_type == "EngineerAstronaut":
            astronaut = EngineerAstronaut(astronaut_id_number, astronaut_salary)
            self.astronauts.append(astronaut)

        elif astronaut_type == "ScientistAstronaut":
            astronaut = ScientistAstronaut(astronaut_id_number, astronaut_salary)
            self.astronauts.append(astronaut)

        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type : str , station_name : str):
        if not station_type in self.VALID_TYPES_OF_STATIONS:
            raise ValueError("Invalid station type!")

        for station in self.stations:
            if station.name == station_name:
                raise ValueError(f"{station_name} has been already added!")

        if station_type == "ResearchStation":
            station = ResearchStation(station_name)
            self.stations.append(station)
        elif station_type == "MaintenanceStation":
            station = MaintenanceStation(station_name)
            self.stations.append(station)

        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if s.name == station_name), None)
        if station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut = next((a for a in self.astronauts if a.specialization == astronaut_type), None)
        if astronaut is None:
            raise ValueError("No available astronauts of the type!")

        if station.available_capacity <= 0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1

        return f"{astronaut.id_number} was assigned to {station_name}."

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int):
        for session in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
        total_stamina = sum(a.stamina for a in station.astronauts)

        return (f"{station.name} astronauts have {total_stamina} "
                f"total stamina after {sessions_number} training session/s.")
    @staticmethod
    def retire_astronaut(station: BaseStation, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        if astronaut is None or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value : float):

        for station in self.stations:
            station.update_salaries(min_value)

        total_capacity = sum(station.available_capacity for station in self.stations)

        output_line = [
            "*Space Agency Up-to-Date Report*",
            f"Total number of available astronauts: {len(self.astronauts)}",
            f"**Stations count: {len(self.stations)}; Total available capacity: {total_capacity}**"
        ]

        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))
        for station in sorted_stations:
            output_line.append(station.status())

        return "\n".join(output_line)

