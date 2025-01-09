import string # Importing the string module for character sets
from random import choice as randomize # Importing choice function from random module and aliasing it as 'randomize'

# Class to generate passwords based on user preferences
class passwordGenerator:
    def __init__(self, length, containsUppercase=True, containsNumbers=True, containsSpecialChar=True):
        
        self.length = length # Length of the password
        self.containsUppercase = containsUppercase # Whether to include uppercase letters
        self.containsNumbers = containsNumbers # Whether to include numbers
        self.containsSpecialChar = containsSpecialChar  # Whether to include special characters

        # Character sets to use in password generation
        self.lowerCase = string.ascii_lowercase
        self.upperCase = string.ascii_uppercase
        self.numbers = string.digits
        self.specialChar = string.punctuation
    
    # Method to generate the password
    def generatePassword(self):
        password = ""
        for i in range(self.length):
            temp = ""
            temp += randomize(self.lowerCase) # Always include a lowercase letter
            if self.containsUppercase:
                temp += randomize(self.upperCase) # Include an uppercase letter if specified
            if self.containsNumbers:
                temp += randomize(self.numbers) # Include a number if specified
            if self.containsSpecialChar:
                temp += randomize(self.specialChar) # Include a special character if specified
            password += randomize(temp) # Add a random character from the temp string to the password
        return password