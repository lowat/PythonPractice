def firstNonRepeatingCharacter(string):
    charFrequencies = {}
    for char in string:
        charFrequencies[char] = charFrequencies.get(char, 0) + 1

    for i, char in enumerate(string):
       if(charFrequencies[char] == 1):
           return i

    return -1