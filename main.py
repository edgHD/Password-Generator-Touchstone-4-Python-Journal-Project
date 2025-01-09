"""
Made by edgHD
Touchstone 4: Python Journal Project
"""

from pswGen import passwordGenerator  # Importing the passwordGenerator class i created in another file
from time import sleep as s # Importing sleep function from time module and aliasing it as 's'

# Welcome message display with and 3 second delay
print(""" ____                                     _    
|  _ \ __ _ ___ _____      _____  _ __ __| |   
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |   
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |   
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   """ "\n\n\n\n\n")
s(3)

# Function to gather user input for password generation
def passwordGeneratorHelper():
    
    # Password length?
    while True:
        lengthInput = input("Please enter the length of your password [Default = 8]:")
        if lengthInput == "":
            lengthInput = 8 # If we don't add anything, we set its value at 8 by default
            break
        elif lengthInput.isdigit():
            lengthInput = int(lengthInput)  # Convert input to integer if it's a digit
            break
        else:
            print("\nPlease enter a valid number!\n") # If it's not a digit, we ask the user to enter a valid number
            s(2)

    # Add Upper Case Letters?
    while True:
        upperCaseInput = input("Do you want to include uppercase letters? [Default = Yes]:").lower()
        if upperCaseInput in ("yes", "y", ""):
            upperCaseInput = True # Default to True if input is 'yes', 'y', or empty
            break
        if upperCaseInput in ("no", "n"):
            upperCaseInput = False # Set to False if input is 'no' or 'n'
            break
        else:
            print("\nPlease enter a valid answer! [YES | NO]\n") # If answer is neither a 'yes or a 'no', we ask the user to enter a valid answer again
            s(2)

    # Add Numbers?
    while True:
        numbersInput = input("Do you want to include numbers? [Default = Yes]:").lower()
        if numbersInput in ("yes", "y", ""):
            numbersInput = True # Default to True if input is 'yes', 'y', or empty
            break
        if numbersInput in ("no", "n"):
            numbersInput = False # Set to False if input is 'no' or 'n'
            break
        else:
            print("\nPlease enter a valid answer! [YES | NO]\n") # If answer is neither a 'yes or a 'no', we ask the user to enter a valid answer again
            s(2)

    # Add Special Characters?
    while True:
        specialCharactersInput = input("Do you want to include special characters? [Default = Yes]:").lower()
        if specialCharactersInput in ("yes", "y", ""):
            specialCharactersInput = True # Default to True if input is 'yes', 'y', or empty
            break
        if specialCharactersInput in ("no", "n"):
            specialCharactersInput = False # Set to False if input is 'no' or 'n'
            break
        else:
            print("\nPlease enter a valid answer! [YES | NO]\n") # If answer is neither a 'yes or a 'no', we ask the user to enter a valid answer again
            s(2)

    # Create an instance of passwordGenerator and generate the password
    generatorInput = passwordGenerator(lengthInput, upperCaseInput, numbersInput, specialCharactersInput)
    newPassword = generatorInput.generatePassword()
    print(f"\nYour new password is: {newPassword}")

# Call the helper function to start the password generation process
passwordGeneratorHelper()
