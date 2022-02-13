'''
Rakshaa Jeyarajah
13 February 2022
This program applies a Caesar Cypher to a string and either encrypts or decrypts the string depending
on use input
'''
#imports

#functions
'''
@param string is the string that will be searched through
This function will check if a string contains any numeric values. It returns true if the string does contain any numeric values and 
false if the string doesn't contain any numeric values
'''
def contains_numbers(string):     
    for counter in range(0, len(string), 1):
        char = string[counter]
        if(char.isdigit() == True):
            return True
    
    return False

'''
@param message is the message that will be encrypted
@param shift is the shift that will be applied to the cypher 
This function applies the Caesar Cypher with a shift that is specified by the user to a string of text to find a encrypted message
'''
def encrypt_message(message, shift):
    encrypted_message = ""
  
    for counter in range(0, len(message), 1):
        char = message[counter]
        
        if(ord(char) == 32):
            encrypted_message += ' '
        elif (char.isupper() == True):
            if((ord(char)+ shift) > 90):
                encrypted_message += chr((ord(char)+ shift - 26))
            else:
                encrypted_message += chr((ord(char)+ shift))
        else:
            if((ord(char)+ shift) > 122):
                encrypted_message += chr((ord(char)+ shift - 26))
            else:
                encrypted_message += chr((ord(char)+ shift))

    return encrypted_message    

'''
@param message is the message that will be decrypted
@param shift is the shift that will be applied to the cypher 
This function applies the Caesar Cypher with a shift that is specified by the user to a string of text to find a decrypted message
'''
def decrypt_message(message, shift):
    decrypted_message = ""
  
    for counter in range(0, len(message), 1):
        char = message[counter]
        
        if(ord(char) == 32):
            decrypted_message += ' '
        elif (char.isupper() == True):
            if((ord(char)- shift) < 65):
                decrypted_message += chr((ord(char)- shift + 26))
            else: 
                decrypted_message += chr((ord(char)- shift))
        else:
            if((ord(char)- shift) < 97):
                decrypted_message += chr((ord(char)- shift + 26))
            else: 
                decrypted_message += chr((ord(char)- shift))
    return decrypted_message    


#main line

print("This program will encrypt or decrypt a message using a simple encryption method of rotating letters:")

#Asks user for input on a message that will be encrypted/ decrypted. Checks if input is valid
user_message = str(input("Please enter your message (don't use nay punctuation or numbers):\n"))
while(contains_numbers(user_message) == True):
    print("Invalid input, try again.")
    user_message = str(input("Please enter your message:\n"))

#Asks user for input on the shift for the message that will be encrypted/ decrypted. Checks if input is valid
rotation_amount = int(input("Enter a rotation amount (between 1 - 25) to the right:\n"))
while(rotation_amount > 25 or rotation_amount < 1):
    print("Invalid input, try again.")
    rotation_amount = int(input("Enter a rotation amount (between 1 - 25):\n"))

#Asks user for input on if they want the message to be encrypted or decrypted. Checks if input is valid
encrypt_or_decrypt = int(input("Would you like to encrypt or decrypt the message\n1 - Encrypt \n2 - Decrypt\n"))
while(encrypt_or_decrypt != 1 and encrypt_or_decrypt != 2):
    print("Invalid input, try again")
    encrypt_or_decrypt = int(input("Would you like to encrypt or decrypt the message\n1 - Encrypt \n2 - Decrypt\n"))

if(encrypt_or_decrypt == 1):
    print("Your original phrase is ", user_message)
    print("Your encrypted phrase is ", encrypt_message(user_message, rotation_amount))
else:
    print("Your original phrase is ", user_message)
    print("Your decrypted phrase is ", decrypt_message(user_message, rotation_amount))