class Zoo:
    __animals = 0
    def __init__(self, _name:str):
        self.name = _name
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.__animals = []

    def add_animal(self , _species , _name):
        if _species == 'mammal':
            self.mammals.append(_name)
        elif _species == 'fish':
            self.fishes.append(_name)
        elif _species == 'bird':
            self.birds.append(_name)
        Zoo.__animals += 1


    def get_info(self , _species):

        if _species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif _species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif _species == 'bird':
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"



zoo_name = input()
zoo = Zoo(zoo_name)
number_of_lines = int(input())

for i in range(number_of_lines):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species , name)

info = input()
print(zoo.get_info(info))