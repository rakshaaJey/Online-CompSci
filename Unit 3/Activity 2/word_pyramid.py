'''
Rakshaa Jeyarajah
DAY MONTH YEAR
DESCRIPTION
'''
#imports

#functions
def word_pyramid(word):
    if len(word):
        print(''.join(word))
        word.pop(0)
        if len(word) != 0:
            word.pop(len(word) - 1)
            word_pyramid(word)
    
#main line
yuh = "rakshaa jeyarajah"
word_pyramid(list(yuh))