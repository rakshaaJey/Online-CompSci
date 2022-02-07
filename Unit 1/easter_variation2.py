#imports

#functions
def gregorianEaster(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (8 + b) // 25
    g = int((b - f + 1)/3)
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    j = (32 + 2*e + 2*i - h - k)%7
    m = (a + 11*h + 22*j)//451
    month = (h + j -7*m + 114)//31
    p = (h + j - 7*m + 114)%31
    day = p + 1

    gregorianEasterDate = [day, month, year]

    return gregorianEasterDate

def julianEaster(year):
    julianEasterDate = gregorianEaster(year)
    julianEasterDate[0] += 13

    if julianEasterDate[1] == 3 or julianEasterDate[1] == 5:
        if julianEasterDate[0] >= 31:
            julianEasterDate[0] = julianEasterDate[0] - 31
        elif julianEasterDate[1] == 4:
            julianEasterDate[0] = julianEasterDate[0] - 30
    return julianEasterDate

def stringMonth(numericalMonth):
    match numericalMonth:
        case 3:
            month = "March"
        case 4:
            month = "April"
        case 5:
            month = "May"
    return month

#main line
userYear = int(input('Type in a year '))

easterDateOne = gregorianEaster(userYear)
easterDateTwo = julianEaster(userYear)

print("Easter will fall on Sunday, ", easterDateOne[0], ' ', stringMonth(easterDateOne[1]), ' ', easterDateOne[2], ' according to the gregorian calendar')
print("Easter will fall on Sunday, ", easterDateTwo[0], ' ', stringMonth(easterDateTwo[1]), ' ', easterDateTwo[2], ' according to the julian calendar')