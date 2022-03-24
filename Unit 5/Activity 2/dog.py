import random

class Dog(object):
    
    def __init__(self, name = "", breed = "", hunger = 0, aggression = 0):
        dog_names = ["Chester", "Rover", "Ace", "Sparky", "Fluffy", "Beans", "Foo Foo"]
        dog_breeds = ["German Shepard", "Golden Retriver", "Dalmatian", "Yorkie", "Shiba", "Spaniel"]

        if name == "":
            random_num = random.randint(0, len(dog_names) - 1)
            name = dog_names[random_num]
        
        if breed == "":
            random_num = random.randint(0, len(dog_breeds) - 1)
            breed = dog_breeds[random_num]
        
        hunger = random.randint(0, 10)
        aggression = random.randint(0, 10)

        self.name = name
        self.breed = breed
        self.hunger = hunger
        self.aggression = aggression
    
    def get_name(self):
        return self.name
    
    def get_breed(self):
        return self.breed

    def get_hunger(self):
        return self.hunger

    def get_aggression(self):
        return self.aggression

    def set_hunger(self, given_hunger):
        self.hunger = given_hunger
    
    def set_aggression(self, given_aggression):
        self.aggression = given_aggression

    def __str__(self):
        '''
        Returns the properties of the car
        '''
        return '\nName: {}\nBreed: {}\nAggression: {}\nHunger: {}'.format(self.name, self.breed, self.aggression, self.hunger)