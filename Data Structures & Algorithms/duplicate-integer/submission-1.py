class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            removed = nums.pop(i)
            if removed in nums:
                return True;
            nums.insert(i, removed)
        return False;