class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in myDict:
                myDict[s_sorted].append(s)
            else:
                myDict[s_sorted] = [s]
        res = []
        for key in myDict:
            res.append(myDict[key])
        return res
