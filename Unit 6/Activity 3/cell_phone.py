class CellPhone(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.__owner = "owner"
        self.__carrier = "carrier"
        self.__phone_type = "phone_type"
        self.__speed = 0
        self.__memory = 0
        self.__number_of_apps = 0
    
    def set_owner(self, new_owner):
        '''
        @param new_owner is the new owner of the object

        Sets the owner to have the value of the given parameter
        '''
        self.__owner = new_owner
    
    def set_carrier(self, new_carrier):
        '''
        @param new_carrier is the new carrier of the object

        Sets the carrier to have the value of the given parameter
        '''
        self.__carrier = new_carrier
    
    def set_phone_type(self, new_phone_type):
        '''
        @param new_phone_type is the new phone type of the object

        Sets the phone type to have the value of the given parameter
        '''
        self.__phone_type = new_phone_type
    
    def set_speed(self, new_speed):
        '''
        @param new_speed is the new speed of the object

        Sets the speed to have the value of the given parameter
        '''
        self.__speed = new_speed

    def set_memory(self, new_memory):
        '''
        @param new_memory is the new memory of the object

        Sets the memory to have the value of the given parameter
        '''
        self.__memory = new_memory
    
    def set_number_of_apps(self, new_number_of_apps):
        '''
        @param new_number_of_apps is the new number of apps of the object

        Sets the number of apps to have the value of the given parameter
        '''
        self.__number_of_apps = new_number_of_apps

    def __str__(self):
        '''
        Returns the properties of the phone
        '''

        output = '{} Phone:\nCarrier - {}\nPhone Type - {}\nSpeed - {}Ghz\nMemory - {}Gb\nNumber of Apps - {}'.format(self.__owner, 
            self.__carrier, self.__phone_type, self.__speed, self.__memory, self.__number_of_apps)

        return output