class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = 0
        while l < r:
            tempMax = (r - l) * min(heights[l], heights[r])
            if tempMax > maxWater:
                maxWater = tempMax
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater