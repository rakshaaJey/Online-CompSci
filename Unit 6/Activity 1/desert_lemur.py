from unicodedata import decimal
import lemur
import random

class DesertLemur(lemur.Lemur):

    def __init__(self, its_age = 0, its_weight = 0, its_breed = "", its_gender = "", its_location = "", its_coat = "", its_classification = "", grooming = "", female_role = "", coat_colour = "", food = "", death_rate = 0):
        '''
        Constructor using age, weight, breed, gender, location, coat, classification, grooming, female role, coat colour, food and death rate
        '''
        if coat_colour == "":
            coat_colour = "White"
        
        if food == "":
            food = "Cacti"
        
        if death_rate == 0:
            death_rate = round(2/3, 2)

        if its_breed == "":
            its_breed = "Desert Lemur"
        
        if its_age == 0:
            its_age = random.randint(0, 25)
        
        if its_weight == 0:
            its_weight = random.uniform(1.0, 6.7)

        super().__init__(its_age, its_weight, its_breed, its_gender, its_location, its_coat, its_classification, grooming, female_role)

        self.coat_colour = coat_colour
        self.food = food
        self.death_rate = death_rate

    #Get Methods
    def get_coat_colour(self):
        '''
        Returns the coat colour
        '''
        return self.coat_colour
    
    def get_food(self):
        '''
        Returns the food
        '''
        return self.food
    
    def get_death_rate(self):
        '''
        Returns the death rate
        '''
        return self.death_rate

    #Set Methods
    def set_coat_colour(self, new_coat_colour):
        '''
        @param new_coat_colour is the new coat colour of the object

        Sets the coat colour to have the value of the given parameter
        '''
        self.coat_colour = new_coat_colour
    
    def set_food(self, new_food):
        '''
        @param new_food is the new food of the object

        Sets the food to have the value of the given parameter
        '''
        self.food = new_food
    
    def set_death_rate(self, new_death_rate):
        '''
        @param new_death_rate is the new death rate of the object

        Sets the death rate to have the value of the given parameter
        '''
        self.death_rate = new_death_rate
    
    def __str__(self):
        '''
        Formats the print output of the object
        '''
        
        output = super().__str__() + ("\nCoat colour: {}\nDiet: {}\nBaby Death Rate: {}%").format(self.coat_colour, self.food, self.death_rate)
        return output
