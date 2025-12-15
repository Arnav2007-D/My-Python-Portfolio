import random
import string

while True:
    length = int(input("Enter Length: "))

    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation

    password = ''

    for i in range(length):
        password += random.choice(chars)

    print("Your password is: ", password)


    print("\n")
    print("1: New password")
    print("2: Exit")
    selection = int(input("Enter Option:"))

    if selection == 2:
        break 
    
                
          
