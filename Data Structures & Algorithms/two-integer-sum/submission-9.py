class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, c in enumerate(nums):
            diff = target - c
            
            if diff in count:
                return [count[diff], i]
            count[c] = i
