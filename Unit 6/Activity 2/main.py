import animal_shelter

shelter = animal_shelter.AnimalShelter()

while True:
  print ()
  print ("Hello operator, what will you do?")
  print ("1 - Display dogs")
  print ("2 - Add a dog")
  print ("3 - Remove a dog")
  print ("4 - Display shelter costs")
  print ("5 - Exit shelter")
  choice = input ("Choose an option(1-5): " )
  if choice == "1":
    print(shelter)
  elif choice == "2":
    shelter.add_dog()
  elif choice == "3":
    shelter.remove_dog()
  elif choice == "4":
    shelter.shelter_cost()
  elif choice == "5":
    print("\nGoodbye.")
    break
  else:
    print ("Invalid input\n")