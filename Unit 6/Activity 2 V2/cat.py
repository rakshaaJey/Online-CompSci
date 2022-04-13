#imports
import random 

class Cat(object):
    '''
    Describes the class of cats
    '''

    def __init__(self, name = "", age = 0, breed = ""):
        '''
        Initializes the cat
        '''
        
        '''
        Assigns values for the parameters of the cat if none are given
        '''
        cat_names = ["Viktor", "Taco", "Tom", "Floof", "Henry", "Barry", "Sam", "Nav"]
        cat_breeds = ["American Shorthair", "Bengal", "Bombay", "British Longhair", "Maine Coon", "Persian"]

        if name == "":
            random_num = random.randint(0, len(cat_names) - 1)
            name = cat_names[random_num]

        if breed == "":
            random_num = random.randint(0, len(cat_breeds) - 1)
            breed = cat_breeds[random_num]

        self.name = name
        self.age = age
        self.breed = breed
    
    #Get methods
    def get_name(self):
        '''
        Returns the name of the cat
        '''
        return self.name
    
    def get_age(self):
        '''
        Returns the age of the cat
        '''
        return self.age

    def get_breed(self):
        '''
        Returns the breed of the cat
        '''
        return self.breed

    #Set methods
    def set_name(self, new_name):
        '''
        @param new_name is the new name of the cat

        Sets the name of the cat to the given name
        '''
        self.name = new_name
    
    def set_age(self, new_age):
        '''
        @param new_age is the new age of the cat

        Sets the age of the cat to the given age
        '''
        self.age = new_age
    
    def set_breed(self, new_breed):
        '''
        @param new_breed is the new breed of the cat

        Sets the breed of the cat to the given breed
        '''
        self.breed = new_breed

    def __str__(self):
        '''
        Returns the properties of the cat
        '''
        return '{} is a {} year old {}'.format(self.name, self.age, self.breed)