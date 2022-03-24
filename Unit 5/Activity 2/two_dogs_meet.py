'''
Rakshaa Jeyarajah
25 03 2022
Creates two dogs and checks if the dogs will be friendly towards each other
'''
#imports
import dog
import time

#functions
def interaction_checker(dog_one, dog_two, aggression_one, hunger_one, aggression_two, hunger_two):
    dog_one_fight = 0
    dog_two_fight = 0

    if aggression_one > 5 or hunger_one > 5:
        dog_one_fight = 1
    if aggression_two > 5 or hunger_two > 5:
        dog_two_fight = 1
    
    if dog_one_fight == 0 and dog_two_fight == 0:
        print(dog_one, "and", dog_two, "play happily with one another")
    elif dog_one_fight == 1 and dog_two_fight == 0:
        print(dog_one, "is hostile towards", dog_two, "and", dog_two, "runs away")
    elif dog_one_fight == 0 and dog_two_fight == 1:
        print(dog_two, "is hostile towards", dog_one, "and", dog_one, "runs away")
    else:
        print(dog_one, "and", dog_two, "are fighting")

def change_values(value_to_change, initial_value, dog_name):
    change = str(input("Would you like to change the {} on {}? (YES/NO)\n".format(value_to_change, dog_name)))
    while change.upper() != "YES" and change.upper() != "NO":
        print("Invalid Input! Try again!")
        change = str(input("Would you like to change the {} on {}? (YES/NO)\n".format(value_to_change, dog_name)))
    if change.upper() == "YES":
        while True:
            try:
                if value_to_change.upper() == "AGGRESSION":
                    dog_aggression = int(input("What is the aggression of {}?\n".format(dog_name)))
                    while dog_aggression > 10 or dog_aggression < 0:
                        print("Dog aggression is on a scale of 0 - 10")
                        dog_aggression = int(input("What is the aggression of {}?\n".format(dog_name)))
                    return dog_aggression
                else:
                    dog_hunger = int(input("What is the hunger of {}?\n".format(dog_name)))
                    while dog_hunger > 10 or dog_hunger < 0:
                        print("Dog hunger is on a scale of 0 - 10")
                        dog_hunger = int(input("What is the hunger of {}?\n".format(dog_name)))
                    return dog_hunger
            except ValueError:
                print("Invalid Input")
            else:
                break
    else:
        return initial_value

#main line
while True:
    #Asks the user for the name of dog one
    while True:
        try:
            dog_one_name = str(input("What is the name of dog one?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
  
    #Asks the user for the breed of dog one
    while True:
        try:
            dog_one_breed = str(input("What is the breed of dog one?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
   #Asks the user for the name of dog two
    while True:
        try:
            dog_two_name = str(input("What is the name of dog two?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
  
    #Asks the user for the breed of dog two
    while True:
        try:
            dog_two_breed = str(input("What is the breed of dog two?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    dog_one = dog.Dog(dog_one_name, dog_one_breed, 0, 0)
    dog_two = dog.Dog(dog_two_name, dog_two_breed, 0, 0)

    print(dog_one.get_name(), "stats:", dog_one)
    time.sleep(5)
    print()
    print(dog_two.get_name(), "stats:", dog_two)
    time.sleep(5)
    print()

    dog_one.set_aggression(change_values("aggression", dog_one.get_aggression(), dog_one.get_name()))
    dog_one.set_hunger(change_values("hunger", dog_one.get_hunger(), dog_one.get_name()))
    dog_two.set_aggression(change_values("aggression", dog_two.get_aggression(), dog_two.get_name()))
    dog_two.set_hunger(change_values("hunger", dog_two.get_hunger(), dog_two.get_name()))
    
    interaction_checker(dog_one.get_name(), dog_two.get_name(), dog_one.get_aggression(), dog_one.get_hunger(), dog_two.get_aggression(), dog_two.get_hunger())
        
    #Asks the user if they want the program to be run again
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break