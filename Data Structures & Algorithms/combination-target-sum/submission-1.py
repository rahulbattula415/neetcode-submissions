class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(total, i, currArr):
            if total > target or i >= len(nums):
                return
            if total == target:
                res.append(currArr.copy())
                return
            currArr.append(nums[i])
            dfs(total + nums[i], i, currArr)
            currArr.pop()
            dfs(total, i + 1, currArr)
        
        dfs(0, 0, [])
        return res