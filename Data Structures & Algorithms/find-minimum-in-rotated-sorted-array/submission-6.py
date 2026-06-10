class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                break
            else:
                mid = (l + r) // 2
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid
            print(l, r)
        return nums[l]
        