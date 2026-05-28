class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in hashM:
                hashM[nums[i]] = i
            else:
                return [hashM[diff], i]


