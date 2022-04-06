import random 

class Dog(object):
    def __init__(self, name ="", age = -1, breed = ""):

        dog_names = ["Chester", "Rover", "Ace", "Sparky", "Fluffy", "Beans", "Foo Foo"]
        dog_breeds = ["German Shepard", "Golden Retriver", "Dalmatian", "Yorkie", "Shiba", "Spaniel"]

        if name == "":
            random_num = random.randint(0, len(dog_names) - 1)
            name = dog_names[random_num]

        if age == -1:
            age = random.randint(0, 16)

        if breed == "":
            random_num = random.randint(0, len(dog_breeds) - 1)
            breed = dog_breeds[random_num]

        self.name = name
        self.age = age
        self.breed = breed
    
    #Get methods
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_breed(self):
        return self.breed

    #Set methods
    def set_name(self, new_name):
        self.name = new_name
    
    def set_age(self, new_age):
        self.age = new_age
    
    def set_breed(self, new_breed):
        self.breed = new_breed

    def __str__(self):
        '''
        Returns the properties of the car
        '''
        return '{} is a {} year old {}'.format(self.name, self.age, self.breed)