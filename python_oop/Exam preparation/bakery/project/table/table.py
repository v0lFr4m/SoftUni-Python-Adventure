from abc import ABC

from project.baked_food.baked_food import BakedFood


class Table(ABC):
    def __init__(self, table_number: int , capacity:int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: list = []
        self.drink_orders: list = []
        self.number_of_people : int = 0
        self.is_reserved : bool = False

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self._capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people += number_of_people
        self.is_reserved = True
        return True

    def order_food(self, baked_food : BakedFood):
        self.food_orders.append(baked_food.name)

    def get_bill(self):
        return