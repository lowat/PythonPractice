from collections import defaultdict

def isAnagram(s, t):
    sDict = makeDict(s)
    tDict = makeDict(t)
    for k, v in sDict.items():
        if not k in tDict:
            return False
        if tDict[k] != v:
            return False
    return True

def makeDict(word):
    wordDict = defaultdict(lambda: 0)
    for c in word:
        wordDict[c] += 1
    return wordDict

print(isAnagram('cat','tac'))