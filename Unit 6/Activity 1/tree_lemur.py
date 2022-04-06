import lemur
import random

class TreeLemur(lemur.Lemur):

    def __init__(self, its_age = 0, its_weight = 0, its_breed = "", its_gender = "", its_location = "", its_coat = "", its_classification = "", grooming = "", female_role = "", group_size = "", food = "", mane = ""):
        '''
        Constructor using age, weight, breed, gender, location, coat, classification, grooming, female role, group size, food and mane
        '''
        if group_size == "":
            group_size = "Large Groups"
        
        if food == "":
            food = "Fruits"
        
        if mane == "":
            mane = "Red"

        if its_breed == "":
            its_breed = "Tree Lemur"
        
        if its_age == 0:
            its_age = random.randint(0, 16)
        
        if its_weight == 0:
            its_weight = random.uniform(1.0, 10.1)

        super().__init__(its_age, its_weight, its_breed, its_gender, its_location, its_coat, its_classification, grooming, female_role)

        self.group_size = group_size
        self.food = food
        self.mane = mane
    
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

    def __str__(self):
        '''
        Formats the print output of the object
        '''

        output = super().__str__() + ("\nPack Size: {}\nDiet: {}\nMane: {}").format(self.group_size, self.food, self.mane)
        return output
