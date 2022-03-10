'''
Rakshaa Jeyarajah
03 03 2022
Finds all possible ways to rearrange the letters in a word
'''
#imports

#functions

def letter_swap(jumble_list, shift, swap_one, swap_two):
    '''
    @param jumble_list is an array that contains all the different spellings of the original word
    @param shift is a counter that cunts the allowed shifts
    @param swap_one is the index of the first letter that will be swapped
    @param swap_two is the index of the first letter that will be swapped
    
    Swaps Two letters in an array. It shifts the the word after swapping the letters and continues
    shifting and swapping until all ways to rearrange the letters of the given word are done
    '''
    if swap_one < len(jumble_list[0]):
        if swap_two < len(jumble_list[0]):
            if swap_two == swap_one:
                letter_swap(jumble_list, shift, swap_one, swap_two + 1)
            new_word = list(jumble_list[0])
            element_one = new_word[swap_one]
            element_two = new_word[swap_two]
            new_word[swap_one] = element_two
            new_word[swap_two] = element_one
            new_word = ''.join(new_word)
            if jumble_list.count(new_word) == 0:
                jumble_list.append(new_word)
                print(new_word)
            letter_shift(jumble_list, new_word, shift, swap_one, swap_two)
        else:
            letter_swap(jumble_list, shift, swap_one + 1, 0)
    else:
        return

def letter_shift(jumble_list, word, shift, swap_one, swap_two):
    '''
    @param jumble_list is an array that contains all the different spellings of the original word
    @param word is teh word that will be shifted
    @param shift is a counter that cunts the allowed shifts
    @param swap_one is the index of the first letter that will be swapped
    @param swap_two is the index of the first letter that will be swapped
    
    Shifts the letters in a word 1 at a time. After shifting to every possible combination it calls the letter
    swap function. 
    '''
    new_word = []
    if shift < len(jumble_list[0]):
        for counter in range(1, len(word)):
            new_word.append(word[counter])
        new_word.append(word[0])
        if jumble_list.count(''.join(new_word)) == 0:
            jumble_list.append(''.join(new_word))
            print(''.join(new_word))
        letter_shift(jumble_list, new_word, shift + 1, swap_one, swap_two)
    else:
        letter_swap(jumble_list, 1, swap_one, swap_two + 1)

#main line
while True:
    user_input = str(input("Enter a word: "))
    print("By rearranging your word,", user_input, "I have come up with the following \"words\"")
    jumble_list = [user_input]
    letter_swap(jumble_list, 1, 0, 0)
    
    #Allows the user to rerun the program
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break
print("Good bye!")