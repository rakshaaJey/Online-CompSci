'''
Rakshaa Jeyarajah
15 February 2022
This program calculates the resistance of resistors of certain colours when together
'''
#imports
import math

#functions 
'''
@param string string that will be sorted through
This function finds the first colour that within a string and returns 
a string with the first colour that is found
'''
def colour_finder(string):
    colour = ""
    for counter in range(0, len(string), 1):
        match colour.upper():
            case "BLACK":
                break
            case "BROWN":
                break
            case "RED":
                break
            case "ORANGE":
                break
            case "YELLOW":
                break
            case "GREEN":
                break
            case "BLUE":
                break
            case "GREY":
                break
            case "VIOLET":
                break
            case "WHITE":
                break
        
        colour += string[counter]
    
    return colour

'''
@param resistor_order is a string containing the order of the resistors
This function separates each colour found in the string and puts them into an array. Then the function will return
the array
'''
def string_separator(resistor_order):
    resistors = resistor_order.replace("-", '')
    colour_array =  [0, 0, 0]
    for counter in range(0, 3, 1):
        colour_array[counter] = colour_finder(resistors)
        resistors = resistors.replace(colour_array[counter], "")
    
    return colour_array
    
'''
@param colour_array is an array containing the colour of the resistors in order
This calculates the resistance (in ohms) of the resistors
'''
def ohms_calculator(colour_array):
    calculation_values = [0, 0, 0]
    resistor_values = [["BLACK", "0"], ["BROWN", "1"], ["RED", "2"], ["ORANGE", "3"], 
        ["YELLOW", "4"], ["GREEN", "5"], ["BLUE", "6"], ["GREY", "7"], ["VIOLET", "8"],
        ["WHITE", "9"]]
    
    for counter_one in range(0, 3, 1):
        for counter_two in range(0, 10, 1):
            if resistor_values[counter_two][0] == colour_array[counter_one].upper():
                calculation_values[counter_one] = int((resistor_values[counter_two][1]))
                break
    
    ohms =  ((calculation_values[0]*10) + calculation_values[1]) * math.pow(10, calculation_values[2])
    return ohms

#main line
user_input = str(input("What is your resistor colour code? \nUse hyphens (-) to separate the colours.\nExample: RED-BLUE-BLACK\n"))
print("you have entered: ", user_input)
print("The value of the resistor is: ", ohms_calculator((string_separator(user_input.upper()))), " \u03A9")
