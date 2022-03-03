'''
Rakshaa Jeyarajah
DAY MONTH YEAR
DESCRIPTION
'''
#imports
import random 

#functions
def factorial(num):
    if (num <= 1):
        return 1
    else:
        return num*factorial(num-1)

def word_jumbler(jumble_list, word, shift, max_words):
    new_word = []
    if max_words != len(jumble_list):
        if shift <= len(word):
            for counter in range(shift, len(word)):
                new_word.append(word[counter])
            for counter in range(0, shift):
                new_word.append(word[counter])
            if jumble_list.count(''.join(new_word)) == 0:
                jumble_list.append(''.join(new_word))
                print(''.join(new_word))
            word_jumbler(jumble_list, new_word, shift + 1, max_words)
        else:
            word = list(word)
            random.shuffle(word)
            result = ''.join(word)
            word_jumbler(jumble_list, result, 0, max_words)

#main line
word = "fish"
jumble_list = [word]
max = factorial(len(word))
word_jumbler(jumble_list, word, 0, max)
