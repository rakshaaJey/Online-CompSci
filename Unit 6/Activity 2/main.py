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
  print ("1 - Display dogs")
  print ("2 - Add a dog")
  print ("3 - Remove a dog")
  print ("4 - Display shelter costs")
  print ("5 - Exit shelter")

  while True:
    try:
      choice = int(input ("Choose an option(1-5): " ))
      while choice < 1 or choice > 5:
        print("Invalid Input")
        choice = int(input ("Choose an option(1-5): " ))
    
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
    shelter.remove_dog()
  elif choice == 4:
    shelter.shelter_cost()
  elif choice == 5:
    print("\nGoodbye.")
    break
  else:
    print ("Invalid input\n")