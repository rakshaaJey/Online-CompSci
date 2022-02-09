'''
Rakshaa Jeyarajah
08 February 2022
This program outputs the round off error that occurs in code
'''
#imports
import math

#functions

#main line
'''
Asks the user for a number and finds the square root of the number, the square root of the number to the power of two, and the round off error
'''
user_number = float(input("Please input a number: "))

number_square_root = math.sqrt(user_number)
number_squared = math.pow(number_square_root, 2)
rounding_error = user_number - number_squared

'''
Prints the square root of the number, the square root of the number to the power of two and the round off error
'''
print('The square root of your number is: ', number_square_root)
print(number_square_root, ' squared is: ', number_squared)
print('The round off error is: ', rounding_error)