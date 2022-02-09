'''
Rakshaa Jeyarajah
08 February 2022
This program finds the julian and gregorian dates for easter according to the Meeus algorithm
'''
#imports

#functions
'''
@param year represents the year that easter will occur
This function uses the Meeus's Julian algorithm to find the date that easter will be on according to the julian calendar. It then returns the 
date as an array that contains the date and month (in numerical form) of easter
'''
def julian_easter_calculator(year):

    a = year % 4
    b = year % 7
    c = year % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    month = int(((d + e + 114) / 31))
    day = ((d + e + 114) % 31) + 1

    easter_date = [day, month]

    return easter_date

'''
@param year represents the year that easter will occur
This function uses the input from the julian easter date calculator and figures out the gregorian easter date
'''
def gregorian_easter_calculator(year):
    easter_date = julian_easter_calculator(year)
    easter_date[0] += 13

    if easter_date[1] == 3 or easter_date[1] == 5 and easter_date[0] >= 31:
        easter_date[0] -= 31
        easter_date[1] += 1
    elif easter_date[0] >= 30 and easter_date[1] == 4:
        easter_date[0] -= 30
        easter_date[1] += 1

    return easter_date

'''
@param numerical_month represents the numerical value of the month
This function takes in a numerical value that represents a month and outputs a string of the month
'''
def string_month(numerical_month):
    match numerical_month:
        case 3:
            string_month = "March"
        case 4:
            string_month = "April"
        case 5:
            string_month = "May"
    return string_month

#main line
user_year = int(input('Type in a year: '))

gregorian_easter_date = gregorian_easter_calculator(user_year)
julian_easter_date = julian_easter_calculator(user_year)

print("Easter will fall on Sunday, ", gregorian_easter_date[0], ' ', string_month(gregorian_easter_date[1]), ' ', user_year, ' according to the gregorian calendar')
print("Easter will fall on Sunday, ", julian_easter_date[0], ' ', string_month(julian_easter_date[1]), ' ', user_year, ' according to the julian calendar')