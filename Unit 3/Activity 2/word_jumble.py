'''
Rakshaa Jeyarajah
DAY MONTH YEAR
DESCRIPTION
'''
#imports
import random 
import sys
import math
sys.setrecursionlimit(10000)

#functions
def factorial(num):
    if (num <= 1):
        return 1
    else:
        return num*factorial(num-1)

#check for double letters
def word_jumbler(jumble_list, word, shift, swap, max_words):
    new_word = []
    if max_words != len(jumble_list):
        if swap <= len(word):
            if swap >= len(word):
                swap = 1
            word = list(word)
            element_one = word[0]
            element_two = word[swap]
            word[0] = element_two
            word[swap] = element_one
            if jumble_list.count(''.join(word)) == 0:
                jumble_list.append(''.join(word))
                print(''.join(word))
            word_jumbler(jumble_list, word, 0, shift + 1, max_words)
        if shift <= len(word):
            for counter in range(shift, len(word)):
                new_word.append(word[counter])
            for counter in range(0, shift):
                new_word.append(word[counter])
            if jumble_list.count(''.join(new_word)) == 0:
                jumble_list.append(''.join(new_word))
                print(''.join(new_word))
            word_jumbler(jumble_list, new_word, shift + 1, swap, max_words)
        if shift <= len(word) and swap <= len(word):
            word_jumbler(jumble_list, new_word, 0, 1, max_words)

def max_jumbles(word):
    denominator = 1
    for counter in range(0, len(word)):
        denominator *= factorial(word.count(word[counter]))
        word.replace(word[counter], "")
    denominator = math.sqrt(denominator)
    return factorial(len(word))/denominator


#main line
word = "happy"
jumble_list = [word]
word_jumbler(jumble_list, word, 0, 1, max_jumbles(word))
