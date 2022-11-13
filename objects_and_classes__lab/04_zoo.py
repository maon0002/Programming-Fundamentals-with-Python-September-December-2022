class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        selected_animal_type = ''
        if species == "mammal":
            selected_animal_type += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"

        elif species == "fish":
            selected_animal_type += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"

        elif species == "bird":
            selected_animal_type += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        selected_animal_type += f"Total animals: {Zoo.__animals}"
        return selected_animal_type


name_of_the_zoo = input()
which_zoo = Zoo(name_of_the_zoo)
number_of_inputs = int(input())

for x in range(number_of_inputs):
    species, name = input().split(" ")
    which_zoo.add_animal(species, name)

chosen_animal_type = input()
which_zoo.get_info(chosen_animal_type)
print(which_zoo.get_info(chosen_animal_type))
