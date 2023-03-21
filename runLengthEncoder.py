def runLengthEncoding(string):
    currentChar = string[0];
    currentCharCount = 0;
    encodedStringChars = [];
    for character in string:
        if(character != currentChar or currentCharCount >= 9):
            encodedStringChars.append(str(currentCharCount))
            encodedStringChars.append(currentChar);
            currentChar = character
            currentCharCount = 0
        currentCharCount += 1
    encodedStringChars.append(str(currentCharCount))
    encodedStringChars.append(currentChar);
    return "".join(encodedStringChars)