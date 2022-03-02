'''
Rakshaa Jeyarajah
February 28 2022
Takes user input and puts it into the combination equation
'''
#input

#function
'''
@param num is the number whose factorial will be found
Finds the factorial of this number
'''
def factorial(num):
    if (num <= 1):
        return 1
    else:
        return num*factorial(num-1)

'''
@param n is the total number of objects in the set
@param r is the number of choosing objects from the set
Calculates the answer of the combination equation 
'''
def combination_equation(n, r):
    return factorial(n)/ (factorial(r) * factorial(n - r))

#main line
while True:
    print("This program will calculate the number of ways to choose r different objects from a set of", 
        " n objects")
    
    #Recives user input and checks if the user input is valid to use. If not the program prompts the user to reinput a value
    while True:
        try:
            user_input_n = int(input("How many objects would you like to choose? "))
            user_input_r = int(input("How many objects are there to choose from? "))
            while True:
                if user_input_n <= user_input_r:
                    print("The number of objects that you choose must be larger than the number of objects to", 
                    " choose from")
                elif user_input_n <= 0 or user_input_r <= 0:
                    print("Values cant be smaller than or equal to 0")
                else:
                    break
                user_input_n = int(input("How many objects would you like to choose? "))
                user_input_r = int(input("How many objects are there to choose from? "))
            print("There are", combination_equation(user_input_n, user_input_r), "ways to choose", user_input_r, 
                "objects from a set of", user_input_n, "objects")
        except ValueError:
            print("Invalid input! Try again.")
        else:
            break
    
    #Allows the user to rerun the program
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break
print("Good bye!")