
class Solution:
    def minEatingSpeed(self, piles: 'List[int]', H: int) -> int:
        count = 1
        hour = 0
        while True:
            for p in piles:
                hour += p/count // 1
                if p/count % 1 > 0:
                    hour += 1
                
            if not hour == H:
                count += 1
                hour = 0
                
            else:
                return count
            

sol = Solution()
sol.minEatingSpeed(piles = [30,11,23,4,20], H = 6)

