class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)
        length = 0
        

        for num in hashNums:
            res = []
            prev = num - 1
            after = num + 1
            if prev not in hashNums:
                res.append(num)
                while after in hashNums:
                    res.append(after)
                    after += 1
            if len(res) > length:
                length = len(res)
        return length