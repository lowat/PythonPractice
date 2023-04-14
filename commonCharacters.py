def commonCharacters(strings):
    commonCharSet = set(strings[0])
    newCommonCharSet = set()
    
    for i in range(1, len(strings)):
        currentWord = strings[i]
        newCommonCharSet = set()
        for char in currentWord:
            if(char in commonCharSet):
                newCommonCharSet.add(char)
        commonCharSet = newCommonCharSet
    return commonCharSet