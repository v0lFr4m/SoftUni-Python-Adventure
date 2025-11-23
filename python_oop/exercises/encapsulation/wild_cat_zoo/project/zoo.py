from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name , budget , animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal , price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(current_worker.salary for current_worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = sum(current_animal.money_for_care for current_animal in self.animals)
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        output = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"
        ]
        output.extend(str(l) for l in lions)

        output.append(f"----- {len(tigers)} Tigers:")
        output.extend(str(t) for t in tigers)

        output.append(f"----- {len(cheetahs)} Cheetahs:")
        output.extend(str(c) for c in cheetahs)

        return "\n".join(output)

    def workers_status(self):
        keepers = [k for k in self.workers if isinstance(k, Keeper)]
        caretakers = [c for c in self.workers if isinstance(c , Caretaker)]
        vets = [v for v in self.workers if isinstance(v , Vet)]

        output = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:"
        ]
        output.extend(str(k) for k in keepers)

        output.append(f"----- {len(caretakers)} Caretakers:")
        output.extend(str(c) for c in caretakers)

        output.append(f"----- {len(vets)} Vets:")
        output.extend(str(v) for v in vets)

        return "\n".join(output)

