#imports
import math

#functions
def surfaceArea(length, width, height):
    return (length * width) + (length * math.sqrt(math.pow((width/2), 2) + math.pow(height, 2))) + (width * math.sqrt(math.pow((length/2), 2) + math.pow(height, 2)))

#main line
userLength = float(input('What is the length of the pyramid?\n'))
userWidth = float(input('What is the width of the pyramid?\n'))
userHeight = float(input('What is the height of the pyramid?\n'))

print('The surface area of the pyramid is ' + str(surfaceArea(userLength, userWidth, userHeight)) + ' units squared')