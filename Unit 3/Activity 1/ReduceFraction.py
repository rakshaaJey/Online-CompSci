'''
Rakshaa Jeyarajah
February 28 2022
Reduces a fraction 
'''
#input

#function
'''
@param number_one is the first number
@param number_two is the second number
Finds the greatest common denominator of 2 numbers
'''
def greatest_common_denominator_finder(number_one, number_two):
    if number_two == 0:
        return number_one
    else:
        return greatest_common_denominator_finder(number_two, number_one % number_two)

'''
@param numerator is the numerator of the fraction
@param denominator is the denominator of the fraction
Prints the reduced fraction
'''
def fraction_reducer(numerator, denominator):
    gcd = greatest_common_denominator_finder(numerator, denominator)
    print("The fraction", numerator,'/', denominator, "can be reduced to", numerator/gcd, '/', denominator/gcd)

#main line
while True:
    #Recives user input and checks if the user input is valid to use. If not the program prompts the user to reinput a value
    while True:
        try:
            numerator = int(input("What is the numerator of your fraction? "))
            denominator = int(input("What is the denominator of your fraction? "))
        except ValueError:
            print("Invalid Input! Try again")
        else:
            break
    fraction_reducer(numerator, denominator)

    #Allows the user to rerun the program
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break
print("Thank you for using the fraction reducer. Good bye!")
