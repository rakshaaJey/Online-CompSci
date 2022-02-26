'''
'''
#input

#function
def factorial(num):
    factorial = 1
    for counter in range (0, num):
        factorial = (num - counter) * factorial
    
    return factorial
    
def combination_equation(n, r):
    return factorial(n)/ (factorial(r) * factorial(n - r))

#main line
while True:
    print("This program will calculate the number of ways to choose r different objects from a set of", 
        " n objects")
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
    
    while True:
        try:
            print("There are", combination_equation(user_input_n, user_input_r), "ways to choose", user_input_r, 
                "objects from a set of", user_input_n, "objects")
            break
        except ValueError:
                print("Invalid input! Try again.")
    
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break