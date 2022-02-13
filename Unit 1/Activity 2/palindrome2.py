'''
Rakshaa Jeyarajah
13 February 2022
This program checks if a sentence contains words that are palindromes
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
@param phrase is the sentence
Sorts through a sentence to see if there are any palindromes. Prints the number of palindromes and which
words are palindromes
'''
def sentence_palindrome_check(phrase):
    phrase.split()
    counter = 0
    palindrome_list = []
    for word in phrase.split():
        if(word.upper() == word_reverse(word).upper()):
            palindrome_list.append(word)
            counter += 1
    
    print("This sentence has ", counter, " palindrome(s)")
    
    for list_counter in range(0, len(palindrome_list), 1):
        print(palindrome_list[list_counter], " is a palindrome")
        
#main line
print("Words that are the same forwards and backwards are palindromes.\nThis program " + 
    " determines if a sentence has a palindrome")

user_input = str(input("(Do not use punctuation) Please enter a sentence:\n"))
sentence_palindrome_check(user_input)