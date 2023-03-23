def semordnilap(words):
    wordSet = set(words)
    semordnilapPairs = []
    for word in words:
        reversedWord = word[::-1]
        if reversedWord in wordSet and word != reversedWord:
            semordnilapPairs.append([word, reversedWord])
            wordSet.discard(word)
            wordSet.discard(reversedWord)
    return semordnilapPairs
