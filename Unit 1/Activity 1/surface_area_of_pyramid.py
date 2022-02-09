'''
Rakshaa Jeyarajah
08 February 2022
This program finds the surface area of a pyramid
'''
#imports
import math

#functions
'''
@param length represents the length of the pyramid
@param width represents the width of the pyramid
@param height represents the height of the pyramid
This function returns the surface area of a pyramid
'''
def surfaceArea(length, width, height):
    return (length * width) + (length * math.sqrt(math.pow((width/2), 2) + math.pow(height, 2))) + (width * math.sqrt(math.pow((length/2), 2) + math.pow(height, 2)))

#main line
'''
Asks the user for the length, width, and height of a pyramid and prints the surface area of the pyramid. 
'''
user_length = float(input('What is the length of the pyramid?\n'))
user_width = float(input('What is the width of the pyramid?\n'))
user_height = float(input('What is the height of the pyramid?\n'))

'''
Outputs the surface area
'''
print('The surface area of the pyramid is ', surfaceArea(user_length, user_width, user_height), ' units squared')