from .animal import Animal

class RatSnake(Animal):
    def __init__(self, name, species, food, chip_num ):
        super().__init__(name, species, food, chip_num)
