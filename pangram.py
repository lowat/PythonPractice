class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentenceSet = {c for c in sentence}
        return len(sentenceSet) == 26