from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    INITIAL_SPECIALIZATION = "EngineerAstronaut"
    INITIAL_STAMINA = 80

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.INITIAL_SPECIALIZATION, self.INITIAL_STAMINA)

    def train(self):
        result = self.stamina + 5
        if result > 100:
            result = 100

        self.stamina = result


