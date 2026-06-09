class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        r = 1
        maxLen = 1
        tempLen = 1
        while r < len(s):
            if s[r] in s[l:r]:
                while s[r] in s[l:r]:
                    l += 1
                tempLen = r - l + 1
            else:
                tempLen += 1
                maxLen = max(maxLen, tempLen)
            r += 1
        return maxLen
