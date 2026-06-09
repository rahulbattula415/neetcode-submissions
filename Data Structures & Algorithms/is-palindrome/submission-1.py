class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        validChars = "abcdefghijklmnopqrstuvwxyz0123456789"
        for idx in range(len(s) - 1, -1, -1):
            print(s[idx])
            if s[idx] in validChars:
                continue
            else:
                s = s[:idx] + s[idx+1:]
        if s == s[::-1]:
            return True
        return False