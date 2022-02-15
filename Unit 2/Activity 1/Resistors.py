'''
Rakshaa Jeyarajah
15 February 2022

'''
#imports

#functions 
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
            case "GREY":
                break
            case "BLUE":
                break
            case "VIOLET":
                break
            case "WHITE":
                break
        
        colour += string[counter]
    
    return colour


def string_separator(resistor_order):
    resistor_order.replace("-", "")
    colour_array = []
    for counter in range(0, 3, 1):
        colour_array[counter] = colour_finder(resistor_order)
        resistor_order.replace(colour_array[counter], "")
    
    return colour_array
    

def ohms_calculator(colour_array):
    calculation_values = []
    resistor_values = [["BLACK", "0"], ["BROWN", "1"], ["RED", "2"], ["ORANGE", "3"], 
        ["YELLOW", "4"], ["GREEN", "5"], ["GREY", "6"], ["BLUE", "7"], ["VIOLET", "8"],
        ["WHITE", "9"]]
    
    for counter_one in range(0, 10, 1):
        for counter_two in range(0, 8, 1):
            if resistor_values[counter_two, 0] == colour_array[counter_one].upper():
                calculation_values[counter_one] = resistor_values[counter_two, 1]
                break

#main line
x = "BLACK-BLUE-ORANGE"
print(colour_finder(x))