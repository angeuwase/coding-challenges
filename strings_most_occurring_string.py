# Given a list of strings, find the string that occurs the most. 


def most_occurring(myList):
    words = {}

    for astring in myList:
        if astring not in words:
            words[astring] = 1
        words[astring] += 1
    max = 0
    most_occurring = None
    for key, value in words.items():
        if value > max:
            max = value
            most_occurring = key

    return most_occurring


mylist = ["geeks", "for", "geeks", "a", 
                "portal", "to", "learn", "can",
                "be", "computer", "science", 
                 "zoom", "yup", "fire", "in", 
                 "be", "data", "geeks", 'be', 'be', 'be']

print(most_occurring(mylist))

        
