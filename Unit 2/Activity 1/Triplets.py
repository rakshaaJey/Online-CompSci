'''
Rakshaa Jeyarajah
15 February 2022
This program generates random poems
'''

#imports
import random

#functions
'''
@param word_one is a word whose suffix is compared to word_two
@param word-two is a word whose suffix is compared to word_one
Compares the suffixes of word_one and word_two to see if they would rhyme
'''
def rhyme_finder(word_one, word_two):
    suffix = ["ly", "ing", "ed", "or", "ung", "and", "an", "at", "og", "sh", "ig", "ad", "ake", "er"]
    for counter in range(0, len(suffix), 1):
        if word_one.endswith(suffix[counter]) == True and word_two.endswith(suffix[counter]) == True:
            return True
    return False

#main line
#Arrays containing nouns and verbs
nouns = ["sister", "brother", "cat", "dog", "mat", "bat", "frog", "fish", "rat", "bog", "bank", "dish", "hat", "rake", "cake", "man", "van", 
            "father", "mother", "can", "pig", "fig", "building", "boyfriend", "girlfriend", "log", "floor", "door", "fan", "caravan", "Easter", "meter"]
verbs = ["ran", "band", "sung", "flung", "hung", "dig", "flying", "singing", "bringing", "read", "lead", "jumped", "dancing", "played", "bake", "make",
            "ban", "mopped", "mixed", "fixing", "brung", "sipping", "fishing", "falling", "jumping"]

#assigns noun_one and noun_two a value and restets the value if they don't rhyme
noun_one = nouns[random.randint(0,len(nouns)-1)]
noun_two = nouns[random.randint(0,len(nouns)-1)]

while rhyme_finder(noun_one, noun_two) != True or noun_one == noun_two:
    noun_one = nouns[random.randint(0,len(nouns)-1)]
    noun_two = nouns[random.randint(0,len(nouns)-1)]

#assigns verb_one and verb_two a value and restets the value if they don't rhyme
verb_one = verbs[random.randint(0,len(verbs)-1)]
verb_two = verbs[random.randint(0,len(verbs)-1)]

while rhyme_finder(verb_one, verb_two) != True or verb_one == verb_two:
    verb_one = verbs[random.randint(0,len(verbs)-1)]
    verb_two = verbs[random.randint(0,len(verbs)-1)]

#Chooses a random poem whose template follows AABB or ABAB pattern 
poem_type = random.randint(0,5)
print("The", noun_one.title(), "by Python AI")
match poem_type:
    case 0: 
        print("There once was a",noun_one, "\nWho liked",verb_one, "\nWhen it called",noun_two, "\nThey tend to",verb_two)
    case 1:
        print("There once was a",noun_one, "\nWho liked",noun_two, "\nWhen they",verb_one, "\nThey tend to",verb_two)
    case 2:
        print("I was a",noun_one, "\nWho liked to",verb_one, "\nWhen I found my",noun_two, "\nWe tried to",verb_two)
    case 3:
        print("My friend had a",noun_one, "\nThey liked to",verb_one, "\nWhen they found out about",noun_two, "\nThey tried",verb_two)
    case 4:
        print("He tried to",verb_one, "\nThe jobs not finished",noun_one, "\nNow work like you are",verb_two, "\nJust like a", noun_two )
    case 5:
        print("The birds are here", verb_one, "\nThere is a river",noun_one, "\nThe girl is",verb_two, "\nFollowing her dog who knows a",noun_two)
