#imports
import math

#functions

#main line

#variables
userNumber = float(input("Please input a number: "))

numberSquareRoot = math.sqrt(userNumber)
numberSquared = math.pow(numberSquareRoot, 2)
roundError = userNumber - numberSquared

#prints what is required by the assignment
print('The square root of your number is: ' + str(numberSquareRoot))
print(str(numberSquareRoot) + ' squared is: ' + str(numberSquared))
print('The round off error is: ' + str(roundError))

