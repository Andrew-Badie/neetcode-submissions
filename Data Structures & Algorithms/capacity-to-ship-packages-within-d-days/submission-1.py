class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(m):
            ships, currentCap = 1, m

            for w in weights:
                if currentCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currentCap = m
                    
                currentCap -= w
            return True
        
        while l <= r:
            m = (l+r) // 2

            if canShip(m):
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
            
        
        return res
