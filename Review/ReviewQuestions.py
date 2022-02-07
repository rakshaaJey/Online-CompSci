#imports

#functions
#Lists the intergers between the desired variables
#The solution was looked at when coding the following function
def output(intOne, intTwo):
    if intOne < intTwo:
        for counter in range(intOne, intTwo + 1):
            print(counter, end=' ')
    elif intTwo < intOne :
        for counterTwo in range(intOne, intTwo - 1, -1):
            print(counterTwo, end=' ')
    else:
        print('The intergers are the same')

#outputs a scentence with the user's name
def nameScentence(userName):
    print('Your name is ' + userName + '. Hello ' + userName + '!')

#adds the user's name to a text file
def addNameToFile(file, userName):
    file.write(userName + '\n')
    file.close()

#main line
name = input('Please enter your full name\n').upper()
textFile = open("Review/UserNames.txt", "a")

nameScentence(name)
addNameToFile(textFile, name)

#loop that asks the user for two numbers until the user wants to exit the loops
userInput = 'YES'
while userInput == 'YES':
    while True:
        try:
            numberOne = int(input('What is the first number?\n'))
        except ValueError:
            print('Invalid input. Try again!')
        else:
            break
    while True:
        try:
            numberTwo = int(input('What is the second number\n'))   
        except ValueError:
            print('Invalid input. Try again!') 
        else:
            break
    
    output(numberOne, numberTwo) 
    userInput = input('\nWould you like to continue? (Yes or No)\n').upper()

print('Goodbye!')