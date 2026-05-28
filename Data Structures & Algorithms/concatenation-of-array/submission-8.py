class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ary = []
        for i in range(2):
            for num in nums:
                ary.append(num)
        return ary
