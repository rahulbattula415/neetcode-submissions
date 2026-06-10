class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        minIndex = l
        if minIndex == 0:
            l = 0
            r = len(nums) - 1
        elif target < nums[0]:
            l = minIndex
            r = len(nums) - 1
        else:
            l = 0
            r = minIndex - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] == target:
            return l
        else:
            return -1