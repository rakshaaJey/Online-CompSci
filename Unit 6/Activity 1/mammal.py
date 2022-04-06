import random

class Mammal(object):
  
    #Constructor
    def __init__(self,its_age = 0,its_weight = 0,its_breed = "", its_gender = ""):
        '''
        Constructor using age, weight, breed and gender 
        '''
        if its_gender == "":
            gender = ["Male", "Female"]
            choice = random.randint(0, 1)
            its_gender = gender[choice]

        self.its_age = its_age
        self.its_weight = its_weight
        self.its_breed = its_breed
        self.its_gender = its_gender
   
    #Get methods 
    def get_age(self):
        '''
        Returns the age
        '''
        return self.its_age
        
    def get_weight(self):
        '''
        Returns the weight
        '''
        return self.its_weight
        
    def get_breed(self):
        '''
        Returns the breed
        '''
        return self.its_breed

    def get_gender(self):
        '''
        Returns the gender
        '''
        return self.its_gender

        
    #Set methods
    def set_age(self,new_age):
        '''
        @param new_age is the new age of the object

        Sets the age to have the value of the given parameter
        '''
        self.its_age = new_age

    def set_weight(self, new_weight):
        '''
        @param new_weight is the new weight of the object

        Sets the weight to have the value of the given parameter
        '''
        self.its_weight = new_weight
    
    def set_breed(self, new_breed):
        '''
        @param new_breed is the new breed of the object

        Sets the breed to have the value of the given parameter
        '''
        self.its_breed = new_breed
    
    def set_gender(self, new_gender):
        '''
        @param new_gender is the new gender of the object

        Sets the gender to have the value of the given parameter
        '''
        self.its_gender = new_gender
    
    def __str__(self):
        '''
        Formats the print output of the object
        '''

        output = ("{}:\nAge: {} years old\nWeight: {} ilbs\nGender: {}").format(self.its_breed, self.its_age, self.its_weight, self.its_gender)
        return output
