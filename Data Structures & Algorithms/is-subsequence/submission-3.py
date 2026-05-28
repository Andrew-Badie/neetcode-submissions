class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        for i in range(len(t)):
            if l < len(s) and t[r] == s[l]:
                l += 1
            r += 1
        return l == len(s)