'''
Rakshaa Jeyarajah
February 22 2022

'''
#imports
import time

#functions

#main line
'''
school_lists is an array with all of the participating schools
donation_options is an array with teh donation options
student_donations is a 2D array that stores the donation information
'''
school_list = ["Catholic Central", "Holy Cross", "John Paul II", "Mother Teresa", "Regina Mundi", "St. Joseph", "St. Mary", "St. Thomas Aquinas", "Exit"]
donation_options = [0.25, 0.5, 1, 2]
student_donation = [[0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0.50, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

while True:
    #prints tha list of schools (and an exit option) and asks the user for the school that will be running the fundraiser
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
    
    #prints the donation options and asks for what donation amount the school will be asking students to bring
    for counter in range(0, len(donation_options), 1):
        print(counter , "- $", str(donation_options[counter]))
        
    while True:
        donation = int(input("What is the estimated donation amount?\n"))
        if donation >= 0 and donation <= 3:
            break
        else:
            print("Invalid input. Try again")

    #asks the user for the number of students that will bring the donation amount    
    while True:
        student_population = int(input("What is the estimated amount of students that will donate?\n"))
        if student_population > 0:
            break
        else:
            print("Invalid input. Try again")
    
    #prints a table with the donation values for each school and the totals
    print(school_list[school],"will be having a fundraiser and will be asking", student_population, " to bring in", )
    student_donation[donation][school + 1] += int(student_population * donation_options[donation])
    student_donation[donation][9] += int(student_population * donation_options[donation])

    print("{:<7} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17}".format("Donation", "Catholic Central", "Holy Cross", "John Paul II", "Mother Teresa", "Regina Mundi", "St. Joseph", "St. Mary", "St. Thomas A", "Total($)"))
    for elements in student_donation:
        donation_value, catholic_centeral, holy_cross, john_paul, mother_teresa, regina_mundi, st_joseph, st_mary, st_thomas, total = elements
        print ("${:<7} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17} {:<17}".format(donation_value, catholic_centeral, holy_cross, john_paul, mother_teresa, regina_mundi, st_joseph, st_mary, st_thomas, total))
    
    time.sleep(5)
    print()

print("Your total is $", (student_donation[0][9] + student_donation[1][9] + student_donation[2][9] + student_donation[3][9]))
print("Thank you for using the donation calculator")
