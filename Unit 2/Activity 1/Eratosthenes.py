'''
Rakshaa Jeyarajah
15 Frbruary 2022

'''
#imports

#functions 
def eratosthenes_algorythm(max_num):
    not_prime_number_list = []
    prime_number_list = []
    for counter in range(2, max_num+1):
        if (counter not in not_prime_number_list):
            prime_number_list.append(counter)
            for num in range(counter + counter, max_num+1, counter):
                not_prime_number_list.append(num)
    
    return prime_number_list

def format_array(array):
    for counter in range(0, len(array)):
        print(array[counter], '\t')

#main line
format_array(eratosthenes_algorythm(70))