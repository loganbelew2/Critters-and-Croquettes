from datetime import date
from .animal import Animal
from movements import Walking
class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
      Animal.__init__(self, name, species, food, chip_num)
      Walking.__init__(self)
      self.shift = shift


    def feed(self):
       print(f'{self.name} was calmed down and fed {self.food} on {date.today().strftime("%m/%d/%y")}')