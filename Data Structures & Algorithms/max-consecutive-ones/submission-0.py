class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        score = 0
        for num in nums:
            if num == 1:
                score += 1 
            if max1 < score:
                max1 = score
            if num == 0:
                score = 0
        return max1
        