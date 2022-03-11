'''
Rakshaa Jeyarajah
03 03 2022
Makes a pyramid using words
'''
#imports

#functions
def word_pyramid(word):
    '''
    @param word is the word that will be used to build a pyramid
    
    This function removes the first and last letters of a word and prints the remaining letters
    until the word either has 1 or no letter(s)
    '''
    if len(word):
        print(''.join(word))
        word.pop(0)
        if len(word) != 0:
            word.pop(len(word) - 1)
            word_pyramid(word)
    
#main line
while True:
    #Asks for user input
    user_input = str(input("Enter a word: "))
    print("Let's build a pyramid with your word(s)!")
    word_pyramid(list(user_input))

    #Allows the user to rerun the program
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break
print("Good bye!")