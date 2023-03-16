def generateDocument(characters, document):
   return ableToGenerateDocumentFromCharMap(document, generateCharMapFromString(characters));

def generateCharMapFromString(string):
    charMap = {}
    for char in string:
        charMap[char] = charMap.get(char, 0) + 1
    return charMap

def ableToGenerateDocumentFromCharMap(document, charMap):
    for char in document:
        if(not char in charMap):
            return False

        charStockRemaining = charMap[char]
        if(charStockRemaining <= 0):
            return False

        charMap[char] = charStockRemaining - 1
    return True