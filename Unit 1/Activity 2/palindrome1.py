'''
Rakshaa Jeyarajah
13 February 2022
This program checks if a word is a palindrome
'''
#imports

#functions
'''
@param word is the word that will be reversed
Reverses a word. Example if the parameter is "hello", this function will return "olleh"
'''
def word_reverse(word):
    word_reverse = ""
    for length in range(len(word) -1, -1, -1):
        word_reverse += word[length]
    return word_reverse

'''
@param word is the word that will be reversed
@param reverseOfWord is reverse of the parameter word
Checks if a word is a palindrome by comparing the original word to the word when its charectars are reversed
'''
def palindrome_check(word, reverse_of_word):
    if(word.upper() == reverse_of_word.upper()):
        print("It is a palindrome")
    else:
        print(word, " is not a palindrome")
        
#main line
print("Words that are the same forwards and backwards are palindromes.\nThis program " + 
    " determines if a word is a palindrome")

user_input = str(input("Please enter a word:\n"))

print('\n' +user_input, " reversed is ", word_reverse(user_input))
palindrome_check(user_input, word_reverse(user_input))