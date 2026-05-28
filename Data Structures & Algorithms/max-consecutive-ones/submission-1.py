class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1, score = 0, 0
        for num in nums:
            if num == 1:
                score += 1 
            else:
                max1 = max(score, max1)
                score = 0
        return max(score, max1)
        