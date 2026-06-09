class Solution:
    def search(self, nums: List[int], target: int) -> int:
        tempL = 0
        tempR = len(nums) - 1
        while tempL < tempR:
            if nums[tempL] < nums[tempR]:
                break
            tempMid = int((tempL + tempR) / 2)
            if nums[tempMid] < nums[tempL]:
                tempR = tempMid
            else:
                tempL = tempMid + 1
        
        minIndex = tempL
        if target < nums[0]:
            l = minIndex
            r = len(nums) - 1
        else:
            l = 0
            r = minIndex - 1
            if r == -1:
                r = len(nums) - 1
        

        while l < r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                mid = int((l + r) / 2)
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        if nums[l] == target:
            return l
        else:
            return -1

        