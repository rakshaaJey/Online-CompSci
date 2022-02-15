'''
Rakshaa Jeyarajah
15 February 2022
Calculates all prime numbers between 2 and 1000
'''
#imports

#functions 
'''
@param max is the largest number that will be on the array of numbers starting from 2
This function creates an array that contains the all numbers from 2 to the max (which is determined by a parameter)
'''
def number_list(max):
    numerical_list = [0] * (max -1)
    counter_two = 0
    
    for counter_one in range(2, max + 1, 1):
        numerical_list[counter_two] = counter_one
        counter_two += 1
    
    return numerical_list

'''
@param max_num represents the largest number that the algorithm will check
This function contains an algorithm that will decide if a number is is prime or not. It will remove any numbers that
are not prime from the array and return an array that contains all prime numbers between 2 and the max
'''
def eratosthenes_algorithm(max_num):
    numerical_list = [0] * (max_num - 1)
    numerical_list = number_list(max_num)
    
    for counter in range (2, max_num, 1):
        for counter_two in range (counter + counter, max_num + 1, counter):
            try:
                numerical_list.remove(counter_two)
            except ValueError:
                counter += 1
    
    return numerical_list

'''
@param array is the array that will be formatted
This function formats an array print out the variables it holds in rows of 5
'''
def format_array(array):
    for counter in range(0, len(array) - 1, 7):
        try:
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(array[counter], array[counter + 1], array[counter + 2], array[counter + 3], array[counter + 4], array[counter + 5], 
                array[counter + 6]))
        except IndexError:
            for counter in range(counter, len(array), 1):
                print(array[counter], '\t', end="")
            break

#main line
print("Prime numbers from 1 - 1000 are: ")
format_array(eratosthenes_algorithm(1000))