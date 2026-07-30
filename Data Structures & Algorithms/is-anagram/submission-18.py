class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictMapS = {}
        dictMapT = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            dictMapS[s[i]] = dictMapS.get(s[i], 0) + 1
            dictMapT[t[i]] = dictMapT.get(t[i], 0) + 1
        return dictMapS == dictMapT
        

    
        
        