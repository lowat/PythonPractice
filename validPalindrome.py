class Solution(object):
    def isAlphaNumeric(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            if not self.isAlphaNumeric(s[left]):
                left += 1
                continue
            if not self.isAlphaNumeric(s[right]):
                right -= 1
                continue
            if not s[left].lower() == s[right].lower():
                return False
            left += 1
            right -= 1
        return True