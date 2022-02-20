'''
Rakshaa Jeyarajah
Febuary 19 2022

'''
#imports

#functions

#main line
school_list = ["Catholic Central", "Holy Cross", "John Paul II", "Mother Teresa", "Regina Mundi", "St. Joseph", "St. Mary", "St. Thomas Aquinas", "Exit"]
donation_options = [0.25, 0.5, 1, 2]
student_donation = [[0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0.50, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
array_index = 0

while True:
    for counter in range(0, len(school_list), 1):
        print(counter , "-", school_list[counter])
        
    while True:
        school = int(input("Which school is fundraising?\n"))
        if school >= 0 and school <= len(school_list) - 1:
            break
        else:
            print("Invalid input. Try again")
    if school == len(school_list) - 1:
        break
        
    for counter in range(0, len(donation_options), 1):
        print(counter , "- $", str(donation_options[counter]))
        
    while True:
        donation = int(input("What is the estimated donation amount?\n"))
        if donation >= 0 and donation <= 3:
            break
        else:
            print("Invalid input. Try again")
        
    while True:
        student_population = int(input("What is the estimated amount of students that will donate?\n"))
        if student_population > 0:
            break
        else:
            print("Invalid input. Try again")
        
    student_donation[donation][school + 1] += int(student_population * donation_options[donation])
    student_donation[donation][9] += int(student_population * donation_options[donation])

    print("{:<5} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17}".format("", "Catholic Central", "Holy Cross", "John Paul II", "Mother Teresa", "Regina Mundi", "St. Joseph", "St. Mary", "St. Thomas A", "Total($)"))
    for elements in student_donation:
        donation_value, catholic_centeral, holy_cross, john_paul, mother_teresa, regina_mundi, st_joseph, st_mary, st_thomas, total = elements
        print ("{:<5} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17}".format(donation_value, catholic_centeral, holy_cross, john_paul, mother_teresa, regina_mundi, st_joseph, st_mary, st_thomas, total))

print("Thank you for using the donation calculator")
