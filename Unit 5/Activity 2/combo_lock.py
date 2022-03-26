import random

class Combo_Lock(object):
    
    def __init__(self, first_number = -1, second_number = -1, third_number = -1):
        if first_number == -1:
            first_number = random.randint(0, 3)
        if second_number == -1:
            second_number = random.randint(0, 3)
        if third_number == -1:
            third_number = random.randint(0, 3)
        
        self.first_number = first_number
        self.second_number = second_number
        self.third_number = third_number
    
    def get_first_number(self):
        '''
        Returns the first number of the lock combo
        '''
        return self.first_number
    
    def get_second_number(self):
        '''
        Returns the second number of the lock combo
        '''
        return self.second_number
    
    def get_third_number(self):
        '''
        Returns the thrid number of the lock combo
        '''
        return self.third_number
    
    def get_locker_combination(self):
        '''
        Returns the lock combination
        '''
        array = []
        array.append(self.first_number)
        array.append(self.second_number)
        array.append(self.third_number)
        return array
    
    def open_lock(self):
        '''
        Opens the lock
        '''
        print("*Click* The lock opened!")

    def __str__(self):
        '''
        Returns the properties of the car
        '''
        return 'Lock Combination: {}, {}, {}'.format(self.first_number, self.second_number, self.third_number)