# Determine if a string has all unique characters

# With an auxiliary data structure
def all_unique(astring):
    astring = astring.lower()
    astring = astring.replace(' ', '')

    characters = {}

    for char in astring:
        if char not in characters:
            characters[char] = 1
        else:
            return 'Not all unique'
    return 'All unique'

print(all_unique('Hello world'))
print(all_unique('world  '))


# Without an auxiliary data structure

def all_unique2(astring):
    astring = astring.lower()
    astring = astring.replace(' ', '')

    count = 0

    for char in astring:
        count = astring.count(char)
        if count>1:
            return 'Not all unique'
        astring = astring.replace(char, '')
    return 'All unique'

print(all_unique2('Hello world'))
print(all_unique2('world  '))


# Without auxiliary data structure - simplest

def all_unique3(astring):
    # use set function 
    # it returns a set of all the characters in the string, duplicates removed
    # if a string only contains unique chars, the length of the set will be equal to the length of the original string as nothing will have been removed
    # if a string contains duplicates, the length of the set will be different to the length of the original string

    astring = astring.lower()
    astring = astring.replace(' ', '')

    return len(astring) == len(set(astring))

print(all_unique3('Hello world'))
print(all_unique3('world  '))
        
    
        

