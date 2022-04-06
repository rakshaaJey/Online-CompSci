'''
Rakshaa Jeyarajah
03 30 2022
Allows the user to create a lemur database
'''
#imports
import tree_lemur, desert_lemur, jungle_lemur, time

#functions

#main line
while True:
    lemur_list = []

    #Asks the user for the number of lemurs that will be in the database
    while True:
        try:
            number_of_lemurs = int(input("How many lemurs do you want to add to the list?\n"))
            while number_of_lemurs <= 0:
                print("Invalid Input!")
                number_of_lemurs = int(input("How many lemurs do you want to add to the list?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for the type of lemur
    for counter in range(0, number_of_lemurs):
        while True:
            try:
                lemur_number = int(input("Please enter the type of lemur to add:\n1. Tree Lemur\n2. Desert Lemur\n3. Jungle Lemur\n"))
                while lemur_number < 1 or lemur_number > 3:
                    print("Invalid Input!")
                    lemur_number = int(input("Please enter the type of lemur to add:\n1. Tree Lemur\n2. Desert Lemur\n3. Jungle Lemur\n"))
            except ValueError:
                print("Invalid Input")
            else:
                lemur_list.append(lemur_number)
                break
    
    #Prints the database of lemurs
    print()

    for counter in range(0, number_of_lemurs):
        if lemur_list[counter] == 1:
            print("Creating Tree Lemur.")
        elif lemur_list[counter] == 2:
            print("Creating Desert Lemur.")
        else:
            print("Creating Jungle Lemur.")
        time.sleep(3)

    print("-------------------------------------------")
    for counter in range(0, number_of_lemurs):
        if lemur_list[counter] == 1:
            lemur_one = tree_lemur.TreeLemur()
            print(lemur_one)
        elif lemur_list[counter] == 2:
            lemur_two = desert_lemur.DesertLemur()
            print(lemur_two)
        else:
            lemur_three = jungle_lemur.JungleLemur()
            print(lemur_three)
        
        print()
        time.sleep(3)
    
    #Asks the user if they want the program to be run again
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye!")

