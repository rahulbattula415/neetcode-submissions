class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = []
        hm = {}
        i = len(nums) - 1
        while i >= 0:
            num = nums[i]
            count = 0
            while num in nums:
                nums.remove(num)
                count += 1
            i = len(nums) - 1
            hm[num] = count
        
        for key in hm:
            freqTable.append([hm[key], key])
        freqTable.sort()

        retList = []
        print(freqTable)
        while k > 0:
            retList.append(freqTable.pop()[1])
            k -= 1
        return retList
        
        
        