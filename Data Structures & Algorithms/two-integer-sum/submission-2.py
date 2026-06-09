class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for idx, val in enumerate(nums):
            if (target - val) in myDict:
                return [myDict[target-val], idx]
            myDict[val] = idx
        return None
        