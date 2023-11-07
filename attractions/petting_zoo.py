from .attraction import Attraction
from animals import Llama
class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    
    
    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)

        except AttributeError:
            print(f'this animal cannot be added to {self.attraction_name}')