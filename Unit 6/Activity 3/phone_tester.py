'''
Rakshaa Jeyarajah
07 April 2022
Allows the user to make a phone
'''
#imports
import cell_phone

#functions

#main line

new_phone = cell_phone.CellPhone()

while True:
    print("Make your own phone!")
    
    #asks user for data about their phone
    owner = str(input("Who is the owner of this phone?\n"))
    new_phone.set_owner(owner)

    carrier = str(input("What is the carrier?\n"))
    new_phone.set_carrier(carrier)

    phone_type = str(input("What type of phone is this?\n"))
    new_phone.set_phone_type(phone_type)


    while True:
        try:
            phone_speed = int(input("What is the speed of the phone?\n"))

            while phone_speed <= 0:
                print("Invalid Input")
                phone_speed = int(input("What is the speed of the phone?\n"))
                
            new_phone.set_speed(phone_speed)
            
        except ValueError:
            print("Invalid Input")
            
        else:
            break
        
    while True:
        try:
            memory = int(input("What is the memory of the phone?\n"))

            while memory <= 0:
                print("Invalid Input")
                memory = int(input("What is the memory of the phone?\n"))
                
            new_phone.set_memory(memory)
            
        except ValueError:
            print("Invalid Input")
            
        else:
            break
        
    while True:
        try:
            number_of_apps = int(input("What is the number of apps of the phone?\n"))

            while number_of_apps <= 0:
                print("Invalid Input")
                number_of_apps = int(input("What is the number of apps of the phone?\n"))
                
            new_phone.set_number_of_apps(number_of_apps)
            
        except ValueError:
            print("Invalid Input")
            
        else:
            break

    print("Your phone:")
    print(new_phone)
    
    #Asks the user if they want the program to be run again
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye!")
