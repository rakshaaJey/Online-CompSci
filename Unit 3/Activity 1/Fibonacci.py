'''
Rakshaa Jeyarajah
February 28 2022
Prints out an index (dictated by the user) of the fibonacci sequence
'''
#input

#function
'''
@param fibonacci_index is the index of the fibonacci sequence that the function will find
Finds the value of teh fibonacci sequence at the desired index
'''
def fibonacci_sequence(fibonacci_index):
    if (fibonacci_index <= 1):
        return fibonacci_index
    else:
        return fibonacci_sequence(fibonacci_index - 1) + fibonacci_sequence(fibonacci_index - 2)

#main line
while True:
    #Recives user input and checks if the user input is valid to use. If not the program prompts the user to reinput a value
    user_input = int(input("The first few numbers are listed as followed...\n"+ 
        "1, 1, 2, 3, 5, 8, 13, 21, 34, ...\nWhat fibonacci term would you like to see?\n"))
    while user_input <= 0:
        print("Invalid input! Try again.")
        user_input = int(input("The first few numbers are listed as followed...\n"+ 
            "1, 1, 2, 3, 5, 8, 13, 21, 34, ...\nWhat fibonacci term would you like to see?\n"))
    
    while True:
        try:
            print("Element at", user_input, "of the fibonacci sequence is", fibonacci_sequence(user_input))
        except ValueError:
            print("Invalid input! Try again.")
        else:
            break
    
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye")
    
