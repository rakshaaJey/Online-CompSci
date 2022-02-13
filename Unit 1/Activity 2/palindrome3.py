'''
Rakshaa Jeyarajah
13 February 2022
This program checks if a sentence is a palindrome
'''
#imports

#functions
'''
@param string is a string that will have its spaces removed
Removes any spaces from a string variables
'''
def remove_space(string):
    return string.replace(" ", "")

'''
@param word is the word that will be reversed
Reverses a string. Example if the parameter is "hello", this function will return "olleh"
'''
def sentence_reverse(word):
    word_reverse = ""
    for length in range(len(word) -1, -1, -1):
        word_reverse += word[length]
    return word_reverse

'''
@param phrase is the sentence
Sorts through a sentence to see if it is a palindrome
'''
def sentence_palindrome_check(phrase):
    if(remove_space(phrase).upper() == sentence_reverse(remove_space(phrase)).upper()):
        print(phrase," is a palindrome")

#main line
print("Words that are the same forwards and backwards are palindromes.\nThis program " + 
    " determines if a sentence is a palindrome")

user_input = str(input("(Do not use punctuation) Please enter a sentence:\n"))
sentence_palindrome_check(user_input)