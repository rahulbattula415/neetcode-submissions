class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ""
        for s in strs:
            finalStr += str(len(s)) + "#" + s
        print(finalStr)
        return finalStr

    def decode(self, s: str) -> List[str]:
        idx = 0
        finalArr = []
        while idx < len(s):
            length = ""
            while s[idx] != "#":
                length += s[idx]
                idx += 1
            length = int(length)
            finalArr.append(s[idx+1:idx+1+length])
            idx += 1 + length
        return finalArr