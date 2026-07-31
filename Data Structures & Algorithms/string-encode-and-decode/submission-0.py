class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            j = start
            while s[j] != "#":
                j += 1
        
            length = int(s[start:j])
            start = j + 1
            j = start + length
            res.append(s[start:j])
            
            start = j
        return res
