#imports
import math

#functions

#main line
userNumber = float(input("Please input a number: "))

numberSquareRoot = math.sqrt(userNumber)
numberSquared = math.pow(numberSquareRoot, 2)
roundingError = userNumber - numberSquared

'''
Prints the square root of the number, the square root of the number to the powewr of two and the round off error
'''
print('The square root of your number is: ', numberSquareRoot)
print(numberSquareRoot, ' squared is: ', numberSquared)
print('The round off error is: ', roundingError)