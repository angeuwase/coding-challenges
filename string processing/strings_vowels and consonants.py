# How to count the number of vowels and consonents in a given string

def count_vowels_and_cons(astring):
    astring = astring.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    #ordinal value of small letters is 97 to 122

    results = {'vowels': 0, 'consonants': 0}

    for char in astring:
        if char in vowels:
            results['vowels'] +=1
        if ord(char) >= 97 and ord(char) <=122:
            if char not in vowels:
                results['consonants'] +=1

    return results

print(count_vowels_and_cons('Hello world!'))