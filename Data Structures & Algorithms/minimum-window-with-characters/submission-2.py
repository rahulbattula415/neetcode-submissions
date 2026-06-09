class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ""
        
        needMap = {}
        haveMap = {}
        for char in t:
            if char in needMap:
                needMap[char] += 1
            else:
                needMap[char] = 1
            haveMap[char] = 0

        needCount = len(needMap)
        haveCount = 0
        
        l = 0
        r = 0
        res = (0, len(s) + 1)
        while r < len(s):
            if s[r] in needMap:
                haveMap[s[r]] += 1
                if haveMap[s[r]] == needMap[s[r]]:
                    haveCount += 1
            while haveCount >= needCount:
                if s[l] in haveMap:
                    haveMap[s[l]] -= 1
                    if haveMap[s[l]] < needMap[s[l]]:
                        haveCount -= 1
                if haveCount < needCount and len(s[l:r + 1]) < res[1] - res[0]:
                    res = (l, r + 1)
                l += 1
            r += 1
        if res == (0, len(s) + 1):
            return ""
        return s[res[0]:res[1]]