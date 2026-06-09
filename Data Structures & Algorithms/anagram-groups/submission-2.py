class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for idx in range(len(strs)):
            sortedS = ''.join(sorted(strs[idx]))
            if sortedS in hm:
                hm[sortedS].append(strs[idx])
            else:
                hm[sortedS] = [strs[idx]]
        
        print(hm.values())
        return list(hm.values())