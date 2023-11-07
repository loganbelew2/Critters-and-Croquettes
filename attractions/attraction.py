class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def addAnimals(self, animals: list ):      
         if isinstance(animals, list):
            for animal in animals:
                 self.animals.append(animal)
         else:
            raise ValueError("animals parameter must be a list")

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)
    
    @property
    def last_added(self):
        return self.animals[len(self.animals) -1]