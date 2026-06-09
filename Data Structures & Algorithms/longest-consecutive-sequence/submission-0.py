class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)
        maxLen = 0
        for n in newNums:
            if n - 1 not in newNums:
                tempSequence = []
                while n in newNums:
                    tempSequence.append(n)
                    n = n + 1
                if len(tempSequence) > maxLen:
                    maxLen = len(tempSequence)
        return maxLen
