class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        retList = []
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
            if len(retList) < k and i not in retList:
                retList.append(i)
            else:
                for j in retList:
                    if myDict[i] > myDict[j] and i not in retList:
                        retList.remove(j)
                        retList.append(i)
                    else:
                        continue
        return retList
        