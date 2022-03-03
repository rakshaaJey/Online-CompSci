'''
'''
#imports
import math
import random

#functions

def cancer_finder(x ,y, old, new, array):
    
    if x < 0 or x >= len(array[0]) or y < 0 or y >= len(array):
        array[y][x] = array[y][x]
    if ord(array[y][x]) != old:
        array[y][x] = array[y][x]

    else:
        array[y][x] = new
        cancer_finder(x+1, y, old, new, array)
        cancer_finder(x-1, y, old, new, array)
        cancer_finder(x, y+1, old, new, array)
        cancer_finder(x, y-1, old, new, array)
    
    while array.count('-')> 0:
        cancer_finder(random(0, len(array) -1), random(0, len(array[0]) -1), '-', ' ')
    return array   

def print_array(array):
    # this function will print the contents of the array
    for y in range(len(array)):
        for x in range(len(array[0])):
            # value by column and row
            print(array[y][x], end=' ')

#main line
data_list = []

text_file = open("Unit 3/Activity 2/Cancer/Cancer.txt", "r")
while True:
    data = text_file.readline().strip()
    if data == "":
        break
    else:
        data_list.append(data)

b = cancer_finder(0 ,0, 45, 32, data_list)
print(b)