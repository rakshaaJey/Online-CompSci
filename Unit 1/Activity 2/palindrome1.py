#imports

#functions
'''
@param word is the word that will be reversed
Reverses a word. Example if the parameter is "hello", this function will return "olleh"
'''
def wordReverse(word):
    wordReverse = ""
    for length in range(len(word) - 1, -1, -1):
        wordReverse += word[length]
    return wordReverse

'''
@param word is the word that will be reversed
@param reverseOfWord is reverse of the parameter word
Checks if a word is a palindrome by comparing the original word to the word when its charectars are reversed
'''
def palindromeCheck(word):
    reverseOfWord = wordReverse(word)
    if(word.upper() == reverseOfWord.upper()):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
        
#main line
print("Words that are the same forwards and backwards are palindromes.\nThis program " + 
    " determines if a word is a palindrome")

userInput = str(input("Please enter a word: "))

print(userInput + " reversed is " + wordReverse(userInput))
palindromeCheck(userInput, wordReverse(userInput))