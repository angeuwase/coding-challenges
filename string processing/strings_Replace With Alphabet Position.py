# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# Example 
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

# Solution idea
# need to make string characters all lower case so python treats them the same

# Solution
    # Each letter has an associated ordinal number. 
    # a = 97 --> should map to 1
    # z = 122 --> should map to 26
    # formula: y = mx + c 
    # y1 = 1, y2 = 26
    # x1 = 97, x2 = 122
    # m = (26-1)/(122-97)= 1
    # c = -96
    # y = x -96 GIVEN A LETTER'S ORDINAL VALUE, SUBTRACT 96 FROM IT TO GET THE POSITION OF THE LETTER IN THE ALPHABET

def alphabet_position(text):

    # Make all string characters lower case so that python treats them the same
    text = text.lower()

    # iterate over the string. for every character in the string, if it is a letter, get its position, convert it to a string and add it to the list, otherwise skip it
    positions = []

    for char in text:

        
        if char.isalpha():
            position = ord(char) - 96
            positions.append(str(position))
        
    # join all the positions into a string. Method only works if items to be joined are string type
    result = ' '.join(positions)

    return result

print(alphabet_position("The sunset sets at twelve o' clock."))
# terminal output: 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
