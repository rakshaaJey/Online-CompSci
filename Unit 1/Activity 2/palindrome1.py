#imports

#functions
'''
@param word is the 
'''
def wordReverse(word):
    wordReverse = ""
    for length in range(len(word) - 1, -1, -1):
        wordReverse += word[length]
    return wordReverse

def palindromeCheck(word, wordReverse):
    if(word.upper() == wordReverse.upper()):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
#main line
print("Words that are the same forwards and backwards are palindromes.\nThis program " + 
    " determines if a word is a palindrome")

userInput = str(input("Please enter a word: "))

print(userInput + " reversed is " + wordReverse(userInput))
palindromeCheck(userInput, wordReverse(userInput))