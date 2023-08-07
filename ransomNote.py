class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        zineApp = {}
        for c in magazine:
            if c in zineApp:
                zineApp[c] += 1
            else:
                zineApp[c] = 1
        
        for c in ransomNote:
            if c not in zineApp or zineApp[c] < 1:
                return False
            else:
                zineApp[c] -= 1
        return True