# Read the input string and shift value from the user
input_string = input("Enter a string to encrypt: ")
shift = int(input("Enter a shift value (1-25): "))

# Make sure the shift value is in the valid range
while shift < 1 or shift > 25:
    print("Shift value must be in the range 1-25. Please try again.")
    shift = int(input("Enter a shift value (1-25): "))

# Create an empty string to store the encrypted text
encrypted = ""

# Iterate over each character in the input string
for c in input_string:
    # If the character is a letter, apply the shift
    if c.isalpha():
        # Convert the letter to ASCII code
        code = ord(c)
        
        # Shift the ASCII code by the specified amount
        code += shift
        
        # If the code is now outside the range of lower-case letters,
        # adjust it to wrap around to the beginning of the alphabet
        if code > ord('z'):
            code -= 26
        
        # If the code is now outside the range of upper-case letters,
        # adjust it to wrap around to the beginning of the alphabet
        if code > ord('Z') and c.isupper():
            code -= 26
        
        # Convert the shifted ASCII code back to a letter and add it
        # to the encrypted text
        encrypted += chr(code)
    else:
        # If the character is not a letter, add it to the encrypted
        # text without applying the shift
        encrypted += c

# Print the encrypted text
print(encrypted)
