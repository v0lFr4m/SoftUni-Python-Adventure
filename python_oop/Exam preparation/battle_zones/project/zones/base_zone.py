from abc import ABC , abstractmethod

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code : str , volume: int):
        self.code = code
        self.volume = volume
        self.ships : list[BaseBattleship]= []

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value.isallnum():
            raise ValueError("Zone code must contain digits only!")
        self._code = value

    def get_ship(self):

