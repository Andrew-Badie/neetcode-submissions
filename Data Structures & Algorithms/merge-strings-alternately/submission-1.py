class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        n, m = len(word1), len(word2)
        output = ""

        while l < n or r < m:
            if l < n:
                output += word1[l]
                l += 1
            if r < m:
                output += word2[r]
                r += 1
        return output