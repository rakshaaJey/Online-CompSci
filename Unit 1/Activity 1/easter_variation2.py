#imports

#functions
'''
@param year represents the year that easter will occur
This function uses the input from the julian easter date calculator and figures out the gregorian easter date
'''
def gregorianEasterCalculator(year):
    gregorianEasterDate = julianEasterCalculator(year)
    gregorianEasterDate[0] += 13

    if gregorianEasterDate[1] == 3 or gregorianEasterDate[1] == 5 and gregorianEasterDate[0] >= 31:
        gregorianEasterDate[0] -= 31
        gregorianEasterDate[1] += 1
    elif gregorianEasterDate[0] >= 30 and gregorianEasterDate[1] == 4:
        gregorianEasterDate[0] -= 30
        gregorianEasterDate[1] += 1

    return gregorianEasterDate

'''
@param year represents the year that easter will occur
This function uses the Meeus's Julian algorithm to find the date that easter wil be on according to the julian calendar
'''
def julianEasterCalculator(year):

    a = year % 4
    b = year % 7
    c = year % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    month = int(((d + e + 114) / 31))
    day = ((d + e + 114) % 31) + 1

    julianEasterDate = [day, month]

    return julianEasterDate

'''
@param numerticalMonth represents the numerical value of the month
This function takes in a numerical value that represents a month and outputs a string of the month
'''
def stringMonth(numericalMonth):
    match numericalMonth:
        case 3:
            stringMonth = "March"
        case 4:
            stringMonth = "April"
        case 5:
            stringMonth = "May"
    return stringMonth

#main line
userYear = int(input('Type in a year '))

easterDateOne = gregorianEasterCalculator(userYear)
easterDateTwo = julianEasterCalculator(userYear)

print("Easter will fall on Sunday, ", easterDateOne[0], ' ', stringMonth(easterDateOne[1]), ' ', userYear, ' according to the gregorian calendar')
print("Easter will fall on Sunday, ", easterDateTwo[0], ' ', stringMonth(easterDateTwo[1]), ' ', userYear, ' according to the julian calendar')