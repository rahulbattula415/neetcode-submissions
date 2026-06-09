class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        product = 1
        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        product = 1
        print(prefix)
        for i in range(len(nums)-1, -1, -1):
            suffix.insert(0, product)
            product *= nums[i]
        res = []
        print(suffix)
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res
        