'''
Rakshaa Jeyarajah
February 22 2022
The game of life board game
'''
#imports
import random

#functions
'''
Generates a 20 x 20 board with a boarder and stores it within a 2D array. The return value
is the 2D array with the board. 
'''
def board_generator():
    row, column = [],[]
    for row_counter in range(0, 22):
        for column_counter in range(0, 22):
            if row_counter == 0 or row_counter == 21:
                if column_counter == 0 or column_counter == 21:
                    column.append(" + ")
            if row_counter == 0 or row_counter == 21:
                if column_counter != 0 and column_counter != 21:
                    column.append(" - ")
            if column_counter == 0 or column_counter == 21:
                if row_counter != 0 and row_counter != 21:
                    column.append(" | ")
            if column_counter != 0 and column_counter != 21:
                if row_counter != 0 and row_counter != 21:
                    column.append(" _ ")
        row.append(column)
        column = []    
    
    return row

'''
@param board_array is the 2D array that will be printed
Prints a 2D array
'''
def print_board(board_array):
    for counter in range(0, len(board_array)):
        for counter_two in range(0, len(board_array[counter])):
            if counter_two == 21:
                print(board_array[counter][counter_two])
            else:
                print(board_array[counter][counter_two], end = "")

'''
@param number_of_coordinates is the number of coordinates that will be generated
Generates random coordinates and adds each coordinate to an array. The function
then returns the array with the coordinates
'''
def coordinate_generator(number_of_coordinates):
    counter = 1
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    x_coordinate, y_coordinate = [],[]
    x_coordinate.append(x)
    x_coordinate.append(y)
    y_coordinate.append(x_coordinate)
    x_coordinate = []

    while counter < number_of_coordinates:
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        for counter_two in range (0, len(y_coordinate)):
            if y_coordinate[counter_two][0] == x:
                if y_coordinate[counter_two][1] == y:
                    x = random.randint(1, 20)
                    y = random.randint(1, 20)
                    counter_two = 0
        
        x_coordinate.append(x)
        x_coordinate.append(y)
        y_coordinate.append(x_coordinate)
        x_coordinate = []
        counter += 1
    
    return y_coordinate

'''
@param number_of_coordinates is the number of cells
Adds the cells to the board and checks if they will die or stay alive based on the number of neighbors the 
cell has
'''
def print_game_board(number_of_cells):
    game_board = board_generator()
    coordinates = coordinate_generator(number_of_cells)
    for counter in range(0, len(coordinates)):
        x = coordinates[counter][0]
        y = coordinates[counter][1]
        game_board[x][y] = " Ѡ "
    print("\n   -  -  -  -  -  -  -  -  GENERATION 0  -  -  -  -  -  -  -  -")
    print_board(game_board)

    generation_counter = 1
    next_generation = str(input("Would you like to see the next generation (Yes/No): "))
    while next_generation.upper() != "YES" and  next_generation.upper() != "NO":
        print("Invalid input. Try again")
        next_generation = str(input("Would you like to see the next generation (Yes/No): "))

    while next_generation.upper() == "YES":
        for counter in range(0, len(coordinates)):
            x = coordinates[counter][0]
            y = coordinates[counter][1]
            neighbor_counter = 0
            if game_board[x - 1][y] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x + 1][y] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x][y + 1] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x][y - 1] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x + 1][y + 1] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x + 1][y - 1] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x - 1][y + 1] == " Ѡ ":
                neighbor_counter += 1
            if game_board[x - 1][y - 1] == " Ѡ ":
                neighbor_counter += 1
            
            if neighbor_counter < 2:
                game_board[x][y] = " _ "
            elif neighbor_counter > 3:
                game_board[x][y] = " _ "
            if neighbor_counter == 3 and game_board[x][y] == " _ ":
                game_board[x][y] = " Ѡ "
        
        print("\n   -  -  -  -  -  -  -  -  GENERATION", generation_counter, "-  -  -  -  -  -  -  -")
        generation_counter += 1
        print_board(game_board)
        
        next_generation = str(input("Would you like to see the next generation (Yes/No): "))
        while next_generation.upper() != "YES" and next_generation.upper() != "NO":
            print("Invalid input. Try again")
            next_generation = str(input("Would you like to see the next generation (Yes/No): "))

#main line

#asks user the number of cells that would be present in the current iteration of the game
play_again = "YES"
while play_again.upper() == "YES":
    cell_count = int(input("How many cells do you want in this simulation?\n"))

    while cell_count <= 0 or cell_count >= 200:
        print("That is not a valid input!")
        cell_count = int(input("How many cells do you want in this simulation?\n"))

    print_game_board(cell_count)

    #Asks the user if they would like to go through a new iteration of the game
    play_again = str(input("Thank you for playing the game of life! Play again(Yes/No)?\n"))
    while play_again.upper() != "YES" and play_again.upper() != "NO":
        print("Invalid input. Try again")
        play_again = str(input("Would you like to see the next generation (Yes/No): "))

print("Good bye!")