class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                t = t[0:t.index(char)] + t[t.index(char)+1:]
            else:
                return False
        if len(t) != 0:
            return False
        return True