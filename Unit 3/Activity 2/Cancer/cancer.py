'''
Rakshaa Jeyarajah
03 03 2022
Finds the cancer spots in a text file
'''
#imports

#functions
def get_cancer_spot_total(cancer_array):
    '''
    @param cancer_array is the array that will be sorted through to find spots of cancer

    This function sorts through an array to find the start of a cancer spot. Once a cancer spot
    is found it is flood filled and a counter counting the amount of cancer spot found will increase 
    by one
    '''
    array_width = len(cancer_array)
    array_height = len(cancer_array[0])

    spot_count = 0
    for x in range(array_width):
        for y in range(array_height):
            if cancer_array[x][y] == '-':
                flood_fill(cancer_array, x, y, '-', ' ')
                spot_count += 1
    
    print("Your file has", spot_count, "cancer spots in it. \nThe new grid is:")
    print_array(cancer_array)

def flood_fill(array, x, y, old_char, new_char):
    '''
    @param array is the array that will be flood filled
    @param x is the current x coordinate
    @param y is the current y coordinate
    @param old_char is the charecter that will be replaced
    @param new_char is the charecter that will be replacing the old one

    This flood fills spots with the cancer cell (represented by the charecter '-') with a blank space
    '''
    array_width = len(array)
    array_height = len(array[0])

    if array[x][y] != old_char:
        return

    array[x][y] = new_char

    if x > 0: 
        flood_fill(array, x-1, y, old_char, new_char)

    if y > 0:
        flood_fill(array, x, y-1, old_char, new_char)

    if x < array_width-1:
        flood_fill(array, x+1, y, old_char, new_char)

    if y < array_height-1:
        flood_fill(array, x, y+1, old_char, new_char)

def print_array(array):
    '''
    @param array is the 2D array that will be printed

    Prints a 2D array
    '''
    for counter in range(0, len(array)):
        for counter_two in range(0, len(array[counter])):
            if counter_two == len(array[counter])-1:
                print(array[counter][counter_two])
            else:
                print(array[counter][counter_two], end = "")

#main line
data_list = []

#Opens text file
text_file = open("Activity 2/Cancer/Cancer.txt", "r")
while True:
    data = text_file.readline().strip()
    if data == "":
        break
    else:
        #Takes data from the text file and adds it to an array
        data_list.append(list(data))
text_file.close() 
 
print("Your cancer data file looks like this:")
print_array(data_list)
get_cancer_spot_total(data_list)