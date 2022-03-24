#imports
import random

class Car(object):
    
    def __init__(self, car_make = "", car_model = "", car_year = 0, car_price = 0, car_colour = "", number_of_wheels = -1):
        '''
        @param car_make is the make of the car
        @param car_model is the cars model
        @param car_year is the year the car was made
        @param car_price is the price of the car
        @param car_colour is the colour of the car
        @param number_of_wheels is the number of wheels the car has

        Initializes the car object and adds the properties
        '''

        #Lists of possible models, makes and colours
        car_model_list = [["Audi", "A3", "A4", "R8", "A1", "A2"], ["BMW", "i3", "i8", "3 Series", "5 Series", "X5"], 
            ["Chevrolet", "Corvette", "Cruze", "Impala", "Malibu"], ["Ford", "F Series", "Explorer", "Fiesta", "Mustang"],
            ["Honda", "Civic", "Fit", "CR-V", "Accord"], ["Nissan", "Leaf", "Maxima", "Micra", "Z-cars"],
            ["Toyota", "Corolla", "Prius", "RAV4", "Mirai"]]
        colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Indigo", "Pink", "White", "Grey", "Black"]
        
        #If both the car make and car model are unknown, the program with chose a random make and assign an appropriate random model
        if car_make == "" and car_model == "":
            random_make = random.randint(0, len(car_model_list) - 1)
            random_model = random.randint(1, len(car_model_list[random_make]) - 1)

            car_make = car_model_list[random_make][0]
            car_model = car_model_list[random_make][random_model]
        
        #Generates a random make
        if car_make == "":
            random_make = random.randint(0, len(car_model_list) - 1)
            car_make = car_model_list[random_make][0]
        
        #Check if the car make matches any in the list. If it does an appropriate model will be assigned. If not
        #a random model will be chosen
        if car_model == "":
            for counter in range (0, len(car_model_list)):
                if car_make.upper() == car_model_list[counter][0].upper():
                    random_model = random.randint(1, len(car_model_list[counter]) - 1)
                    car_model = car_model_list[counter][random_model]
                    break
            if counter == len(car_model_list):
                random_make = random.randint(0, len(car_model_list) - 1)
                random_model = random.randint(1, len(car_model_list[random_make]) - 1)

                car_model = car_model_list[random_make][random_model]
        
        if car_year == 0:
            car_year = random.randint(1908, 2022)

        if car_price == 0:
            car_price = random.randint(2500, 70000000)
        
        if car_colour == "":
            random_num = random.randint(0, len(colours) - 1)
            car_colour = colours[random_num]

        if number_of_wheels == -1:
            number_of_wheels = random.randint(0, 4)    

        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.car_price = car_price
        self.car_colour = car_colour
        self.number_of_wheels = number_of_wheels
    
    def honk(self):
        '''
        Makes the car honk
        '''
        print("HONK!")
    
    def beep(self):
        '''
        Makes the car go beep beep
        '''
        print("BEEP BEEP!")

    def __str__(self):
        '''
        Returns the properties of the car
        '''
        return '\nMake Name: {}\nModel Name: {} \nYear: {} \nPrice: ${} \nColour: {} \nNumber of Wheels: {}'.format(self.car_make, self.car_model, self.car_year,
            self.car_price, self.car_colour, self.number_of_wheels)