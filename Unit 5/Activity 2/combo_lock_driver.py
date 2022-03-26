'''
Rakshaa Jeyarajah
25 03 2022
DESCRIPTION
'''
#imports
import combo_lock

#functions
def check_combo(locker_combination, lowest_num, highest_num):
    '''
    @param locker_combination is the combination of the lock
    @param lowest_num is the lowest number of the lock
    @param highest_num is the highest number of the lock

    Asks the user to guess the combination of the lock and prints if they got the combo right
    The user only has three guesses and if all three guesses are used the combination will be printed
    '''
    for counter in range(0, 3):
        guesses = []
        for counter_two in range(0, 3):
            while True:
                try:
                    guess = int(input("What is {} number in the lock combination?\n".format(counter_two + 1)))
                    while guess > highest_num or guess < lowest_num:
                        print("The lock only has numbers between {} and {}!".format(lowest_num, highest_num))
                        guess = int(input("What is {} number in the lock combination?\n".format(counter_two + 1)))
                except ValueError:
                    print("Invalid Input!")
                else:
                    break
            
            guesses.append(guess)

        if guesses != locker_combination and counter == 2:
            print("Incorrect combination!\nThe correct combination is", locker_combination)
        elif guesses == locker_combination:
            print("You got the combination correct!")
            break
        else:
            print("Incorrect Combination!\n")

#main line
while True:
    #Asks the user for the first number of the lock
    while True:
        try:
            first_number = int(input("What is the first number of the combination?\n"))
            while first_number < 0:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for the second number of the lock
    while True:
        try:
            second_number = int(input("What is the second number of the combination?\n"))
            while second_number < 0:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    #Asks the user for the three number of the lock
    while True:
        try:
            third_number = int(input("What is the third number of the combination?\n"))
            while third_number < 0:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
        else:
            break

    lock_one = combo_lock.Combo_Lock(first_number, second_number, third_number)
    sorted_combo = lock_one.get_locker_combination()
    sorted_combo.sort()

    #User guesses the combo of the lock they made
    check_combo(lock_one.get_locker_combination(), 0, sorted_combo[2] + 10)

    #User guesses the combo of the randomy generated lock
    lock_two = combo_lock.Combo_Lock()
    print("\nNow its time to guess the combination of a randomly generated lock\nNote that this lock contains",
        "numbers from 0 to 3")
    check_combo(lock_two.get_locker_combination(), 0, 3)

    #Asks the user if they want the program to be run again
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye!")
