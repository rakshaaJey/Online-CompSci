import lemur
import random

class JungleLemur(lemur.Lemur):

    def __init__(self, its_age = 0, its_weight = 0, its_breed = "", its_gender = "", its_location = "", its_coat = "", its_classification = "", grooming = "", female_role = "", group_size = "", food = "", mane = "", coat_colours = ""):
        '''
        Constructor using age, weight, breed, gender, location, coat, classification, grooming, female role, group size, food, mane and coat colour
        '''

        if group_size == "":
            group_size = "Small Groups"
        
        if food == "":
            food = "Mice, Snails and Insects"
        
        if mane == "":
            mane = "None"

        if its_breed == "":
            its_breed = "Jungle Lemur"
        
        if its_age == 0:
            its_age = random.randint(0, 17)
        
        if its_weight == 0:
            its_weight = random.uniform(1.0, 5.6)
        
        if coat_colours == "":
            coat_colours = "Black or Bue"

        super().__init__(its_age, its_weight, its_breed, its_gender, its_location, its_coat, its_classification, grooming, female_role)

        self.group_size = group_size
        self.food = food
        self.mane = mane
        self.coat_colours = coat_colours
    
    #Get methods
    def get_group_size(self):
        '''
        Returns the group size
        '''
        return self.group_size
    
    def get_food(self):
        '''
        Returns the food
        '''
        return self.food
    
    def get_mane(self):
        '''
        Returns the mane
        '''
        return self.mane
    
    def get_coat_colours(self):
        '''
        Returns the coat colours
        '''
        return self.coat_colours
    
    #Set methods
    def set_group_size(self, new_group_size):
        '''
        @param new_group_size is the new group size of the object

        Sets the group size to have the value of the given parameter
        '''
        self.group_size = new_group_size
    
    def set_food(self, new_food):
        '''
        @param new_food is the new food of the object

        Sets the food to have the value of the given parameter
        '''
        self.food = new_food
    
    def set_mane(self, new_mane):
        '''
        @param new_mane is the new mane of the object

        Sets the mane to have the value of the given parameter
        '''
        self.mane = new_mane
    
    def set_coat_colour(self, new_coat_colours):
        '''
        @param new_coat_colours is the coat colours of the object

        Sets the coat colours to have the value of the given parameter
        '''
        self.coat_colours = new_coat_colours
    
    def __str__(self):
        '''
        Formats the print output of the object
        '''

        output = super().__str__() + ("\nPack Size: {}\nDiet: {}\nMane: {}\nCoat Colour: {}").format(self.group_size, self.food, self.mane, self.coat_colours)
        return output
