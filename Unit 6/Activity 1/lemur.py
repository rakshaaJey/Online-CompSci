import mammal

class Lemur(mammal.Mammal):

    def __init__(self, its_age, its_weight, its_breed, its_gender, its_location = "", its_coat = "", its_classification = "", grooming = "", female_role = ""):
        '''
        Constructor using age, weight, breed, gender, location, coat, classification, grooming and female role
        '''

        if its_location == "":
            its_location = "Madagascar"
        
        if its_coat == "":
            its_coat = "Fur"
        
        if its_classification == "":
            its_classification = "Prosimians"
        
        if grooming == "":
            grooming = "Using their teeth as a comb"
        
        if female_role == "":
            female_role = "Dominant role"

        super().__init__(its_age, its_weight, its_breed, its_gender)

        self.its_location = its_location
        self.its_coat = its_coat
        self.its_classification = its_classification
        self.grooming = grooming
        self.female_role = female_role
    
    #Get methods 
    def get_location(self):
        '''
        Returns the location
        '''
        return self.its_location
    
    def get_coat(self):
        '''
        Returns the coat
        '''
        return self.its_coat
    
    def get_classification(self):
        '''
        Returns the classification
        '''
        return self.its_classification
    
    def get_grooming(self):
        '''
        Returns the grooming
        '''
        return self.grooming
    
    def get_female_role(self):
        '''
        Returns the role of the female
        '''
        return self.female_role

    #Set methods
    def set_location(self, new_location):
        '''
        @param set_location is the new location of the object

        Sets the location to have the value of the given parameter
        '''
        self.its_location = new_location
    
    def set_coat(self, new_coat):
        '''
        @param new_coat is the new coat of the object

        Sets the coat to have the value of the given parameter
        '''
        self.its_coat = new_coat
    
    def set_grooming(self, new_grooming):
        '''
        @param new_grooming is the new grooming of the object

        Sets the grooming to have the value of the given parameter
        '''
        self.grooming = new_grooming
    
    def set_female_role(self, new_female_role):
        '''
        @param new_female_role is the new role of the female of the object

        Sets the role of the female to have the value of the given parameter
        '''
        self.female_role = new_female_role

    def __str__(self):
        '''
        Formats the print output of the object
        '''
        output = super().__str__()+("\nLocation: {}\nCoat: {}\nClassification: {}\nGrooming: {}\nFemale Role: {}").format(self.its_location, self.its_coat, self.its_classification, self.grooming, self.female_role)
        
        return output