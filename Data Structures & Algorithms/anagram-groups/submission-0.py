class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        retList = []
        for i in strs:
            my_str = "".join(sorted(i))
            if my_str in my_dict:
                my_dict[my_str].append(i)
            else:
                my_dict[my_str] = [i]
        for i in my_dict:
            retList.append(my_dict[i])
        return retList
