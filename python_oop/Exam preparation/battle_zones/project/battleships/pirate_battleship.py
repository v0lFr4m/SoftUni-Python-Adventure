from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INITIAL_AMMO = 80
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMO)

    def attack(self):
        if self.INITIAL_AMMO < 0:
            self.INITIAL_AMMO = 0
        self.INITIAL_AMMO -= 10


