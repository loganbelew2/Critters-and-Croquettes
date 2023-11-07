from animals import CopperHead, RatSnake, Llama, Goat, Donkey, Mallard, Goldfish, Goose
from attractions import PettingZoo, Attraction, SnakePit, WetLands
def main():
    #instantiating animals and attractions
    varmint_village = PettingZoo('varmint_village', 'full of fluffy animals')
    Garry = Llama('Garry', 'Llama', 'afternoon', 'chicken', 1.1)
    donk = Donkey("ted", "donkey", "afternoon", 'carrots', 1.11)
    Leo = Goat('Leo', 'goat', 'night', 'grapes', 1.13)
    Bob = Goose('Bob', 'goose', 'fish', 1.14)
    Emily = Llama('Emily', 'Llama', 'morning', 'chicken', 1.15)
    #calling addAnimals method to extend list of animals 
    varmint_village.add_animal(Garry)
    print(varmint_village)

    
if __name__ == "__main__":
    main()