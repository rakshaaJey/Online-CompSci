'''
Rakshaa Jeyarajah 
February 22 2022
A game of hangman
'''
#imports
import random
import time

#functions
'''
@list is a list of words and categories
Randomly chooses a category and a word within each category for the game
'''
def category_and_word_chooser(list):
    category_index = random.randint(0,len(list) - 1)
    word_index = random.randint(1,len(list[category_index]) - 1)
    category_and_word = [list[category_index][0], list[category_index][word_index]]
    return category_and_word

'''
@word is the word for hangman
Changes the word into blank spaces (ex. hello -> _ _ _ _ _ )
'''
def secret_word(word):
    blank_word = ""
    for counter in range(0, len(word), 1):
        char = word[counter]
        if char == ' ':
            blank_word += " "
        else:
            blank_word += "_"

    return blank_word

'''
@param category is the category of word
@param hidden_word is the word as a blank 
@param word is the word
This allows the user to guess a letter and checks if the letter is within the randomly generated word. 
Leaves the function if the user guesses the wrong letter 7 times
'''
def guess_word(category, hidden_word, word):

    guess_counter = 7
    guesses_list = [""]
    while guess_counter > 0:
        print(category)
        print("Number of words: ", len(word.split()))
        print(hidden_word)
        while True:
            guess = str(input("What is your guess?\n"))
            guesses_list.append(guess)
            if len(guess) > 1:
                print("You can only guess a single letter. Try again!")
            elif guesses_list.count(guess) > 1:
                print("You already guessed this!")
            else:
                break
                        
        if word.find(guess.upper()) != -1:
            for counter in range(0, len(word), 1):
                char = word[counter]
                if char == guess.upper():
                    hidden_word = hidden_word[:counter] + char + hidden_word[counter+1:]

        else:
            guess_counter -= 1
        
        match guess_counter:
            case 7:
                time.sleep(1)
                print()
            case 6:
                time.sleep(1)
                print(" O ")
            case 5:
                time.sleep(1)
                print(" O \n | ")
            case 4:
                time.sleep(1)
                print(" O \n/|")
            case 3:
                time.sleep(1)
                print(" O \n/|\\")
            case 2:
                time.sleep(1)
                print(" O \n/|\\\n | ")
            case 1:
                time.sleep(1)
                print(" O \n/|\\\n | \n/")
            case 0:
                print(" O \n/|\\\n | \n/ \\")
                print("The word was", word, "\nGood Try!")
        
        if hidden_word == word:
            print(category)
            print("Number of words: ", len(word.split()))
            print(hidden_word)
            print("Congratulations! You guessed correct")
            break

#main line
#2D array with the categories and words  
possible_words = [["TV SHOWS", "FRIENDS", "THE OFFICE", "POWER RANGERS", "SHERA", "HE MAN", "COBRA KAI", "WANDAVISION", "LOKI", "STRANGER THINGS"], 
    ["MOVIES", "AVENGERS", "THE BEE MOVIE", "SHREK", "ENCANTO", "FINDING NEMO", "THE MATRIX", "THE NOTEBOOK", "FERRIS BUELLERS DAY OFF", "TITANIC", "PARASITE"],
    ["ANIMALS", "CAT", "DOG", "TIGER", "LION", "SHARK", "PANDA", "FISH", "ELEPHANT", "HIPPOPOTAMUS", "GIRAFFE", "MOOSE", "GOOSE", "DONKEY", "PIGEON"],
    ["CELEBRETIES", "GORDON RAMSAY", "CELINE DION", "SANDRA OH", "RYAN REYNOLDS", "KEANU REEVES", "DRAKE", "JIM CARREY", "ELLIOT PAGE", "SETH ROGEN"], 
    ["CITIES", "TORONTO", "PARIS", "MONTREAL", "NEW YORK CITY", "LOS ANGELES", "CHICAGO", "LONDON", "TOKYO", "SEOUL", "JAKARTA", "DELHI", "BEIJING"],
    ["COUNTRIES", "CANADA", "UNITED STATES OF AMERICA", "BRAZIL", "CHINA", "TOKYO", "SOUTH KOREA", "SPAIN", "FRANCE", "INDIA", "SOUTH AFRICA", "EGYPT"], 
    ["LANGUAGES", "ENGLISH", "FRENCH", "TAMIL", "GERMAN", "SPANISH", "JAPANESE", "KOREAN", "MANDARIN", "CANTONESE", "PORTUGUESE", "RUSSIAN", "ARABIC"], 
    ["DISNEY PRINCESSES", "MULAN", "ARIEL", "JASMINE", "CINDERELLA", "SNOW WHITE", "RAPUNZEL", "BELLE", "TIANA", "AURORA", "MERIDA", "MOANA"], 
    ["POKEMON", "PIKACHU", "LUCARIO", "EEVEE", "MEW TWO", "MUDKIP", "JIGGLYPUFF", "MAGIKARP", "MEOWTH", "MEW", "CHARIZARD", "SNORLAX", "GENGAR", "UMBREON"], 
    ["SUPER HEROES", "SUPER MAN", "BAT MAN", "SPIDER MAN", "IRON MAN", "HULK", "BLACK WIDOW", "CAPITAN AMERICA", "WONDER WOMAN", "FLASH", "THOR", "GREEN LANTERN"], 
    ["SUPER VILLAINS", "JOKER", "VENOM", "CAT WOMAN", "THE RIDDLER", "ULTRON", "TASKMASTER", "LOKI", "MAGNETO", "THANOS", "ABOMINATION", "YELLOWJACKET"]]

#Allows the user to play hangman and once the game is done asks the user if they want to replay
play_again = "YES"
while play_again.upper() == "YES":
    word_and_category = category_and_word_chooser(possible_words)
    hidden_word = secret_word(word_and_category[1])
    guess_word(word_and_category[0], hidden_word, word_and_category[1])

    play_again = str(input("Would you like to play again(Yes/No): "))
    while play_again.upper() != "YES" and play_again.upper() != "NO":
        print("Invalid input. Try again")
        play_again = str(input("Would you like to see the next generation (Yes/No): "))