#imports
import random 

class Dog(object):
    '''
    Describes the class of dogs
    '''

    def __init__(self, name = "", age = 0, breed = ""):
        '''
        Initializes the dog
        '''
        
        '''
        Assigns values for the parameters of the dog if none are given
        '''
        dog_names = ["Chester", "Rover", "Ace", "Sparky", "Fluffy", "Beans", "Foo Foo"]
        dog_breeds = ["German Shepard", "Golden Retriver", "Dalmatian", "Yorkie", "Shiba", "Spaniel"]

        if name == "":
            random_num = random.randint(0, len(dog_names) - 1)
            name = dog_names[random_num]

        if breed == "":
            random_num = random.randint(0, len(dog_breeds) - 1)
            breed = dog_breeds[random_num]

        self.name = name
        self.age = age
        self.breed = breed
    
    #Get methods
    def get_name(self):
        '''
        Returns the name of the dog
        '''
        return self.name
    
    def get_age(self):
        '''
        Returns the age of the dog
        '''
        return self.age

    def get_breed(self):
        '''
        Returns the breed of the dog
        '''
        return self.breed

    #Set methods
    def set_name(self, new_name):
        '''
        @param new_name is the new name of the dog

        Sets the name of the dog to the given name
        '''
        self.name = new_name
    
    def set_age(self, new_age):
        '''
        @param new_age is the new age of the dog

        Sets the age of the dog to the given age
        '''
        self.age = new_age
    
    def set_breed(self, new_breed):
        '''
        @param new_breed is the new breed of the dog

        Sets the breed of the dog to the given breed
        '''
        self.breed = new_breed

    def __str__(self):
        '''
        Returns the properties of the dog
        '''
        return '{} is a {} year old {}'.format(self.name, self.age, self.breed)