'''
Rakshaa Jeyarajah
09 03 2022
Generates an array and sorts the array based on user given specifications
'''
#imports
import random

#functions
def selection_sort(data, order):
    '''
    @param data is the array that will be sorted
    @param order will tell the function whether to sort it in ascending or decending order
    
    Uses a selection sorting algorithm to sort a numerical array
    '''
    for counter in range (0, len(data) - 1):
        smallest = counter
        for index in range (counter + 1, len(data)):
            if order == 1:
                if data[index] < data[smallest]:
                    data[index], data[smallest] = data[smallest], data[index] 
            else:
                if data[index] > data[smallest]:
                    data[index], data[smallest] = data[smallest], data[index]

def bubble_sort(data, order):
    '''
    @param data is the array that will be sorted
    @param order will tell the function whether to sort it in ascending or decending order    
    
    Uses a bubble sorting algorithm to sort a numerical array
    '''
    for counter_one in range(len(data)):
        for counter_two in range(0,len(data)-1):
            if order == 1:
                if data[counter_two] > data[counter_two + 1]:
                    data[counter_two], data[counter_two + 1] = data[counter_two + 1], data[counter_two] 
            else:
                if data[counter_two] < data[counter_two + 1]:
                    data[counter_two], data[counter_two + 1] = data[counter_two + 1], data[counter_two]
    return data


def insertion_sort(data, order):
    '''
    @param data is the array that will be sorted
    @param order will tell the function whether to sort it in ascending or decending order    
    
    Uses a intertion sorting algorithm to sort a numerical array
    '''
    for counter in range (1, len(data)): 
        insert = data[counter]
        move_item = counter

        if order == 1:
            while move_item > 0 and data[move_item - 1] > insert:
                data[move_item] = data[move_item - 1]
                move_item -= 1
        else:
            while move_item > 0 and data[move_item - 1] < insert:
                data[move_item] = data[move_item - 1]
                move_item -= 1
        
        data[move_item] = insert
    
def quick_sort(data, low, high, order):
    if low < high:
        split_point = partition(data, low, high)
        quick_sort(data, low, split_point - 1)
        quick_sort(data, split_point + 1, high)
    
def partition(data, first, last): 
    pivot_value = data[first] 
    left_mark = first + 1 
    right_mark = last 
    done = False
    while not done:
        while left_mark <= right_mark and data[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while data[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            data[left_mark], data[right_mark] = data[right_mark], data[left_mark]

    data[first], data[right_mark] = data[right_mark], data[first]
  
    return right_mark 

def random_array_maker(array_length):
    '''
    @param array_length is the length of the randomly generated array

    This function generates numbers for an array and adds them to the array. If the randomly generated number
    is already within the array, a new number will be generated (until a number that is not in the array is generated)
    and will replace the repeated number
    '''
    random_array = []
    for counter in range(0, array_length):
        random_array.append(random.randint(0, 1000))
        while random_array.count(random_array[counter]) > 1:
            random_array[counter] = random.randint(0, 1000)
  
    return random_array
 
#main line
while True:
    while True:
        try:
            array_length = int(input("How many random numbers do you wish to generate?\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
  
    while True:
        try:
            sort_type = int(input("What type of sort would you like to perform\n1. Selection Sort\n2. Bubble Sort\n3. Intersection Sort\n4. Quick Sort\n"))
            while sort_type < 1 or sort_type > 4:
                print("Invalid Input")
                sort_type = int(input("What type of sort would you like to perform\n1. Selection Sort\n2. Bubble Sort\n3. Intersection Sort\n4. Quick Sort\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
  
    while True:
        try:
            order_type = int(input("In what order would you like the numbers to be sorted?\n1. Ascending\n2. Decending\n"))
            while order_type != 1 and order_type != 2:
                print("Invalid Input")
                order_type = int(input("In what order would you like the numbers to be sorted?\n1. Ascending\n2. Decending\n"))
        except ValueError:
            print("Invalid Input")
        else:
            break
    
    sorting_array = random_array_maker(array_length)

 
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye!")