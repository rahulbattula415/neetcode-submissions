class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(1)
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j] 
        return res
        