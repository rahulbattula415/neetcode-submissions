class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProdArr = []
        postfixProdArr = []
        product = 1
        for n in nums:
            product = product * n
            prefixProdArr.append(product)
        product = 1
        for idx in range(len(nums) - 1, -1, -1):
            product *= nums[idx]
            postfixProdArr.insert(0, product)
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfixProdArr[i + 1])
            elif i == len(nums) - 1:
                output.append(prefixProdArr[i - 1])
            else:
                output.append(prefixProdArr[i-1] * postfixProdArr[i+1])
        return output
