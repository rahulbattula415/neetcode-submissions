class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        retList = []
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)
        print(sorted_keys)
        for i in range(k):
            retList.append(sorted_keys[i])
        return retList
