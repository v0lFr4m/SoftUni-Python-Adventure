from abc import ABC, abstractmethod


class BaseCollector(ABC):
    def __init__(self, name : str , available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        is_valid = all([char.isalnum() or char.isspace() for char in value.strip()])
        if not is_valid:
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self._name = value

    @property
    def available_money(self):
        return self._available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self._available_money = value

    @property
    def available_space(self):
        return self._available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self._available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        if self.available_money is None or self.available_space is None:
            return False
        return artifact_price <= self.available_money and artifact_space_required <= self.available_space

    # def __str__(self):
    #     if self.purchased_artifacts:
    #         sorted_artifacts = sorted(self.purchased_artifacts, reverse=True)
    #         artifacts_str = ", ".join(sorted_artifacts)
    #     else:
    #         artifacts_str = "none"
    #
    #     return (f"Collector name: {self.name}; "
    #             f"Money available: {self.available_money:.2f}; "
    #             f"Space available: {self.available_space}; "
    #             f"Artifacts: {artifacts_str}")

    def __str__(self):

        artifacts_names = [a.name for a in self.purchased_artifacts]

        sorted_artifacts_names = sorted(artifacts_names, reverse=True)

        return (f"Collector name: {self.name}; "
                f"Money available: {self.available_money:.2f}; "
                f"Space available: {self.available_space}; "
                f"Artifacts: {', '.join(sorted_artifacts_names) or 'none'}")
