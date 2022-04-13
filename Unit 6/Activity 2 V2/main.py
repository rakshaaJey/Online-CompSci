'''
Rakshaa Jeyarajah
06 April 2022
Creates an animal shelter and allows the user to add to the animal shelter
'''
#imports
import animal_shelter

#functions

#main line
shelter = animal_shelter.AnimalShelter()

while True:
  #Asks the user what they want to do
  print ()
  print ("Hello operator, what will you do?")
  print ("1 - Display animals")
  print ("2 - Add a dog")
  print ("3 - Add a cat")
  print ("4 - Remove an animal")
  print ("5 - Display shelter costs")
  print ("6 - Edit animal")
  print ("7 - Exit shelter")

  while True:
    try:
      choice = int(input ("Choose an option(1-7): " ))
      while choice < 1 or choice > 7:
        print("Invalid Input")
        choice = int(input ("Choose an option(1-7): " ))
    
    except ValueError:
      print("Invalid Input!")
    
    else:
      break

  #Take the approporiate course of action based on what the user inputs
  if choice == 1:
    print(shelter)
  elif choice == 2:
    shelter.add_dog()
  elif choice == 3:
    shelter.add_cat()
  elif choice == 4:
    shelter.remove_animal()
  elif choice == 5:
    shelter.shelter_cost()
  elif choice == 6:
    shelter.edit_animal()
  elif choice == 7:
    print("\nGoodbye.")
    break