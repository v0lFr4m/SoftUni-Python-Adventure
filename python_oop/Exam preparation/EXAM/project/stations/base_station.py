import re
from abc import ABC,abstractmethod


class BaseStation(ABC):
    def __init__(self, name: str , capacity:int):
        self.name = name
        self.capacity = capacity
        self.astronauts : list= []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not re.fullmatch(r"[A-Za-z0-9-]+", value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self._name = value
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self._capacity = value

    @property
    def available_capacity(self):
        return self.capacity - len(self.astronauts)

    def calculate_total_salaries(self):
        total_salaries = sum(a.salary for a in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self):
        if not self.astronauts:
            astronauts_as_string = "N/A"
        else:
            astronauts_id = sorted([a.id_number for a in self.astronauts])
            astronauts_as_string = " #".join(astronauts_id)

        return f"Station name: {self.name}; Astronauts: {astronauts_as_string}; Total salaries: {self.calculate_total_salaries()}"
    @abstractmethod
    def update_salaries(self ,min_value: float):
        pass
