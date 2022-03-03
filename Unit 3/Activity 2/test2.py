swap = 3
word = "murder"

for counter in range (1, 10):
    if swap >= len(word):
        swap = 1
    word = list(word)
    element_one = word[0]
    element_two = word[swap]
    word[0] = element_two
    word[swap] = element_one
    word = ''.join(word)
    swap += 1
    print(word)