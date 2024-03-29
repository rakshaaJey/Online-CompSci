import dog

class AnimalShelter(object):
    '''
    The animal shelter will contain dogs stored in an bytearray
    '''
    
    def __init__(self):
        '''
        Initialize the animal shelter
        '''

        #List of dogs
        self.dog_list = []

        self.fill_list()
    
    def fill_list(self):
        '''
        A function to fill the animal shelter with dogs
        '''
        num_dog = int(input("How many dogs would you like to create? "))
    
        for i in range (0, num_dog):
            self.add_dog()

    def shelter_cost(self):
        '''
        Calculates the cost of running the animal shelter based on the number of dogs in the shelter
        '''
        daily_cost = 15 * len(self.dog_list)
        yearly_cost = 365 * daily_cost
        monthly_cost = yearly_cost / 12

        print("Daily cost: $" + str(daily_cost) + "\nMonthly cost on average: $" + str(monthly_cost) + "\nYearly cost: $" + str(yearly_cost))
    
    def add_dog(self):
        '''
        Adds a dog to the animal shelter and adds its data to the list of dogs
        '''
        print("\nDog #" + str(len(self.dog_list) + 1))

        name = str(input("What is the name of the dog?\n"))

        while True:
            try:
                age = int(input("What is the age of the dog?\n"))
                while age < 0:
                    print("Invalid Input")
                    age = int(input("What is the age of the dog?\n"))
            except ValueError:
                print("Invalid Input")
            else:
                break
        
        breed = str(input("What is the breed of the dog?\n"))

        self.dog_list.append(dog.Dog(name, age, breed))

        print("Successfully added a dog.")

    def remove_dog(self):
        '''
        Allows a dog to be adopted and then removed from the list of dogs
        '''
        print(self.__str__())

        while True:
                try:
                    dog_index = int(input("Which dog would you like to remove?\n"))
                    while dog_index < 1:
                        print("Invalid Input")
                        dog_index = int(input("Which dog would you like to remove?\n"))
                    
                    dog_index -= 1

                    print(self.dog_list[dog_index].__str__(),"was adopted and sent to a nice home!")
                    self.dog_list.pop(dog_index)

                except IndexError:
                    print("Invalid Input")
                else:
                    break

    def __str__(self):
        '''
        Returns the properties of the library
        '''
        output = "\nThe Shelter Contains:\n\n"
        
        for i in range (0,len(self.dog_list)):
          output += ("Dog #"+str(i + 1)+"\n")
          output +=  (self.dog_list[i].__str__() + "\n")

        return output