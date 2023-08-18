from datetime import date

class Donkey:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

donk = Donkey("ted", "donkey", "afternoon")

print(f'{donk.name} the {donk.species} is available to pet during the {donk.shift} shift')