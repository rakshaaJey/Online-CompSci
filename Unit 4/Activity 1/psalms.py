'''
Rakshaa Jeyarajah
08 03 2022
Finds if a psalm is in a text file and prints it out. If it is not found an message will be printed 
stating that the psalm was not found
'''
#imports

#functions

def number_array(array):
    '''
    @param array is the array that will be modifies

    Searches through an array and returns an array that contains only the numerical values that were found in original array
    '''
    number_array = []
    for counter in range (0, len(array)):
        if array[counter].isdigit() == True:
            number_array.append(int(array[counter]))
    
    return number_array

def print_array(array, lower_limit, upper_limit):
    '''
    @param array is the array that will be printed
    @param lower_limit is the lowest index that will be printed
    @param upper_limit is the highest index that will be printed

    Prints the desired indexes of an array
    '''
    for counter in range(lower_limit, upper_limit + 1):
        if counter == upper_limit:
            print("["+str(array[counter])+"]")
        else:
            print("["+str(array[counter])+"]", end= " ")

def binary_search_algorithm(array, lower_limit, upper_limit, target):
    '''
    @param array is the array that will be searched through
    @param left is the lowest value that will be looked at
    @param right is the highest value that will be looked at
    @param target is the value that will be searched for

    Uses a binary search algorithm to determine if the desired value is within a given array
    '''
    if upper_limit >= lower_limit:
        print("Searching for Psalm",target,": ",end="")
        print_array(array, lower_limit, upper_limit)
  
        middle = lower_limit + (upper_limit - lower_limit)// 2

        if array[middle] == target:
            return True
  
        elif array[middle] > target:
            return binary_search_algorithm(array, lower_limit, middle - 1, target)
  
        else:
            return binary_search_algorithm(array, middle + 1, upper_limit, target)
  
    else:
        return False

#main line
text_file = open('Unit 4/Activity 1/Psalms.txt')
psalm_array = []

#Takes data from the text file and adds it to an array
while True:
    psalm_data = text_file.readline().strip()
    if psalm_data == "":
        break
    else:
        psalm_array.append(psalm_data)
text_file.close() 

while True:
    #Asks for user input
    while True:
        try:
            target = int(input("Enter a Psalm number between 1 and 99: "))
        except ValueError:
            print("Invalid input! Try again.")
        else:
            if target > 99 or target < 1:
                print("Invalid input! Try again.")
            else:
                break

    #Checks if the psalm was found and prints the appropriate message
    if binary_search_algorithm(number_array(psalm_array), 0, len(number_array(psalm_array)) - 1, target) == True:
        print("\nPsalm", target,'\n'+ psalm_array[psalm_array.index(str(target)) + 1])
    else:
        print("\nThe psalm wasn't found")
    
    #Allows the user to rerun the program
    again = str(input("\nWould you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break
    print()
print("Good bye!")