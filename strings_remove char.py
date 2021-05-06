# Given a string. Write a program to remove all the occurrences of a character in the string.

def remove_char(astring, char):
    if char not in astring:
        return 'Character is not present in string!'
    newstring = ''
    for letter in astring:
        if letter != char:
            newstring += letter
    return newstring
print(remove_char('Hello world', 'l'))

            


