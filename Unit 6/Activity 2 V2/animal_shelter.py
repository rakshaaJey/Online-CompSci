import dog
import cat

class AnimalShelter(object):
    '''
    The animal shelter will contain animals stored in an bytearray
    '''
    
    def __init__(self):
        '''
        Initialize the animal shelter
        '''

        #List of dogs
        self.animal_list = []

        self.fill_list()
    
    def fill_list(self):
        '''
        A function to fill the animal shelter with animals
        '''
        num_dog = int(input("How many dogs would you like to create? "))
    
        for i in range (0, num_dog):
            self.add_dog()
        
        num_cat = int(input("How many cats would you like to create? "))
        
        for i in range (0, num_cat):
            self.add_cat()

    def shelter_cost(self):
        '''
        Calculates the cost of running the animal shelter based on the number of animals in the shelter
        '''
        daily_cost = 15 * len(self.animal_list)
        yearly_cost = 365 * daily_cost
        monthly_cost = yearly_cost / 12

        print("Daily cost: $" + str(daily_cost) + "\nMonthly cost on average: $" + str(monthly_cost) + "\nYearly cost: $" + str(yearly_cost))
    
    def add_dog(self, index = -1):
        '''
        Adds a dog to the animal shelter and adds its data to the list of animals
        '''
        print("Animal #" + str(len(self.animal_list) + 1))

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

        self.animal_list.append(dog.Dog(name, age, breed))
    
    def add_cat(self):
        '''
        Adds a cat to the animal shelter and adds its data to the list of animals
        '''
        print("Animal #" + str(len(self.animal_list) + 1))

        name = str(input("What is the name of the cat?\n"))

        while True:
            try:
                age = int(input("What is the age of the cat?\n"))
                while age < 0:
                    print("Invalid Input")
                    age = int(input("What is the age of the cat?\n"))
            except ValueError:
                print("Invalid Input")
            else:
                break
        
        breed = str(input("What is the breed of the cat?\n"))

        self.animal_list.append(cat.Cat(name, age, breed))

    def remove_animal(self):
        '''
        Allows a dog to be adopted and then removed from the list of animals
        '''
        print(self.__str__())

        while True:
                try:
                    animal_index = int(input("Which dog would you like to remove?\n"))
                    while animal_index < 1:
                        print("Invalid Input")
                        animal_index = int(input("Which dog would you like to remove?\n"))
                    
                    animal_index -= 1

                    print(self.animal_list[animal_index].__str__(),"was adopted and sent to a nice home!")
                    self.animal_list.pop(animal_index)

                except IndexError:
                    print("Invalid Input")
                
                except ValueError:
                    print("Invalid Input")

                else:
                    break
        
    def edit_animal(self):
        '''
        Alows the user to change the properties of an animal in the animal list
        '''

        print(self.__str__())

        while True:
            try:
                animal_index = int(input("Which animal would you like to edit?\n"))
                while animal_index < 1 or animal_index > len(self.animal_list):
                    print("Invalid Input")
                    animal_index = int(input("Which animal would you like to edit?\n"))
                        
                animal_index -= 1

                while True:
                    try:
                        animal_type = int(input("What type of animal would you like to make?\n1 - Cat\n2 - Dog\n"))
                        while animal_type < 1 and animal_type > 2:
                            print("Invalid Input")
                            animal_type = int(input("What type of animal would you like to make?\n1 - Cat\n2 - Dog\n"))
                        
                    except ValueError:
                        print("Invalid Input")
                        
                    else:
                        break

            except ValueError:
                print("Invalid Input")

            else:
                break
        
        if animal_type == 1:
            print("Animal #" + str(len(self.animal_list) + 1))

            name = str(input("What is the name of the docatg?\n"))

            while True:
                try:
                    age = int(input("What is the age of the cat?\n"))
                    while age < 0:
                        print("Invalid Input")
                        age = int(input("What is the age of the cat?\n"))
                except ValueError:
                    print("Invalid Input")
                else:
                    break
        
            breed = str(input("What is the breed of the cat?\n"))

            self.animal_list[animal_index] = cat.Cat(name, age, breed)
        
        else:
            print("Animal #" + str(len(self.animal_list) + 1))

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

            self.animal_list[animal_index] = dog.Dog(name, age, breed)

    def __str__(self):
        '''
        Returns the properties of the library
        '''
        output = "\nThe Shelter Contains:\n\n"
        
        for i in range (0,len(self.animal_list)):
          output += ("Animal #"+str(i + 1)+"\n")
          output +=  (self.animal_list[i].__str__() + "\n")

        return output