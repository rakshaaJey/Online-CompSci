'''
Rakshaa Jeyarajah
22 03 2022
Uses the car class to make cars!
'''
#imports
import car
import time

#functions

#main line
while True:
    #Asks the user for the car make
    while True:
        try:
            car_make = str(input("What is the car make?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
  
    #Asks the user for car model
    while True:
        try:
            car_model = str(input("What is the car model?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for car year
    while True:
        try:
            car_year = int(input("What is the car year?\n"))
            while car_year < 1908:
                print("There aren't any cars from this time! Try again!")
                car_year = int(input("What is the car year?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for cars price
    while True:
        try:
            car_price = int(input("What is the price of the car?\n"))
            while car_price < 0:
                print("Invalid Input")
                car_price = int(input("What is the price of the car?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for cars colour
    while True:
        try:
            car_colour = str(input("What is the colour of the car?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for how many wheels teh car has
    while True:
        try:
            car_wheels = int(input("How many wheels does the car have?\n"))
            while car_wheels < 0:
                print("Invalid Input")
                car_wheels = int(input("How many wheels does the car have?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    user_car = car.Car(car_make, car_model, car_year, car_price, car_colour, car_wheels)
    generated_car = car.Car()

    print("\nYour Car", user_car)
    time.sleep(5)
    print()
    print("Generated Car", generated_car)
    time.sleep(5)
    print()
        
    #Asks the user if they want the program to be run again
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye!")