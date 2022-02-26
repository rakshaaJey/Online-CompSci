'''
'''
#input

#function
def fibonacci_sequence(num):
    fibonacci_array = [0, 1]
    for counter in range(0, num):
        fibonacci_array.append(fibonacci_array[counter] + fibonacci_array[counter + 1])
    
    return fibonacci_array[num]

#main line
while True:
    user_input = int(input("The first few numbers are listed as followed...\n"+ 
        "1, 1, 2, 3, 5, 8, 13, 21, 34, ...\nWhat fibonacci term would you like to see?\n"))
    try:
        print("Element at", user_input, "of the fibonacci sequence is", fibonacci_sequence(user_input))
    except ValueError:
        print("Invalid input! Try again.")
    
    again = str(input("Would you like to go again(YES/NO)?\n"))
    while again.upper() != "YES" and again.upper() != "NO":
        print("Invalid Input! Try again!")
        again = str(input("Would you like to go again(YES/NO)?\n"))
    if again.upper() == "NO":
        break

print("Good bye")
    
